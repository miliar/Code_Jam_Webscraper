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

double n[1005];
double k[1005];
int main()
{
    ifstream fin;
    ofstream fout;
    
     fin.open("inp.in");
    fout.open("out.txt");
    
    int t,num,i,x,y,p1,p2;
    fin>>t;
    int ks=1;
    while(t--){
	    p1=p2=0;
	    fout<<"Case #"<<ks++<<": ";
	    fin>>num;
	    F(i,0,num)fin>>n[i];		    
	    F(i,0,num)fin>>k[i];

	    //cout<<"archit\n";
	    sort(n,n+num);
	    sort(k,k+num);

	   // F(i,0,num)cout<<n[i]<<" ";cout<<endl;		    
	   // F(i,0,num)cout<<k[i]<<" ";cout<<endl;
	    x=num-1;
	    y=num-1;
	    while(x>=0 && y>=0){
		    if(k[x]>n[y]){
			    p1++;
			    x--;
			    y--;
		    } else {
			    while(y>=0 && n[y]>k[x])y--;
		    }
		   // cout<<x<<" "<<y<<endl;getchar();
	    }
	    p1=num-p1;
	    x=num-1;
	    y=num-1;
	    while(x>=0 && y>=0){
		    if(n[x]>k[y]){
			    p2++;
			    x--;
			    y--;
		    } else {
			    while(y>=0 && n[x]<k[y])y--;
		    }
		   // cout<<x<<" "<<y<<endl;
	    }
	   // p2=num-p2;
	    fout<<p2<<" "<<p1<<endl;
    }
}

