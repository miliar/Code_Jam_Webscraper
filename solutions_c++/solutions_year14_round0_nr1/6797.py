#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define uint unsigned int

typedef pair<int,int> pii;
#define x first
#define y second

#define read(n) scanf("%d",&n)
#define readll(n) scanf("%lld",&n)
#define read2(n,m) scanf("%d%d",&n,&m)
#define read3(n,m,l) scanf("%d%d%d",&n,&m,&l)

#define fr(i,n)     for(int i=0;i<n;i++)
#define frr(i,a,b)   for(int i=a;i<b;i++)
#define rf(i,n)     for(int i=n-1;i>=0;i--)

#define init(mem,v) memset(mem,v,sizeof(mem))

#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#define DB4(a, b, c, d)    cout<<__LINE__<<" :: "<<#a<< ": "<<a<<" | "<<#b<< ": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;

int main(){
    int mat[4][4];
    int t,g1,g2;
    read(t);
    for(int ii=1;ii<=t;ii++){
        set<int> s;
        read(g1);
        g1--;
        fr(i,4) fr(j,4) read(mat[i][j]);
        fr(i,4) s.insert(mat[g1][i]);

        read(g2);
        g2--;
        fr(i,4) fr(j,4) read(mat[i][j]);
        int cnt=0,val;
        fr(i,4) if(s.find(mat[g2][i]) != s.end()){cnt++;val=mat[g2][i];}

        if(cnt==1) printf("Case #%d: %d\n",ii,val);
        else if(cnt==0) printf("Case #%d: Volunteer cheated!\n",ii);
        else printf("Case #%d: Bad magician!\n",ii);
    }
}
