/*
Sourav Bhattacharjee
IIT Kharagpur

GO
*/
#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int getins(string str);

int getplus(string inp){
	int len=inp.length();
	if(len==1){
		if(inp[len-1]=='+')
			return 1;
		else
            return 0;

	}
	else{
		if(inp[len-1]=='+')
			return (1+getins(inp.substr(0,len-1)));
		else
			return (getplus(inp.substr(0,len-1)));

	}
}



int getins(string str){
	int len;

	len=str.length();
	if(len==1){
		if(str[len-1]=='-'){
			return 1;
		}
		else{
			return 0;
		}
	}
	else{
		if(str[len-1]=='-'){
			return (1+getplus(str.substr(0,len-1)));
		}
		else{
			return (getins(str.substr(0,len-1)));
		}
	}
}






int main()
{

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

    int TestCase;
	cin >> TestCase;

	for(int i=1;i<=TestCase;i++)
	{
	        string str;
	        cin >> str;
	      	cout << "Case #" << i << ": "<< getins(str) << endl;

	}



    return 0;
}
