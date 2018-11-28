#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

int T;
int M;
int N;
int map[10000];
int colmax[100];
int rowmax[100];

char *out;

void get(){
	scanf("%d %d",&N,&M);
	int target=0;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			scanf("%d",&map[target]);
			target++;
		}
	}
	return;
}

void solve(){
	for(int i=0;i<N;i++){
		int max=0;
		for(int j=0;j<M;j++){
			max=max>map[M*i+j]?max:map[M*i+j];
		}
		colmax[i]=max;
	}
	for(int i=0;i<M;i++){
		int max=0;
		for(int j=0;j<N;j++){
			max=max>map[i+M*j]?max:map[i+M*j];
		}
		rowmax[i]=max;
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if(map[i*M+j] < colmax[i] && map[i*M+j] < rowmax[j]){
				out="NO";
				return;
			}
		}
	}
	out="YES";
	return;
}

int main(int argc,char **argv){
	scanf("%d\n",&T);
	for(int i=0;i<T;i++){
		get();
		solve();
		printf("Case #%d: %s\n",i+1,out);
	}
}
