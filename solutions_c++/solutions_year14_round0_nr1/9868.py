#include<iostream>
using namespace std;

int main(){
	int T=0;
	cin>>T;
	for(int k=1;k<=T; k++){
		int r=0;
		int row=0;
		cin>>r;
		for(int i=1; i<=4; i++)
			for(int j=0; j<4; j++){
				int temp;
				cin>>temp;
				if(i==r){
					row|=1<<temp;
				}
			}
		int answer=0, count=0;
		cin>>r;
		for(int i=1; i<=4; i++)
			for(int j=0; j<4; j++){
				int temp;
				cin>>temp;
				if(i==r && ((1<<temp)&row)>0){
					answer=temp;
					count++;
				}
			}
		if(count>=2)
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		if(count==1)
			cout<<"Case #"<<k<<": "<<answer<<endl;
		if(count<=0)
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
	}
	return 0;
}
