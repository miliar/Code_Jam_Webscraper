#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include<math.h>

int T;
int Smax;
std::string s;

int solve(int num){
	char s2=s[0];
	int sa=(int)(s2 - '0');
	int ans=0;
	for(int i=0;i<Smax;i++){
		if( (i+1)<=sa){
			if(i!=Smax){
			sa=sa+(int)(s[i+1] - '0');
			}
		}
		else{
			ans=ans+(i+1-sa);
			sa=sa+(i+1-sa);
			sa=sa+(int)(s[i+1] - '0');
		}
	}
	printf("Case #%d: %d\n",num,ans);
	return 0;
}

int main(){
	std::cin >> T;
	for(int i=0;i<T;i++){
		std::cin >> Smax >> s;
		solve(i+1);
	}
	return 0;
}