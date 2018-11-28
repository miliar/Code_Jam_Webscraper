#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int makeMeNegative(string inp);
int makeMePositive(string inp){
	int len=inp.length();
	if(len==1){
		if(inp[len-1]=='-'){
			return 1;
		}else{
			return 0;
		}
	}else{
		if(inp[len-1]=='-'){
			return 1+makeMeNegative(inp.substr(0,len-1));
		}else{
			return makeMePositive(inp.substr(0,len-1));
		}	
	}
}

int makeMeNegative(string inp){
	int len=inp.length();
	if(len==1){
		if(inp[len-1]=='+'){
			return 1;
		}else{
			return 0;
		}
	}else{
		if(inp[len-1]=='+'){
			return 1+makeMePositive(inp.substr(0,len-1));
		}else{
			return makeMeNegative(inp.substr(0,len-1));
		}	
	}
}

int calculate(string inp){
	return makeMePositive(inp);
}


int main()
{

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

    	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
	        string str;
	        cin >> str;
	      	cout << "Case #" << i << ": "<< calculate(str) << endl;
		
	}



    return 0;
}
