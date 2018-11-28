#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;
int T, N, J;

bool num[32] = {};
long long bool_to_ll(int base, bool arr[]) {
    long long n=0;
    long long s=1;
    int i=N;
    while(i--) {
        n += s*arr[i];
        s*=base;
    }

    return n;
}

void solve(int i) {
    if(J<=0) return ;
    if(i>= N-1) {

        vector<int> d;
        for(int i=2;i<=10;i++) {
            long long n = bool_to_ll(i, num);
            long long sq = sqrt(n);

            for(int j=2;j<=sq;j++) {
                if(n % j == 0){
                    d.push_back(j);
                    break;
                }
            }

        }

        if(d.size() == 9) {
            for(int i=0;i<N;i++) {
                printf("%d",num[i]);
            }
            putchar(' ');
            for(auto it = d.begin();it!=d.end();it++) {
                printf("%d ",*it);
            }
            putchar('\n');
            J--;

        }
        return;
    }
//    for(int i=0;i<N;i++) {
//        printf("%d",num[i]);
//    }
//    putchar('\n');
    num[i] = 0;
    solve(i+1);
    num[i] = 1;
    solve(i+1);
}

int main(int argc, char *argv[]) {

    scanf("%d%d%d", &T, &N, &J);
    num[0]= num[N-1] = 1;

    printf("Case #1:\n");
    solve(1);
    return 0;
}
