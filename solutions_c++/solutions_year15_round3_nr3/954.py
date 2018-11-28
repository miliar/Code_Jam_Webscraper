/*
ID: xiaoche4
PROG: skidesign
LANG: C++
*/
//#include "TC.cpp"
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <utility>
#include <algorithm>
using namespace std;

int T,C,D,V;
int d[5]; bool v[31];
bool n[17]; int ans;
void dfs(int l){
	if(l==17){
		bool t[31];
		for(int i=0;i<=V;i++)
			t[i]=v[i];
		for(int i=1;i<17;i++){
			if(n[i]){
				for(int j=V;j>=i;j--){
					if(t[j-i])
						t[j]=true;
				}
			}
		}
		bool has=true;
		for(int i=0;i<=V;i++){
			if(!t[i])
				has=false;
		}
		if(has){
			int cnt=0;
			for(int i=1;i<17;i++){
				if(n[i])
					cnt++;
			}
			ans=min(ans,cnt);
		}
		return;
	}
	dfs(l+1);
	for(int i=0;i<D;i++){
		if(d[i]==l)
			return;
	}
	n[l]=true;
	dfs(l+1);
	n[l]=false;
}
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("Ans.out","w",stdout);
	//ifstream fin("dict.out");
	//ofstream fout("Ans.out");
	//FILE *fin=fopen("table.txt","r");
	//FILE *fout=fopen("Ans.out","w");
	cin>>T;
	for(int k=1;k<=T;k++){
		cin>>C>>D>>V;
		for(int i=0;i<D;i++)
			cin>>d[i];
		v[0]=true;
		for(int i=0;i<D;i++){
			for(int j=V;j>=d[i];j--){
				if(v[j-d[i]])
					v[j]=true;
			}
		}
		ans=20; dfs(1);
		printf("Case #%d: %d\n",k,ans);
		memset(v,0,sizeof(v));
	}

	return 0;
}