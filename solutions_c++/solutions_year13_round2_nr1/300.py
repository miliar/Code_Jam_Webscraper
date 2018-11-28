//#pragma comment(linker, "/stack:16777216")
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

int a[100];

void solve()
{
	int s;
	cin>>s;
	int n;
	cin>>n;
	for (int i=0; i<n; i++){
		int x;
		cin>>x;
		a[i]=x;
	}

	if (s==1){
		cout<<n<<endl;
		return;
	}

	sort(a,a+n);
	int res=INF;
	int c=0;
	for (int i=0; i<n; i++){
		res=min(res,c+n-i);
		if (a[i]<s) s+=a[i];
		else{
			while(s<=a[i]){
				s+=s-1;
				c++;
			}
			s+=a[i];
		}
	}
	res=min(res,c);

	cout<<res<<endl;
}

int main()
{

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