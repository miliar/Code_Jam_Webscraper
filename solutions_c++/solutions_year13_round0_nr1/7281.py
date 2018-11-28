#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <set>
#include <map>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define rp(i,s,n) for((i)=(s);(i)<(n);(i)++)	
#define ll long long
#define MP make_pair 
#define PB push_back
#define X first
#define Y second
#define ALL(a) (a).begin(),(a).end()
#define sz(a) a.size()
#define len(s) s.length() 

using namespace std;			

template <class T>
void out(vector<T> & a,string s="%3d "){
	int i,n=a.size();
	rep(i,n) printf(s.c_str(),a[i]);
	printf("\n");
}

template <class T> 
void out(T * a,int n,string s="%3d "){
	int i;
	rep(i,n) printf(s.c_str(),a[i]);
	printf("\n");
} 

int i,j,N,M,n,m,k,p;

int main() {

#ifndef ONLINE_JUDGE
	freopen("C:\\Olimp2013\\GoogleCodeJam13\\Atictac\\input.txt","r",stdin);freopen("C:\\Olimp2013\\GoogleCodeJam13\\Atictac\\output.txt","w",stdout);
	//FILE * f, *g; f = fopen ("input.txt","r");//g = fopen ("output.txt","w");
#endif

	
	vector<string> a(4,"0000");  


     cin>>n;
    int flag=0;
    rep(k,n){
		
        rep(i,4) cin>>a[i];

       
        flag=0;
		char c='X';
					rep(p,4) {flag=1; rep(i,4)if (a[i][p]!=c && a[i][p]!='T'){flag=0;break;} if (flag)  break;}
        if (!flag)  rep(p,4) {flag=1; rep(i,4)if (a[p][i]!=c && a[p][i]!='T'){flag=0;break;} if (flag)  break;}
        
        if (!flag) { flag=1;
		rep(p,4) if (a[p][p]!=c && a[p][p]!='T') {flag=0;break;}}

		if (!flag) { flag=1;
		rep(p,4) if (a[p][4-p-1]!=c && a[p][4-p-1]!='T') {flag=0;break;}}


        if (flag){
            printf("Case #%d: X won\n",k+1);
            continue;
        }
        

		flag=1;
		c='O';
    rep(p,4) {flag=1; rep(i,4)if (a[i][p]!=c && a[i][p]!='T'){flag=0;break;} if (flag)  break;}
        if (!flag)  rep(p,4) {flag=1; rep(i,4)if (a[p][i]!=c && a[p][i]!='T'){flag=0;break;} if (flag)  break;} 

        if (!flag) { flag=1;
		rep(p,4) if (a[p][p]!=c && a[p][p]!='T') {flag=0;break;}}

		if (!flag) { flag=1;
		rep(p,4) if (a[p][4-p-1]!=c && a[p][4-p-1]!='T') {flag=0;break;}}

        
        if (flag){
			 printf("Case #%d: O won\n",k+1);
			continue;
        }
        else{
			 int draw=1;
        rep(i,4) rep(j,4) if (a[i][j]=='.') draw=0;
        if (draw){
            printf("Case #%d: Draw\n",k+1);
            continue;
        }
        
            printf("Case #%d: Game has not completed\n",k+1);
            continue;
        }
        
    }
	
	
	
return 0;
}