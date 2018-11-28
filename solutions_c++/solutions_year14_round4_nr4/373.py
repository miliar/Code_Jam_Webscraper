#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <memory.h>

using namespace std;

int n,m,an1,an2;
string s[10];

struct Node{
	int next[27];
};
vector<Node> a[10];
Node init;

void proc(int v){
	if(v==m){
		int now=0;
		for(int i=0;i<n;i++)
			if(a[i].size()!=1)
				now+=a[i].size();
		if(an1<now) an1=now,an2=1;
		else if(an1==now) an2++;
		return;
	}
	for(int i=0;i<n;i++){
		int no=0,p=0,po=-1,op=0;
		for(int j=0;j<s[v].size();j++){
			if(a[i][no].next[s[v][j]-'A']==0){
				a[i][no].next[s[v][j]-'A']=a[i].size();
				a[i].push_back(init);
				op++;
				if(po==-1) po=no,p=s[v][j]-'A';
			}
			no=a[i][no].next[s[v][j]-'A'];
		}
		proc(v+1);
		for(int j=0;j<op;j++) a[i].pop_back();
		if(po!=-1)
			a[i][po].next[p]=0;
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ca=0;
	scanf("%d",&t);
	for(int i=0;i<26;i++) init.next[i]=0;
	while(t--){
		an1=an2=0;
		scanf("%d %d",&m,&n);
		for(int i=0;i<10;i++){
			a[i].clear();
			a[i].push_back(init);
		}
		for(int i=0;i<m;i++) s[i].clear(),cin>>s[i];
		proc(0);
		printf("Case #%d: %d %d\n",++ca,an1,an2);
	}
	return 0;
}