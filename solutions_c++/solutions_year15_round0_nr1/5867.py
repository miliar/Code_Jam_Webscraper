#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define SIZE_A 3300
using namespace std;
char a[SIZE_A];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    while (~scanf("%d",&T)){
        int smax;
        int cas = 1;
        while (T--){
            scanf("%d",&smax);
            getchar();
            scanf("%s",a);
            int sum = 0;
            int stand = 0;
            int res = 0;
            for (int i = 0; a[i]; i++){
            //printf("%d\n",i);
                if ( i > stand){

                    int temp = i - stand;
                    res += temp;
                    stand += temp;
                }stand += a[i]-'0';
                if (a[i] == '0'){
                    sum++;
                }
            }
            if (sum == smax+1)
                printf("Case #%d: 0\n",cas++);
            else
                printf("Case #%d: %d\n",cas++,res);
        }

    }
    return 0;
}
