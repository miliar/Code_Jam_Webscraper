#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
 
using namespace std;

int main(){
	int T;
	string ans;
	
	cin>>T;
	for(int t=1; t<=T; t++){
		ans="GABRIEL";
		int X,R,C;
		int limit;
		cin>>X>>R>>C;
		if(R*C%X!=0)
			ans="RICHARD";
		else if(X==1)
			ans="GABRIEL";
		else{
			if(X==2)
				ans="GABRIEL";
			else if(X>R && X>C)
				ans="RICHARD";
			else if(X==3 && (R==1 || C==1))
				ans="RICHARD";
			else if (X==4 && (R==1 || C==1))
				ans="RICHARD";
			else if (X==4 && (R==2 || C==2))
				ans="RICHARD";
		}
		//output case
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}