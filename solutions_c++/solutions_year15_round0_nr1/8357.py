#include <bits/stdc++.h>
using namespace std;
#define s second
#define f first
#define mp make_pair
#define ll long long
#define pb push_back
#define fr(i,s,n) for(int i=s; i<n; i++)
#define sz size()
#define mmst(a,x) memset(a,x,sizeof(a))
#define scan(x) scanf("%d",&x)
#define pii pair<int,int>
#define db(x) cout<< #x<<'='<<x<<' ';
#define _ cout<<'\n'

int main(){
    freopen ("ab.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int ans,t,n,own,c=1;
    string s;
    cin>>t;
    while(t--){
        cin>>n;
        cin>>s;
        ans=0;
        own=0;
        int tmp=0;
        for(int i=0; i<=n; i++){
            if(own<i) {
                tmp+=1;
            }
            if(s[i]>'0'){
                own+=(s[i]-'0')+tmp;
                ans+=tmp;
                tmp=0;
            }
        }
        printf("Case #%d: %d\n",c++,ans);
    }
}
