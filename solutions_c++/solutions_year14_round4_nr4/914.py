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

string s[100];
int mp[100];
set<string> st[100];
int m,n;


bool term(){
    fr(i,m) if(mp[i]!=n-1) return false;
    return true;
}


void incmp(){
    int c=1;
    fr(i,m){
        mp[i]+=c;
        c=mp[i]/n;
        mp[i]%=n;
    }
}


int main(){
    int t;
    read(t);
    frr(ii,1,t+1){
        read2(m,n);

        fr(i,m) cin>>s[i];


        fr(i,m) mp[i]=0;
        int bst=0,ways=1;
        while(1){
            fr(i,n) st[i].clear();

            fr(i,m){
                string pre="";
                st[mp[i]].insert(pre);
                fr(j,s[i].size()){
                    pre+=s[i][j];
                    st[mp[i]].insert(pre);
                }
            }
            int v=0;
            fr(i,n){
                v+=st[i].size();
                if(st[i].size() == 0) v=INT_MIN;
            }
            if(v>bst){
                bst=v;ways=1;
            }
            else if(v==bst) ways++;
            if(term()) break;
            incmp();
        }
        printf("Case #%d: %d %d\n",ii,bst,ways);
    }
}
