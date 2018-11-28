//__hr1212__//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mi;

#define si(a) scanf("%d",&a)
#define sii(a,b) scanf("%d %d",&a,&b)
#define nl printf("\n");
#define pi(a) printf("%d\n",a)
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define f(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b) for(i=a;i>=b;i--)
#define clr(x,a) memset(x,a,sizeof(x))
#define MAX 1000100
#define MOD 1000000007
#define F first
#define S second

int n,m,a[MAX],b[MAX];

int main(){
    int r,k,i,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0;
    ll ans=0;string p;

    si(t);
    f(j,1,t+1){
        cin>>p;
        c=0;
        f(i,0,p.size()-1){
            if(p[i]!=p[i+1])
                c++;
        }
        if(p[p.size()-1]=='-')
            c++;
        printf("Case #%d: %d",j,c);
        nl;
    }

    return 0;
}
