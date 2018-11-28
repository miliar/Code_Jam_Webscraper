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
#include<iomanip>

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
  
  	int t;  
    vector<int> tmp;
    fin>>t;

    int n,m,k;
    int ts=1;
    int i,j;
    int val;
    while(t--){
	    int cnt=0;
	    fout<<"Case #"<<ts++<<": ";
	    fin>>n>>m>>k;
	    F(i,0,n){
		    F(j,0,m){
			    val=(i&j);
			    if(val<k)cnt++;
		    }
	    }
	    fout<<cnt<<endl;
    }
}
