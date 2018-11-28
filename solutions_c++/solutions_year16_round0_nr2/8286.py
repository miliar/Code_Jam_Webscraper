#include<cstdio>
#include<queue>
#include<climits>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<ctype.h>
#include<set>
#include<vector>
#include<map>
#include<time.h>
#include<list>
#include<stack>
using namespace std;
#define mod 1000000007
#define mem(x) memset(x,0,sizeof(x))
#define pri printf
#define sca scanf

typedef long long LL;
const double PI=acos(-1.0);
const double  eps=1e-9;
char S[105];
int main(){
    int n,i,j,m,k,x;
    int T;
    freopen("B-large.txt","r",stdin);
    freopen("B-large.out","w",stdout);
    sca("%d",&T);
    for (int cas=1;cas<=T;cas++){
        sca("%s",S);
        n=strlen(S);
        //S[n]='+';
        m=0;
        while (1){
            j=0;
            while(j<n-1&&S[j+1]==S[j]){j++;}
            if (j==n-1&&S[0]=='+'){
                pri("Case #%d: %d\n",cas,m);
                break;
            }
            for (k=0;k<=j;k++){S[k]=(S[k]=='+'? '-':'+');}
            m++;
        }
    }
    return 0;
}





















