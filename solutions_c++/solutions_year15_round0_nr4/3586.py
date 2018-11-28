#include<iostream>

using namespace std;

int main(){
	int t,x,r,c,flag;
	cin>>t;
	for(int z=0;z<t;z++){
		flag=1;
		cin>>x>>r>>c;		
		if(x>=7){
			cout<<"Case #"<<z+1<<": "<<"RICHARD"<<endl;
			flag=0;
			continue;
		}
		if(x>r&&x>c){
			cout<<"Case #"<<z+1<<": "<<"RICHARD"<<endl;
			flag=0;
			continue;
		}
		if(x>3){
			if(((r*c)/x)==2){
				cout<<"Case #"<<z+1<<": "<<"RICHARD"<<endl;
				flag=0;
				continue;
			}
		}
		if(((r*c)%x)!=0){
			cout<<"Case #"<<z+1<<": "<<"RICHARD"<<endl;
			flag=0;
			continue;
		}
		int a=1,b=x;
		for(int i=0;i<x;i++){
			if((a*b)>(r*c)){
				cout<<"Case #"<<z+1<<": "<<"RICHARD"<<endl;
				flag=0;
				break;
			}
			a++;
			b--;
		}
		if(flag){
			cout<<"Case #"<<z+1<<": "<<"GABRIEL"<<endl;
 		}
	}
	return 0;
}
