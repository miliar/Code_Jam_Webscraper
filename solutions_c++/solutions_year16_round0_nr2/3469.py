#include <iostream>
#include <string.h>
using namespace std;

int T;
char str[150];
int pan[150];

int main(){
	
	cin >> T;
	
	for(int i=1; i<=T; i++){
		cin >> str;
		int len = strlen(str);
		for (int j=0;j<len; j++){
			if(str[j]=='+') pan[j]=0;
			if(str[j]=='-') pan[j]=1;
		}
		int flip = 0;
		for(int j=len-1; j>=0; j--){
			//If need to flip and it has not been flipped to the right side yet or it has been flipped to the wrong side
			if ((pan[j]==1&&flip%2==0) || (pan[j]==0&&flip%2==1)) flip++;
		}
		
		cout << "Case #" << i << ": " << flip << "\n";
	}
	
}
