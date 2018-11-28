#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

#define SIZE 1000//0000

unordered_map<long long, bool> hm;
vector<long long> ans;
int A, B;
int nr_case = 1;

bool isPalindrome(long long x) {
    char str[100];
    char *p, *q;

    sprintf(str, "%I64d", x);
    p = str;
    q = &str[strlen(str) - 1];
    while (p <= q) {
        if (*p != *q)
            return false;
        p++;
        q--;
    }
    return true;
}

bool isSquare(long long x) {
    if ((long long)sqrt((double)x) * (long long)sqrt((double)x) == x)
        return true;
    return false;
}

void compute() {
    int count = 0;
    long long s;

    ans.clear();
    hm.clear();
    for (long long i = 1; i <= SIZE; i++) {
        //fair[i] = isPalindrome(i);
        if (isPalindrome(i) && isSquare(i) && isPalindrome((long long)sqrt((double)i))) {
            if(hm[i] == 0) {
                ans.push_back(i);
                hm[i] = true;
                count++;
                //cout << i << endl;
            }
        }
        s = i * i;
        if (isPalindrome(i) && isPalindrome(s) && hm[s] == 0) {
            ans.push_back(s);
            hm[s] = true;
            //cout << s << endl;
            count++;
        }
    }
    //cout << count << endl;
    sort(ans.begin(), ans.begin() + ans.size());
    //for (unsigned int i = 0; i < ans.size(); i++)
    //    cout << ans.at(i) << endl;
}

void solve() {
    int start, _end;
    for (unsigned int i = 0; i < ans.size(); i++)
        if (A <= ans.at(i)) {
            start = i;
            break;
        }

    for (unsigned int i = 0; i < ans.size(); i++)
        if (B <= ans.at(i)) {
            if (B == ans.at(i))
                _end = i;
            else
                _end = i - 1;
            break;
        }
    //cout << "start : " << start << endl;
    //cout << "end : " << _end << endl;
    cout << "Case #" << nr_case << ": " << _end - start + 1 << endl;
    nr_case++;
}

int main()
{
    int T;


    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    compute();
    cin >> T;
    while (T--) {
        cin >> A >> B;
        solve();
    }
    return 0;
}
