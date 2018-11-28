#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int T;
	char pan[200];
	int len;
	char prior;
	int count;
	

	cin>>T;
	for(int casenum=1; casenum<=T; casenum++){
		cin>>pan;
		len=strlen(pan);

		prior=pan[0];
		count=0;
		for(int i=1; i<len; i++){
			if(pan[i]!=prior){
				prior=pan[i];
				count++;
			}
		}
		if(pan[len-1]=='-'){
			count++;
		}

		cout<<"Case #"<<casenum<<": "<<count<<endl;

	}
	return 0;
}
