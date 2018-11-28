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

vector<pair<char,int> > a[1000];

void solve(){
	int n;
    cin>>n;
    for (int i=0; i<n; i++){
        a[i].clear();
        string s;
        cin>>s;

        a[i].push_back(MP(s[0],1));
        for (int j=1; j<s.length(); j++){
            if (s[j]==a[i][a[i].size()-1].first){
                a[i][a[i].size()-1].second++;
            }
            else{
                a[i].push_back(MP(s[j],1));
            }
        }
    }

    bool ok=true;
    for (int i=1; i<n; i++){
        if (a[i].size()!=a[0].size()){
            ok=false;
            break;
        }

        for (int j=0; j<a[0].size(); j++){
            if (a[0][j].first!=a[i][j].first){
                ok=false;
            }
        }
    }

    if (!ok){
        cout<<"Fegla Won"<<endl;
        return;
    }

    int res=0;

    for (int i=0; i<a[0].size(); i++){
        vector<int> A;
        for (int j=0; j<n; j++){
            A.push_back(a[j][i].second);
        }

        sort(A.begin(),A.end());

        for (int j=0; j<A.size(); j++){
            res+=abs(A[j]-A[A.size()/2]);
        }
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