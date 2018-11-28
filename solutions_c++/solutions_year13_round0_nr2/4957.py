#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;


ifstream fin("B-large.in");
ofstream fout("B-large.out");

typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<VI> VVI;
using namespace std;


int main(){
    int t;
    fin>>t;
    for(int test=1;test<=t;++test){
        int n,m;
        fin>>n>>m;
        VVI v(n,VI(m));
        for(int i=0;i<n;++i) for(int j=0;j<m;++j) fin>>v[i][j];
        VI f(n,0);
        VI c(m,0);
        for(int i=0;i<n;++i) for(int j=0;j<m;++j) f[i]=max(f[i],v[i][j]);
        for(int j=0;j<m;++j) for(int i=0;i<n;++i) c[j]=max(c[j],v[i][j]);
        bool b=true;
        for(int i=0;i<n;++i) for(int j=0;j<m;++j) if(v[i][j]!=min(c[j],f[i])) b=false;
        fout<<"Case #"<<test<<":";
        if(b) fout<<" YES"<<endl;
        else fout<<" NO"<<endl;
    }
    system("pause");
}
