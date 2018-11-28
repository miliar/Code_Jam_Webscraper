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

int a[100100];

void solve(){
	int n;
    cin>>n;
    for (int i=0; i<n; i++){
        cin>>a[i];
    }

    int res=INF;

    for (int i=1; i<=10000; i++){
        int c=0;
        for (int j=0; j<n; j++){
            c += a[j] / i;
            if (a[j] % i == 0) c--;
        }
        c+=i;
        res=min(res,c);
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