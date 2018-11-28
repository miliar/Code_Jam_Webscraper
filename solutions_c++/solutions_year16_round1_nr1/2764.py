#include <iostream>
#include <string.h>
using namespace std;

int main(){
	long long testCase;
	cin>>testCase;
	for(long long q=0;q<testCase;q++){
		char str[1001],final[1001];
		cin>>str;
		final[0] = str[0];
		int len = 1;
		cout<<"Case #"<<q+1<<": ";
		for(int i=1;i<strlen(str);i++){
			if((int)str[i]>=(int)final[0]){
				for(int j=len-1;j>=0;j--){
					final[j+1] = final[j];
				}
				final[0] = str[i];
				len++;
			}
			else{
				final[len] = str[i];
				len++;
			}
		}
		final[len] = str[len];
		cout<<final<<"\n";
	}
	return 0;
}