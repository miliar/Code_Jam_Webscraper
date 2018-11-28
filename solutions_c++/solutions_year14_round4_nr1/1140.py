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

int a[10001];

int main(){
    int n,m,t;
    read(t);
    frr(ii,1,t+1){
        read2(n,m);
        multiset<int> s;
        fr(i,n){
            read(a[i]);
            s.insert(a[i]);
        }

        int ans=0;
        while(s.size()>0){
            int rt=*(s.rbegin());
            s.erase(s.find(rt));

            if(s.size()>0){
                multiset<int>::iterator itr=s.lower_bound(m-rt);
                if(itr==s.end() or (itr!=s.begin() and *itr>m-rt)) itr--;

                if(*itr+rt<=m){
                    s.erase(itr);
                }
            }
            ans++;
        }
        printf("Case #%d: %d\n",ii,ans);
    }
}
