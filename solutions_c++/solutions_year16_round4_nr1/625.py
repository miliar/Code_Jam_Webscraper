#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<string>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define VB vector<bool>
#define VI vector<int>
#define VLL vector<LL>
#define VPI vector<PI>
#define PB push_back
#define VVI vector<VI>
#define QI pair<PI,PI>
#define PIS pair<int,string>
#define MAXN 12

int N, R, P, S;
map<QI,PIS> mymap;

void printVector(VI v){
	int sz = v.size();
	for(int i=0;i<sz;i++)
		printf("%d", v[i]);
	printf("\n");
}

int play(int a,int b){
	if(a+b == 1)
		return 0;
	if(a+b == 3)
		return 1;
	if(a+b == 2)
		return 2;
}

string best(string a,string b){
	if(a.compare(b) < 0)
		return a+b;
	else
		return b+a;
}

void preprocess(){
	mymap[MP(MP(1,1),MP(1,0))] = MP(0,"PR");
	mymap[MP(MP(1,1),MP(0,1))] = MP(2,"PS");
	mymap[MP(MP(1,0),MP(1,1))] = MP(1,"RS");

	for(int l=2;l<=MAXN;l++){
		vector<pair<QI,PIS> > v;
		for(map<QI,PIS>::iterator it = mymap.begin();it != mymap.end(); it++){
			if((*it).F.F.F == l-1){
				v.PB(*it);
			}
		}
		int a,b;
		a = 0; b = 1;
		mymap[MP(MP(l,v[a].F.F.S+v[b].F.F.S),MP(v[a].F.S.F+v[b].F.S.F,v[a].F.S.S+v[b].F.S.S))] = MP(play(v[a].S.F,v[b].S.F),best(v[a].S.S,v[b].S.S));
		a = 0; b = 2;
		mymap[MP(MP(l,v[a].F.F.S+v[b].F.F.S),MP(v[a].F.S.F+v[b].F.S.F,v[a].F.S.S+v[b].F.S.S))] = MP(play(v[a].S.F,v[b].S.F),best(v[a].S.S,v[b].S.S));
		a = 1; b = 2;
		mymap[MP(MP(l,v[a].F.F.S+v[b].F.F.S),MP(v[a].F.S.F+v[b].F.S.F,v[a].F.S.S+v[b].F.S.S))] = MP(play(v[a].S.F,v[b].S.F),best(v[a].S.S,v[b].S.S));
	}
}

int main()
{
	freopen("A_input2.txt", "r", stdin);
	freopen("A_output2L.txt", "w", stdout);
	preprocess();

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		scanf("%d %d %d %d", &N, &R, &P, &S);
		if(mymap.find(MP(MP(N,P),MP(R,S))) != mymap.end()){
			cout<<"Case #"<<casenum<<": "<<mymap[MP(MP(N,P),MP(R,S))].S<<endl;
		}
		else{
			cout<<"Case #"<<casenum<<": IMPOSSIBLE"<<endl;
		}
	}

	return 0;
}
