#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main(int argc, char *argv[]) {
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int cases;
	cin>>cases;
	int ccase=1;
	while(ccase<=cases){
		char str[150]; 
		cin>>str;
		int i=1;
		int flips=1;
		char prev=str[0];
		
		while(i<strlen(str)){
			
			if(prev!=str[i])
				flips++;
			prev=str[i];
			i++;
		}
		
		
		if(str[strlen(str)-1]=='+')
			flips--;
		
		cout<<"Case #"<<ccase<<": "<<flips<<"\n";
		
		ccase++;
	}
	return 0;
}

