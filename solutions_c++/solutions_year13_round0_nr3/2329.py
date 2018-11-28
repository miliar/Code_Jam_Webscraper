#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

long long palSquare[1000];
long long counter;

void calPalSquares(long long limit){
	long long iRoot,iNum,temp,i;
	double sqRoot;
	for(i=1;i<=limit;i++){
		temp = i;
		iNum = 0;
		while(temp != 0){
			iNum = iNum*10 + temp%10;
			temp/=10;
		}
		if(iNum==i){
				temp = i*i;
				iRoot = 0;
				while(temp != 0){
					iRoot = iRoot*10 + temp%10;
					temp/=10;
				}
				if(iRoot==i*i){
					palSquare[counter++]=i*i;
				}
		}
	}
}

int main(){
	long long t,kase=1,a,b,i,j;
	//int palSquare[5] = {1, 4, 9, 121, 484};
	counter = 0;
	calPalSquares(10000010LL);
	//calPalSquares(1010LL);
	scanf("%lld",&t);
	while(t--){
		scanf("%lld %lld",&a,&b);
		for(i=0;i<counter;i++){
			if(a<=palSquare[i])
				break;
		}
		for(j=0;j<counter;j++){
			if(b<palSquare[j])
				break;
		}
		printf("Case #%lld: %lld\n", kase++, j-i);
	}
	return 0;
}

