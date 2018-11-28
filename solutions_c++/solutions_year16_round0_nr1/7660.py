#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <set>
using namespace std;
int getValue(int Num){
	if(Num==0){
		return -1;
	}
	else{
		int ctr=1;
		int num=0,temp=0;
		set<int> numset;
		while(ctr<=100){
			num=Num*ctr;
			temp=num;
			while(temp>0){
				numset.insert(temp%10);
				temp=temp/10;
			}
			if(numset.size()==10){
				break;
			}
			ctr++;
		}
		return num;
	}
}
int main(){
	int T;
	int N;
	int result;
	scanf("%d",&T);	
	for(int i=1;i<=T;i++){
		scanf("%d",&N);
		result=getValue(N);
		if(result<0){
			printf("Case #%d: INSOMNIA\n",i );
		}
		else{
			printf("Case #%d: %d\n",i,result );
		}
	}
	return 0;
}
