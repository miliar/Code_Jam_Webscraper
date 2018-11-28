#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("input_dsmall.in", "r", stdin);
	freopen("output_dsmall.txt", "w", stdout);
	int t;
	cin>>t;
	
	for(int a =1; a<=t; a++){
		int x,r,c;
		char ans='r';
		cin>>x>>r>>c;
		if(x==1){
			ans='g';
		}
		else if (x==2){
			if((r*c)<x )ans='r'; // 1x1 handled 
			else if((r*c)%2==0)ans='g';
			else ans = 'r';
		}
		else if (x==3){
			
			if((r*c)<x || r==1 || c==1 )ans='r';
			else if((r%2==0)&&(c%2==0))ans='r';
			else ans = 'g';
		}
		else if(x==4){
			if(((r*c)<=x )|| ((r*c)%4!=0))ans='r';
			else if( (r*c)==8)ans='r';
			else if ((r*c)==12){
				ans='g';
			}
			else if ((r*c)==16){
				ans='g';
			}
			
		}
		if(ans=='g')cout<<"Case #"<<a<<": GABRIEL"<<endl;
		else if(ans=='r') cout<<"Case #"<<a<<": RICHARD"<<endl;
	}
}
