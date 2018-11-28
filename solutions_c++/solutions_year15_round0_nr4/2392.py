#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	freopen("D-small-practice.in","r",stdin);
    freopen("D-small-practice.out","w",stdout);

	int cnt = 0;
	int T;
	cin>>T;
	int X,R,C;
	
	while(T--){
		cin>>X>>R>>C;
		string res;
		if(X==1)
			res = "GABRIEL";
		else if(X==2){
			if((R&0x01)&&(C&0x01))
				res = "RICHARD";
			else
				res = "GABRIEL";
		}
		else if(X==3){
			if((R%3==0&&C>=2)||(C%3==0&&R>=2))
				res = "GABRIEL";
			else
				res = "RICHARD";
		}
		else if(X==4){
			if((R%4==0&&C>=3)||(C%4==0&&R>=3))
				res = "GABRIEL";
			else
				res = "RICHARD";
		}
		else if(X==5){
			if((R%5==0&&C>=4)||(C%5==0&&R>=4))
				res = "GABRIEL";
			else
				res = "RICHARD";
		}
		else if(X==6){
			if((R%6==0&&C>=5)||(C%6==0&&R>=5))
				res = "GABRIEL";
			else
				res = "RICHARD";
		}
		else if(X>=7){
			res = "RICHARD";
		}

				
		cout<<"Case #"<<++cnt<<": ";
		cout<<res<<endl;
	}
	
	return 0;
}