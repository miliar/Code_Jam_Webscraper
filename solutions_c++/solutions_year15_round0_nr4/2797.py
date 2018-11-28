#include <iostream>
#include <string>
#include <stdio.h>
#include<cmath>
#include<set>
using namespace std;

#define loop(n) for(int i=0;i<n;i++)

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,X,R,C;
	cin>>T;
	bool passed = false;
	loop(T) {
		cin>>X>>R>>C;
		passed = false;
		if(R*C%X ==0) 
		{
			if(X==1) 
			{
				passed = true;
			}
			else if(X==2) 
			{
				passed = true;
			}
			else if(X==3  && R*C!=3)
			{
				passed = true;
			}
			else if(X==4 && (R*C==12||R*C==16))
			{
				passed = true;
			}
		}
		if(passed)
			cout<<"Case #"<<(i+1)<<": GABRIEL"<<endl;
		else
			cout<<"Case #"<<(i+1)<<": RICHARD"<<endl;
	}
	// your code goes here
	return 0;
}