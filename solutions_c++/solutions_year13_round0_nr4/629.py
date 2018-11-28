#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define X first 
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define D 1000000007
#define Max (1<<30)
#define LLMAX (1ll<<60)
#define mp make_pair
#define MM 1000000000000000000ll
#define pss pair<string,string>
#define psi pair<string,int>
#define NN 3
#define vi vector<int>


int d[1<<20];
int n,m;
int now[222];
int box[222];
int key[222][222];
int all;


bool go(int st){
	
	if(st==all)return 1;
	if(d[st]!=-1){
		if(d[st]==-2)return 0;
		return 1;
	}
	d[st]=-2;
	for(int i=0;i<n;i++)if((st>>i&1)==0 && now[box[i]]){

		now[box[i]]--;
		for(int k=1;k<=200;k++)now[k]+=key[i][k];

		int nxt= st | (1<<i);
		bool r=go(nxt);

		for(int k=1;k<=200;k++)now[k]-=key[i][k];
		now[box[i]]++;

		if(r){	
			d[nxt]=i;
			return 1;
		}
	}
	return 0;
}

void print(int st){
	if(st){
		print(st- (1<<d[st]));
		cout<<" "<<d[st]+1;
	}
}
int main(){
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	
	int t;
	cin>>t;
	int CC=0;

	while(t--){

		memset(d,-1,sizeof(d));
		memset(now,0,sizeof(now));
		memset(box,0,sizeof(box));
		memset(key,0,sizeof(key));


		CC++;
		cin>>m>>n;
		all=(1<<n)-1;
		for(int i=1;i<=m;i++){
			int t;cin>>t;
			now[t]++;
		}

		for(int i=0;i<n;i++){
			cin>>box[i];
			int t;cin>>t;
			while(t--){
				int k;cin>>k;
				key[i][k]++;
			}
		}


		bool rst=go(0);


		printf("Case #%d:",CC);
		if(rst){
			print(all);
		}
		else cout<<" IMPOSSIBLE";

		cout<<endl;
	}
	

}