#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define uint unsigned int

typedef pair<int,int> pii;
#define x first
#define y second
#define pb push_back

#define read(n) scanf("%d",&n)
#define read2(n,m) scanf("%d%d",&n,&m)
#define read3(n,m,l) scanf("%d%d%d",&n,&m,&l)

#define fr(i,n)     for(int i=0;i<n;i++)
#define frr(i,a,b)   for(int i=a;i<b;i++)

#define init(mem,v) memset(mem,v,sizeof(mem))

#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#define DB4(a, b, c, d)    cout<<__LINE__<<" :: "<<#a<< ": "<<a<<" | "<<#b<< ": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;

int a[10000];
map<int,int> p;


int inve(vector<int> v){
    int ans=0;
    fr(i,v.size()) frr(j,i+1,v.size()){
        if(v[i]>v[j]) ans++;
    }
    return ans;
}

int main(){
    int t,n;
    read(t);
    frr(ii,1,t+1){
        read(n);
        p.clear();
        fr(i,n){
            read(a[i]);
            p[a[i]]=i;
        }

        int L=*max_element(a,a+n);
        int pos=0;fr(i,n) if(a[i]==L) pos=i;

        int ans=2000000000;
        for(int mask=0;mask<(1<<n);mask++){
            if(mask & (1<<pos)) continue;
            vector<int> v1,v2,v;
            fr(i,n) if(i!=pos){
                if(mask & (1<<i)) v1.pb(a[i]);
                else v2.pb(a[i]);
            }
            sort(v1.begin(),v1.end());
            sort(v2.begin(),v2.end());
            reverse(v2.begin(),v2.end());

            fr(i,v1.size()) v.pb(p[v1[i]]);
            v.pb(p[L]);
            fr(i,v2.size()) v.pb(p[v2[i]]);

            ans=min(ans,inve(v));
        }

        printf("Case #%d: %d\n",ii,ans);

    }
}
