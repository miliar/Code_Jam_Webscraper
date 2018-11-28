#include<iostream>
using namespace std;
int main(){
	int t,j=0;
	cin>>t;
	int result[t];
	while(j<t){
		int x,r,c;
		cin>>x>>r>>c;
		if(r*c % x == 0){
			if(r*c == x){
				if(x<=2)
					result[j]=1;
				else
					result[j]=0;
			}
			else
				result[j]=1;
		}
		else
			result[j]=0;
		if(x==4 && r*c ==8)
			result[j]=0;
		j++;
	}
	for(j=0;j<t;j++){
		if(result[j]==0)
			cout<<"Case #"<<j+1<<": RICHARD"<<endl;
		else
			cout<<"Case #"<<j+1<<": GABRIEL"<<endl;
	}
	return 0;
}
