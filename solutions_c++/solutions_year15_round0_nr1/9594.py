#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int T;
    cin >> T;
    for(int qqq = 0; qqq < T; qqq++){
        int smax;
        char c;
        scanf("%d%c", &smax, &c);
        int add = 0;
        int sum = 0;
        for(int i = 0; i <= smax; i ++){
            scanf("%c", &c);
            int tmp = c-'0';
            if(tmp){
                if(sum >= i){
                    sum += tmp;
                }else{
                    add += i-sum;
                    sum = i + tmp;
                }
            }
        }
        printf("Case #%d: %d\n", qqq+1, add);

    }
    return 0;
}
