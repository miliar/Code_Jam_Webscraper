#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int a[105];
char str[105];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t = 0;
    scanf("%d",&T);
    while(T--){
        scanf("%s",str);
        int len = strlen(str);
        for(int i = 0; i < len; ++i){
            if(str[i] == '+')
                a[i] = 1;
            else
                a[i] = 0;
        }
        int cnt = 0;
        for(int i = len-1; i >= 0; --i){
            if(a[i] == 0){
                ++cnt;
                for(int j = 0; j <= i; ++j)
                    a[j] = !a[j];
                //cout<<i<<endl;
            }
            //cout<<cnt<<endl;
        }
        printf("Case #%d: %d\n",++t,cnt);
    }
    return 0;
}
