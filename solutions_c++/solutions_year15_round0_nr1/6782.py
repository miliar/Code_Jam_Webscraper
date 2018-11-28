#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<set>
using namespace std;
#define PI 2 * acos (0.0)


int main()
{
    freopen("C:\\Users\\talha629\\Desktop\\New folder\\A-large.in","r",stdin);
    freopen("C:\\Users\\talha629\\Desktop\\New folder\\A-large.out","w",stdout);
    int tc,t=1,p,c,x,y,i,n;
    char s[1010];
    scanf("%d",&tc);
    while(tc--){
        scanf("%d",&n);
        scanf("%s",&s);
        p=0;
        c=0;
        for(i=0;i<=n;i++){
            x = s[i]-'0';
            if(i==0)
                c+=x;
            else{
                if(i>c){
                    y=i-c;
                    p+=y;
                    c+=y;
                    c+=x;
                }
                else{
                    c+=x;
                }
            }
        }
        printf("Case #%d: %d\n",t++,p);
    }
    return 0;
}
