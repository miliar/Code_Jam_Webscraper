/*Archit Mittal*/

#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include<ios>
#include<fstream>

#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    
    fin.open("inp.in");
    fout.open("out.txt");
    
    int t,i,j,a1,a2,sz2,sz1,pv,nw,ans,x;
    fin>>t;
    int k=1;
    while(t--){
        fout<<"Case #"<<k++<<": ";
        fin>>a1;
        a1--;
        set<int> s;
        F(i,0,4){
            F(j,0,4){
                fin>>x;
                if(i==a1)s.insert(x);
            }
        }
        
        sz1=s.size();
        fin>>a2;
        a2--;
        F(i,0,4){
            F(j,0,4){
                fin>>x;
                pv=s.size();
                if(i==a2)s.insert(x);
                nw=s.size();
                if(i==a2 && pv==nw)ans=x;
            }
        }
        
        sz2=s.size();
        //cout<<a1<<" "<<a2<<" "<<s.size()<<endl;system("pause");
        if(sz2==8)fout<<"Volunteer cheated!\n";
        else if(sz2==7)fout<<ans<<endl;
        else fout<<"Bad magician!\n";
    }
    //int tmp;cin>>tmp;
}
