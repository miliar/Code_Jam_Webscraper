#include<iostream>
using namespace std;
int main (){
	int x;
	cin>>x;
	int original,times,student;
	for(int i=1;i<=x;i++){
		cin>>original>>times>>student;
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=original;j++){
			cout<<j;
			if(j==original){
				cout<<endl;
			}else{
				cout<<" ";
			}
		}
	}
}
