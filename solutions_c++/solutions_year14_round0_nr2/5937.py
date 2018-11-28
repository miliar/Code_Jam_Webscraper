#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

void solve(int c)
{
	double C,F,X;
	cin>>C>>F>>X;
	int f = 0;
	double lastTry = X/2;
	double curTry = 0;	
	do{
		f++;
		curTry = 0;
		for(int i=0;i<f;i++){
			curTry += C/(2+F*i);
		}
		curTry += X/(2+F*f);
		if(curTry>lastTry)
			break;
		else
			lastTry=curTry;
	}while(true);
	
	printf("Case #%d: %.7f\n",c,lastTry);
}

int main(int argc, char** args)
{
	int T;
	cin>>T;
	int c=0;
	while((++c)<=T){
		solve(c);
	}
}
