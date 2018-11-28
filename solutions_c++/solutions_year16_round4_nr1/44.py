#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <fstream>
using namespace std;

#define lowbit(x) ((x)&(-(x)))
#define sqr(x) ((x)*(x))
#define PB push_back
#define MP make_pair

map<pair<int,int>,pair<pair<int,int>,int> > res[13][3];

int win(int a,int b){
	if (a>b) return win(b,a);
	if (a==0&&b==2) return 0;
	return b;
}

void init(){
	for (int i=0;i<13;i++)
		for (int j=0;j<3;j++)
			res[i][j].clear();
	res[0][0][MP(1,0)]=MP(MP(0,0),0);
	res[0][1][MP(0,1)]=MP(MP(0,0),0);
	res[0][2][MP(0,0)]=MP(MP(0,0),0);
	for (int n=0;n<12;n++){
		vector<pair<pair<int,int>,int> > cur;
		cur.clear();
		for (int k=0;k<3;k++)
			for (map<pair<int,int>,pair<pair<int,int>,int> >::iterator itr=res[n][k].begin();itr!=res[n][k].end();itr++){
				cur.PB(MP(itr->first,k));
			}
		for (int i=0;i<cur.size();i++)
			for (int j=i+1;j<cur.size();j++)
				if (cur[i].second!=cur[j].second){
					res[n+1][win(cur[i].second,cur[j].second)][MP(cur[i].first.first+cur[j].first.first,cur[i].first.second+cur[j].first.second)]=
					cur[i];
				}
	}
}

int lost(int i,int j){
	if (i==j) return (i+2)%3;
	else return i;
}

string getans(int n,int a,int b,int i){
	if (n==0) {
		if (i==0) return "R";
		if (i==1) return "P";
		if (i==2) return "S";
	}
	pair<pair<int,int>,int> le=res[n][i][MP(a,b)];
	string ta=getans(n-1,le.first.first,le.first.second,le.second);
	string tb=getans(n-1,a-le.first.first,b-le.first.second,lost(i,le.second));
	return min(ta,tb)+max(ta,tb);
}

string getans(){
	int n,a,b,c;
	scanf("%d%d%d%d",&n,&a,&b,&c);
	if (a+b+c!=(1<<n)) return "IMPOSSIBLE";
	for (int i=0;i<3;i++)
		if (res[n][i].find(MP(a,b))!=res[n][i].end())
			return getans(n,a,b,i);
	return "IMPOSSIBLE";
}

int main(int argc,char ** argv){
	int T;
	scanf("%d",&T);
	init();
	for (int t=1;t<=T;t++){
		printf("Case #%d: %s\n",t,getans().c_str());
	}
	return 0;
}