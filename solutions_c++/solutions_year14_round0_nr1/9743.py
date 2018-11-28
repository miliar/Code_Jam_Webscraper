#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

#define REP(i,n) for(i=0 ; i<n ; i++)
#define rep(i,x,n) for(i=x ; i<n ; i++)
#define All(i) i.begin(),i.end()

typedef vector<int> V;
typedef map<int, int> M;
typedef set<int> S;

int main() {
	int r,i,j,t,v,a1[4][4],a2[4][4],e[2][4],c=0,ii;
	cin>>t;
	REP(r,t){
		cin>>v;
		REP(i,4)
			REP(j,4)
			cin>>a1[i][j];
		REP(i,4)e[0][i]=a1[v-1][i];
		cin>>v;
		REP(i,4)
			REP(j,4)
			cin>>a2[i][j];
		REP(i,4)e[1][i]=a2[v-1][i];
		REP(i,4){
			REP(j,4){
				if (e[0][i]==e[1][j])
					c++,ii=e[0][i];
			}
		}
		cout<<"Case #"<<r+1<<": ";
		if(c==0)cout<<"Volunteer cheated!"<<endl;
		else if (c==1)cout<<ii<<endl;
		else cout<<"Bad magician!"<<endl;
		c=0;
	}
}



