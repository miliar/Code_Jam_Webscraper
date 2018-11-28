#include <stdio.h>
#include <math.h>
using namespace std;

int main() {

    int T;
    int s_max=0;
    char aud_list[1001];
    int sum;
    int aud_req;

    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);

    while(scanf("%d",&T)==1 && T<=100)
    {
        for(int t=1;t<=T;t++){

        scanf("%d %s", &s_max, &aud_list);
        //printf("%s\n", aud_list);
        sum=aud_req=0;

        for(int i=0;i<=s_max;i++){

            if(i>0){
                if(i>sum){
                    (i-sum)>aud_req ? aud_req=i-sum:aud_req;
                }

                (int)(aud_list[i]-'0')>0 ? sum+=aud_list[i]-'0':sum;
            }
            else{
                //sum+=aud_list[i]-'0';
                (int)(aud_list[i]-'0')>0 ? sum+=aud_list[i]-'0':sum;
            }
            //printf("sum %d, aud_req %d, i=%d\n", sum, aud_req,i);
        }
        printf("Case #%d: %d\n", t, aud_req);
        }
    }
    return 0;
}
