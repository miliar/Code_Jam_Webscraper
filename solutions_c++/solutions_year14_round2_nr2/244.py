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

long long d[100][2][2][2];

void solve(){
	int A,B,C;
    cin>>A>>B>>C;
    A--;
    B--;
    C--;

    vector<int> a,b,c;
    while(A||B||C){
        a.push_back(A&1);
        b.push_back(B&1);
        c.push_back(C&1);

        A>>=1;
        B>>=1;
        C>>=1;
    }

    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    reverse(c.begin(),c.end());

    FILL(d,0);

    d[0][0][0][0]=1;

    for (int i=0; i<a.size(); i++){
        for (int j=0; j<2; j++){
            for (int k=0; k<2; k++){
                for (int g=0; g<2; g++){


                    int J,K,G;
                    bool ok;

                    ///////////00
                    J=j;
                    G=g;
                    K=k;

                    if (a[i]==1) J=1;
                    if (b[i]==1) K=1;
                    if (c[i]==1) G=1;
                    
                    d[i+1][J][K][G] += d[i][j][k][g];

                    ///////////10
                    J=j;
                    G=g;
                    K=k;
                    ok=true;

                    if (j==0 && a[i]==0) ok=false;
                    if (b[i]==1) K=1;
                    if (c[i]==1) G=1;
                    
                    if (ok){
                        d[i+1][J][K][G] += d[i][j][k][g];
                    }

                    ///////////01
                    J=j;
                    G=g;
                    K=k;
                    ok=true;

                    if (a[i]==1) J=1;
                    if (k==0 && b[i]==0) ok=false;
                    if (c[i]==1) G=1;
                    
                    if (ok){
                        d[i+1][J][K][G] += d[i][j][k][g];
                    }


                    ///////////11

                    J=j;
                    G=g;
                    K=k;

                    if (j==0 && a[i]==0) continue;
                    if (k==0 && b[i]==0) continue;
                    if (g==0 && c[i]==0) continue;

                    d[i+1][J][K][G] += d[i][j][k][g];

                }
            }
        }
    }

    long long res=0;
    for (int j=0; j<2; j++){
        for (int k=0; k<2; k++){
            for (int g=0; g<2; g++){
                res+=d[a.size()][j][k][g];
            }
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