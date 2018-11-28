#include<bits/stdc++.h>
#define ll long long
#define Mod 1000000007
#define F first
#define S second
#define maxm(a,b) (a>b)?a:b
#define minm(a,b) (a<b)?a:b

using namespace std;

typedef pair< ll,ll> pii;
typedef pair<ll,pii> piii;
typedef vector<pii> vii;

int main()
{
    int T,t,i,j,k;
    freopen("B-large.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        int a[121]={0},cnt=0;
        char s[121];
        scanf("%s",s);
        int n=strlen(s);
        for(i=0;i<n;i++)
            if(s[i]=='+')
                a[i]=1;
        if(n==1){
            cnt=(a[0]==0)?1:0;
        }
        else{
            for(i=n-1;i>=0;i--){
                if(!a[i])
                    break;
            }
            n=i+1;
            int temp=a[0];
            for(i=1;i<n;i++){
                if((!temp&&a[i])||(temp&&(!a[i])))
                    cnt++;
                temp=a[i];
            }
            if(!cnt)
                if(!a[0])   cnt=1;
                else    cnt=0;
            else
                cnt++;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
