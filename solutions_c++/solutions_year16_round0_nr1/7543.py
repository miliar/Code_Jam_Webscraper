#include<stdio.h>
#include<algorithm>
using namespace std;
bool digit[10];
int main(){
    int n,t,i,j,k;
    int in,ans;

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    //t = 1000000;
    for(k=0;k<t;k++) {
        scanf("%d",&in);
        //in = k+1;
        bool check = false;

        printf("Case #%d: ",k+1);
        if(in == 0) {
            printf("INSOMNIA\n");
            continue;
        }

        for(j=0;j<10;j++) {
            digit[j] = false;
        }
        for(i=1; true;i++) {
            ans = in*i;
            j = ans;

            while(j>0) {
                digit[j%10] = true;
                j/=10;
            }

            for(j=0;j<10;j++) {
                if(!digit[j])
                    break;
            }
            if(j==10) break;
        }



        if(i>100) {
            printf("INSOMNIA\n");
        } else {
            printf("%d\n",ans);
        }
    }
}
