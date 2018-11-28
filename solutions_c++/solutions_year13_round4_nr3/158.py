#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int A[2000], B[2000], X[2000], N;
char rel[2000][2000];

void eval(){
	memset(rel, 0, sizeof(rel));
	for(int i=0; i<N; i++){
		bool has=false;
		for(int j=i-1; j>=0; j--){
			if(A[j]>=A[i]){
				rel[j][i]=1;
			}else if(!has){
				rel[i][j]=1;
			}
			if(A[j]==A[i]-1)
				has=true;
		}
		has=false;
		for(int j=i+1; j<N; j++){
			if(B[j]>=B[i]){
				rel[j][i]=1;
			}else if(!has){
				rel[i][j]=1;
			}
			if(B[j]==B[i]-1)
				has=true;
		}
	}
	for(int k=0; k<N; k++)
	for(int i=0; i<N; i++)
	for(int j=0; j<N; j++){
		if(rel[i][k] && rel[k][j]){
			rel[i][j]=1;
		}
	}
	bool used[2001]={};
	for(int i=0; i<N; i++){
		assert(rel[i][i]==0);
		int count=0;
		for(int j=i; j<N; j++)
			if(rel[i][j]==1)
				count++;
		int a=1;
		while(true){
			if(used[a])
				a++;
			else if(count){
				count--;
				a++;
			}else
				break;
		}
		used[a]=true;
		X[i]=a;
		printf(" %d", X[i]);
	}
	putchar('\n');
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		scanf("%d", &N);
		for(int j=0; j<N; j++)
			scanf("%d", A+j);
		for(int j=0; j<N; j++)
			scanf("%d", B+j);
		cout<<"Case #"<<i<<":";
		eval();
	}
	return 0;
}
