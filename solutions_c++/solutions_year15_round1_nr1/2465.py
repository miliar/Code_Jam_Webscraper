#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include<math.h>

int T;
int N;
int m[10001];

int solve(int num){
	int ans1=0,ans2=0;
	int tmpn=m[N-2]-m[N-1];
	for(int j=0;j+1<N;j++){
		if(m[j]-m[j+1]>tmpn){
			tmpn=m[j]-m[j+1];
		}
	}
	//printf("tmpn=%d\n",tmpn);
	for(int j=0;j<N;j++){
		if(m[j+1]<m[j] && (j+1)<N ){
			ans1=ans1+(m[j]-m[j+1]);
		}
		if(j<N-1&&tmpn>0){
		if(m[j]<tmpn){
			ans2=ans2+m[j];
		}else {
			ans2=ans2+tmpn;
		}
		}
	}

	printf("Case #%d: %d %d\n",num,ans1,ans2);
	return 0;
}

int main(){
	std::cin >> T;
	for(int i=0;i<T;i++){
		std::cin >> N;
		for(int j=0;j<N;j++){
			std::cin >> m[j];
		}
		solve(i+1);
	}
	//std::cin >> m[1];
	return 0;
}