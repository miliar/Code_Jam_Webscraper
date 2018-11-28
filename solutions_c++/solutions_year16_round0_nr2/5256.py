
#include <cstdio>
#include <iostream>

using namespace std;

int getMinimalSwap(string x ){
	int len = x.size();
	int swap = 0;
	while(len!= 0){
		bool swapDone = false;
		for (int i = len-1; i >=0 ; --i){
			if(x[i]== '-'){
				swapDone = true;
				swap ++;
				len = i ; 
				for (int j = 0; j <= len; ++j){
					if(x[j]=='+'){
						x[j]='-';
					}else {
						x[j]='+';
					}
				}
				break;
			}
		}
		if(!swapDone){
			break;
		}
	}
	return swap;
}
int main(){
	 // freopen("b.in","r",stdin);
	 // freopen("B-large.out","w",stdout);
	string x;
	int n;
	cin >> n; 
	for (int i = 1; i <= n; ++i){
		cin >> x;
		int y = getMinimalSwap(x);
		printf("Case #%d: %d\n", i,y);	
	}
	return 0; 
}