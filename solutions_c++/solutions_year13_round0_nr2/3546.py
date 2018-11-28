#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>

using namespace std;

#define MAXN 109

int Map[MAXN][MAXN],N,M;

void Read() {
	scanf("%d %d",&N,&M);
	
	for (int i=1;i<=N;i++) {
		for (int j=1;j<=M;j++) {
			scanf("%d",&Map[i][j]);
		}
	}
}

inline bool Right(int i,int j) {
	int num=Map[i][j],p1=j+1;
	
	while (p1<=M) {
		if (num<Map[i][p1])
			return true;
		p1++;
	}
	return false;
}

inline bool Left(int i,int j) {
	int num=Map[i][j],p1=j-1;
	
	while (p1>=1) {
		if (num<Map[i][p1])
			return true;
		p1--;
	}
	return false;
}

inline bool Down(int i,int j) {
	int num=Map[i][j],p1=i+1;
	
	while (p1<=N) {
		if (num<Map[p1][j])
			return true;
		p1++;
	}
	return false;
}

inline bool Up(int i,int j) {
	int num=Map[i][j],p1=i-1;
	
	while (p1>=1) {
		if (num<Map[p1][j])
			return true;
		p1--;
	}
	return false;
}

void Solve(int kase) {
	bool ok=true;
	for (int i=1;i<=N;i++) {
		for (int j=1;j<=M;j++) {
			if ((Right(i,j)&&Up(i,j))||(Down(i,j)&&Right(i,j))||(Left(i,j)&&Down(i,j))||(Up(i,j)&&Left(i,j)))  {
				ok=false;
				break;
			}
		}
	}
	
	if (ok)
		printf("Case #%d: YES\n",kase);
	else 
		printf("Case #%d: NO\n",kase);
}

void Init() {
	memset(Map,0,sizeof Map);
}

int main () {
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	int t;
	scanf("%d",&t);
	
	for (int i=1;i<=t;i++) {
		Read();
		Solve(i);
		Init();
	}
	
	return 0;
}
