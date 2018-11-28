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
    double c,f,x,ans,t1,t2,val,r,curr,t3;
    fin>>t;
    int k=1;
    while(t--){
	    fout<<"Case #"<<k++<<": ";
	    fin>>c>>f>>x;
	    ans=c/2;
	    r=2;
	    curr=c;
	    while(1){
		    t1=(x-curr)/r;
		    if(curr>=c){
			    t2=(x-curr+c)/(r+f);
			    if(t2<=t1){
				    r+=f;
				    curr-=c;
			    } else {
				    ans+=t1;
				    break;
			    }
		    } else {
			    t3=(c-curr)/r;
			    if(t3>=t1){
				    ans+=t1;
				    break;
			    } else {
				    ans+=t3;
			    }
			    curr=c;
		    }
		   // cout<<curr<<" "<<ans<<" "<<r<<endl;getchar();
	    }
	    fout<<fixed<<setprecision(7)<<ans<<endl;
	    //printf("%0.7lf\n",ans);
    }
}


