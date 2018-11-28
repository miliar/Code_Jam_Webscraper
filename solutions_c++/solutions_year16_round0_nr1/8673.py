#include <iostream>
#include <cstdio>
using namespace std;

bool check(int digits[]){
	for (int i=0;i<10;i++){
		if (digits[i]==0) return false;
	}
	return true;
}

int main(){
	int tc;
	scanf("%d",&tc);
	for (int i=1;i<=tc;i++){
		int N;
		scanf("%d",&N);
		if (N==0) {printf("Case #%d: INSOMNIA \n",i);}
		else{
			int digits[10],mp;
			for (int x=0;x<10;x++) digits[x]=0;
			for (mp=1;check(digits)==false;mp++){
				int tmp=N*mp;
				while (tmp!=0){
					digits[tmp%10]++;
					tmp/=10;
				}
			}
			printf("Case #%d: %d\n",i,N*(mp-1));
		}
	}
	cin.get();
	cin.ignore();
}