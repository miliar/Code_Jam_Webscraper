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

int a[101][101];

void solve(){

	int n,m; 
	cin>>n>>m;

	for (int i=0; i<n; i++){
		for (int j=0; j<m; j++){
			cin>>a[i][j];
		}
	}

	int res=1;

	for (int i=0; i<n; i++){
		for (int j=0; j<m; j++){
			bool ok=1;
			for (int k=0; k<n; k++){
				if (a[k][j]>a[i][j]) ok=0;
			}

			if (ok) continue;
			ok=1;
			for (int k=0; k<m; k++){
				if (a[i][k]>a[i][j]) ok=0;
			}
			if (ok) continue;
			res=0;


		}
	}

	if (res) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;

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