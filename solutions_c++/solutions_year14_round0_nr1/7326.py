/*
Author : Rashedul Hasan Rijul ( Silent_coder ).
*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>
using namespace std;

#define maxm 1000
#define inf (1<<29)
#define ii int

#define pi  acos(-1.0)
#define eps 1e-9
#define iseq(a,b) (fabs(a-b)<eps)

#define pii pair<int,int>
#define mp  make_pair
#define uu first
#define vv second

ii on(ii n,ii k){ return (n|(1<<k)); }
ii off(ii n,ii k){ return (n-(n&(1<<k))); }
bool chck(ii n,ii k){ return (n&(1<<k)); }

ii mini(ii a,ii b){ if(a<b) return a;  return b;  }
ii maxi(ii a,ii b){ if(a>b) return a;  return b;  }


int main(){

    int i,j,k,l,test,t=1;

    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&test);

    while(test--){

        int ans1,ans2;
        bool can[17]={0};

        scanf("%d",&ans1);

        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                int tmp;
                scanf("%d",&tmp);
                if(i==ans1) can[tmp]=1;
            }
        }

        bool flag=0;

        scanf("%d",&ans2);

        int ans=-1;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                int tmp;
                scanf("%d",&tmp);
                if(i==ans2){
                    if(can[tmp] && ans==-1){
                        ans=tmp;
                    }
                    else if(can[tmp]){
                        flag=1;
                    }
                }
            }
        }

        printf("Case #%d: ",t++);
        if(ans==-1) puts("Volunteer cheated!");
        else if(flag==0) printf("%d\n",ans);
        else             puts("Bad magician!");


    }

    return 0;
}

