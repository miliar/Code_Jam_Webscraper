#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include<math.h>
#include <complex>

int T;
int R;
int C;
int W;
int B[20][20];


int solve(int num){
	int ans=0,tR=0,tC=0;
	if(W==1){ans=R*C;}
	else while(1){
		if(tC+W-1<C){
			ans=ans+1;
			tC=tC+W;
		}
		else if(tR<R){tR++;}
		else {
			if(tC<C){ans++;}
			ans=ans+W-1;break;
		}
	}
	printf("Case #%d: %d\n",num,ans);
	return 0;
}

int main(){
	std::cin >> T;
	for(int i=0;i<T;i++){
		std::cin >> R >> C >> W;
		solve(i+1);
	}
	
	return 0;
}