#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>
#include <unordered_map>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

int n;

//typedef map<int,int> keytype;
typedef VI keytype;

struct csucs{
	int ss;
	keytype keys;
	csucs(int ss):ss(ss),keys(keytype(201)){}
	csucs(int ss, keytype &keys):ss(ss),keys(keys){}
};


int main(){
	/*cout<<(LL)sqrt(16)<<endl;
	system("PAUSE");*/

	ifstream be("D-small-attempt1.in");
	ofstream ki("ki.txt");
	int T; be>>T;
	FOR(tt,T){
		int k; be>>k>>n;
		csucs start(0);
		FOR(i,k){
			int x; be>>x;
			start.keys[x]++;
		}
		VI ot(n);
		VVI chests(n);
		FOR(i,n){
			int x, y; be>>x>>y;
			ot[i]=x;
			chests[i]=VI(y);
			FOR(j,y)
				be>>chests[i][j];
		}

		vector<bool> volt(1<<n);
		volt[start.ss]=true;
		queue<csucs> q;
		q.push(start);
		vector<int> hon(1<<n);
		while(!q.empty()){
			csucs u=q.front(); q.pop();
			FOR(i,n){
				int vss=u.ss | (1<<i);
				if(!(u.ss & (1<<i)) && !volt[vss] && u.keys[ot[i]]){
					csucs v(vss, u.keys);
					v.keys[ot[i]]--;
					FOR(j,SZ(chests[i]))
						v.keys[chests[i][j]]++;

					q.push(v);
					volt[v.ss]=true;
					hon[v.ss]=i;
				}
			}
		}

		int end=(1<<n)-1;
		if(!volt[end])
			ki<<"Case #"<<tt+1<<": "<<"IMPOSSIBLE"<<endl;
		else{
			int akt=end;
			VI kit;
			while(akt!=0){
				kit.PB(hon[akt]);
				akt=akt^(1<<hon[akt]);
			}
			reverse(ALL(kit));
			ki<<"Case #"<<tt+1<<":";
			FOR(i,n)
				ki<<" "<<kit[i]+1;
			ki<<endl;
		}
	}
	
	ki.close();
	return 0;
}