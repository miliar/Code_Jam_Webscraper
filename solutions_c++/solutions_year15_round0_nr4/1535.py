#include<bits/stdc++.h>
using namespace std;
int main(){
	int i,sum,smax,t,ans,count,x,r,c;
	char s[10000];
	
	#ifndef ONLINE_JUDGE
		freopen("inp","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	cin>>t;
	count=1;
	while(t--){
		cout<<"Case #"<<count<<": ";
		cin>>x>>r>>c;
		if(x==1){
			cout<<"GABRIEL"<<endl;
		}
		else if(x==2){
			if((r*c)%2==0){
				cout<<"GABRIEL"<<endl;
			}
			else{
				cout<<"RICHARD"<<endl;
			}
		}
		else if(x==3){
			if(r==1||c==1) cout<<"RICHARD"<<endl;
			else if((r*c)%3==0) cout<<"GABRIEL"<<endl;
			else cout<<"RICHARD"<<endl;
		}
		else if(x==4){
			if(r<3||c<3) cout<<"RICHARD"<<endl;
			else if((r*c)%4==0) cout<<"GABRIEL"<<endl;
			else cout<<"RICHARD"<<endl;
		}
		else if(x==5){
			if(r<4||c<4) cout<<"RICHARD"<<endl;
			else if((r*c)%5==0) cout<<"GABRIEL"<<endl;
			else cout<<"RICHARD"<<endl;
		}
		else if(x==6){
			if(r<4||c<4) cout<<"RICHARD"<<endl;
			else if((r*c)%6==0) cout<<"GABRIEL"<<endl;
			else cout<<"RICHARD"<<endl;
		}
		else{
			cout<<"RICHARD"<<endl;
		}
		count++;
	}
	
return 0;
}
