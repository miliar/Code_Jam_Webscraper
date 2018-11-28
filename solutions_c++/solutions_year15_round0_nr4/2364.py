#include<bits/stdc++.h>

using namespace std;

int main(){
	
int a,j=1,x,r,c;
	cin>>a;
	while(a>0){
		cin>>x>>r>>c;
		if((r*c)%x!=0)
			cout<<"Case #"<<j<<": RICHARD"<<endl;
		
		else{
			if(x-1>r||x-1>c)
				cout<<"Case #"<<j<<": RICHARD"<<endl;
			else
				cout<<"Case #"<<j<<": GABRIEL"<<endl;
			}
	j++;
	a--;
	}
return 0;
}