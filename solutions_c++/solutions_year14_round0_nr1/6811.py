#include<algorithm>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<stack>
using namespace std;
#define MAXN 5005
#define MAXM 20005
#define ll long long
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef stack<int> si;
int main(){
    int T,n,m;
    int a[4][4],b[4][4];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&n);
        n--;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&m);
        m--;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&b[i][j]);
            }
        }
        int cnt=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[n][i]==b[m][j])cnt++;
            }
        }
        if(cnt==0){
            printf("Case #%d: Volunteer cheated!\n",t);
        }
        else if(cnt==1){
                int x;
            for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[n][i]==b[m][j]){x=a[n][i];break;}
            }
            }
            printf("Case #%d: %d\n",t,x);
        }
        else{
            printf("Case #%d: Bad magician!\n",t);
        }
    }
    return 0;
}
