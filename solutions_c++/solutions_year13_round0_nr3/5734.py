#include <cstdio>
#include <vector>

bool palindrom[1001];
bool fair[1001];
int pre[1001];

int main() {
    for(int i = 1; i <= 1000; i++) {
        std::vector<int> v;
        int t = i;
        while(t) {
            v.push_back(t % 10);
            t /= 10;
        }
        bool b = true;
        for(int j = 0; j < v.size() / 2 + 1 && b; j++)
            if(v[v.size() - 1 - j] != v[j])
                b = false;
        if(b)
            palindrom[i] = true;
    }
    for(int i = 1; i < 32; i++)
        if(palindrom[i])
            if(palindrom[i * i])
                fair[i * i] = true;
    for(int i = 1; i <= 1000; i++)
        if(fair[i])
            pre[i] = pre[i - 1] + 1;
        else
            pre[i] = pre[i - 1];
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        a--;
        printf("Case #%d: %d\n", i + 1, pre[b] - pre[a]);
    }
    return 0;
}