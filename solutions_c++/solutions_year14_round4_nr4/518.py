#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))
#define ll long long

#define BASE (1000000007)

map<string, bool> mb[5];
typedef map<string,bool>::iterator it_type;

int T,N,M;
char s[10][15];

int a[10];
int ans,cc;

void calc(){
	FOR(i,0,M) mb[i].clear();

	FOR(i,0,N){
		int tar = a[i], len = strlen(s[i]);
		FOE(j,0,len){
			string tmp; tmp.assign(s[i],s[i]+j);
			//cout<<"str: "<<tmp<<endl;
			mb[tar][tmp] = 1;
		}
	}

	int tp=0;
	FOR(i,0,M){
		tp += mb[i].size();
	}
	if (tp > ans){
		ans = tp;
		cc = 1;
	}
	else if (tp == ans){
		cc = (cc+1)%BASE;
		/*
		if (ans == 10){
			FOR(i,0,N) printf("%d ",a[i]);
			puts("");

			FOR(i,0,M){
				printf("%d!!\n",i);
				for(it_type iterator = mb[i].begin(); iterator != mb[i].end(); iterator++) {
					cout <<"str: "<<iterator->first<<endl;
					// iterator->first = key
					// iterator->second = value
					// Repeat if you also want to iterate through the second map.
				}
			}
		}
		*/
	}
}

void f(int pos){
	if (pos >= N){
		calc();
	}
	else{
		FOR(i,0,M){
			a[pos] = i;
			f(pos+1);
		}
	}
}

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		scanf("%d%d",&N,&M); gets(s[0]);
		FOR(i,0,N) gets(s[i]);

		ans = -1;
		cc = 0;
		f(0);

		printf("Case #%d: %d %d\n",t,ans,cc);
	}
	return 0;
}
