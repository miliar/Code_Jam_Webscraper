#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
	int times=0,k=1;
	cin >> times;
	while(times--){
		int total=0;
		cin >> total;
		int mush[1050];
		memset(mush,0,sizeof(mush));
		for(int a=0;a<total;a++){
			cin >> mush[a];
		}
		int ans1=0,ans2=0;
		for(int a=1;a<total;a++){
			if(mush[a]<mush[a-1]){
				ans1=ans1+mush[a-1]-mush[a];
			}
		}
		int maxx=0;
		for(int a=1;a<total;a++){
			maxx=max(maxx,(mush[a-1]-mush[a]));
		}
		for(int a=0;a<total-1;a++){
			if(mush[a]>=maxx){
				ans2=ans2+maxx;
			}
			else{
				ans2=ans2+mush[a];
			}
		}
		printf("Case #%d: %d %d\n",k,ans1,ans2);
		k++;
	}
	return 0;
}
