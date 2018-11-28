#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>


using namespace std;

void print(int a, int n) {
    while (n--) {
        printf("%d", a & 1);
        a>>=1;
    }
    printf("\n");
}

int solve(const string& s) {
    int a = 0;
    for (int i=0;i<s.size();++i) {
        a *= 2;
        if (s[s.size() - 1 -i] == '-') {
            a += 1;
        } else {
        }
    }

    int mem[1<<20];
    memset(mem,-1,sizeof(mem));
    mem[a] = 0;
    deque<int> q;
    q.push_back(a);
    while (!q.empty()) {
        int cur = q.front();
        q.pop_front();
        if (cur == 0) {
            return mem[cur];
        }
        //print(cur, s.size());

        for (int i = 1; i <=s.size();++i) {
            int pre = cur & ((1<<i) - 1);
            pre = ~pre & ((1<<i) -1);
            for (int j = 0; j < i/2; ++j) {
                bool a = pre & (1<<j);
                bool b = pre & (1<<(i - j - 1));
                if (a) pre |= 1<<(i-j-1); else pre &= ~(1<<(i-j-1));
                if (b) pre |= 1<<j; else pre &= ~(1<<(j));
            }

            int next = (cur & ~((1<<i)-1)) | pre;
            if (mem[next] == -1) {
                mem[next] = mem[cur] + 1;
                q.push_back(next);
                //printf("\t:");
                //print(next, s.size());
            }
        }
    }

    printf("UH OH\n");
    return 0;
}

int solve2(const string& s, int p, bool rev) {
    if (p == -1) return 0;
    if ((s[p] == '+') != rev) {
        return solve2(s, p-1, rev);
    } else {
        return solve2(s, p-1, !rev) + 1;
    }
}



int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        string s;
        cin>>s;

        //int ans1 = solve(s);
        int ans2 = solve2(s, s.size()-1, false);

        printf("Case #%d: %d\n", t, ans2);
    }
}
