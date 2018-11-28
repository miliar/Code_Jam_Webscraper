#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#define pii pair<int,int>
#define LL long long
using namespace std;
int t,a,b,d,e;
char c[100];
bool abc(int x){
     sprintf(c,"%d",x);
     d=strlen(c);
     for (int i=0;i<d>>1;i++)
         if (c[i]!=c[d-i-1]) return 0;
     return 1;
     }

int main(){
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        e=0;
        scanf("%d%d",&a,&b);
        for (int j=1;j<=50;j++)
            if (abc(j) && abc(j*j) && j*j>=a && j*j<=b){
               e++;
               }
        printf("Case #%d: %d\n",i,e);
        }
    return 0;
}
