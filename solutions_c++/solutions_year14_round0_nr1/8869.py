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


void solve(){
	int x;
    cin>>x;
    x--;
    set<int> s;
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            int y;
            cin>>y;
            if (i!=x) continue;
            s.insert(y);
        }
    }

    set<int> ss;

    cin>>x;
    x--;
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            int y;
            cin>>y;
            if (i!=x) continue;
            if (s.find(y)!=s.end()) ss.insert(y);
        }
    }

    if (ss.empty()) cout<<"Volunteer cheated!"<<endl;
    else if (ss.size()>1) cout<<"Bad magician!"<<endl;
    else cout<<*ss.begin()<<endl;
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