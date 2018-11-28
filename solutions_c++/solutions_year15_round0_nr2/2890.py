#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include<math.h>
#include <vector> 

int T;
int D;
int Px[1000];

int solve(int num){
	std::vector<int> data;
	int tnum,tnum2;
	for(int j=0;j<D;j++){
		tnum=Px[j];
		for(int k=1;k<33;k++){
			tnum2=(tnum+(k-1))/k;
			data.push_back(tnum2);
			if(tnum2<=2){
				break;
			}
		}
	}
	std::sort(data.begin(),data.end(),std::greater<int>());
	for (int i=0; i<data.size(); i++){
       data[i]=data[i]+i;
    }
	std::sort(data.begin(),data.end());
	 printf("Case #%d: %d\n",num,data[0]);
	return 0;
}

int main(){
	std::cin >> T;
	for(int i=0;i<T;i++){
		std::cin >> D;
		for(int j=0;j<D;j++){
			std::cin >> Px[j];
		}
		solve(i+1);
	}
	return 0;
}