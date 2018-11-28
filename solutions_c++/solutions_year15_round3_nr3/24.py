#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <memory.h>
#include <ctime>
//#include <fstream>
using namespace std;
 
using namespace std;

#define INF 1000000000
#define MP make_pair
#define FILL(a,value) memset(a,value,sizeof(a))
#define MOD 1000000009
double const PI = acos(-1.0);
double const EPS=1e-7;

long long a[100];


void solve(){
   long long c, n, m;
   cin>>c>>n>>m;

   for (int i=0; i<n; i++){
       cin>>a[i];
   }

   sort(a,a+n);

   long long s = 0;
   int res=0;
   for (int i=0; i<n; i++){
       if (s>=m) continue;
       if (a[i] <= s){
           s += a[i] * c;
       }
       else
       if (a[i] != s+1){
           res++;
           s += (s+1) * c;
           i--;
       }
       else if (a[i] == s+1) s += a[i] * c;
   }

   while(s<m){
       s += (s+1)*c;
       res ++;
   }

   cout<<res<<endl;
}

int main(){

	freopen("in.txt","r",stdin);
	freopen("OUTPUT.txt","w",stdout);

	int tt;
	cin>>tt;

	//string str;
	//getline(cin,str);

	for (int t=1; t<=tt; t++){
		cout<<"Case #"<<t<<": ";
		int time=clock();
		solve();
		cerr<<"\t\tCase #"<<t<<"\t time="<<clock()-time<<endl;
	}

}