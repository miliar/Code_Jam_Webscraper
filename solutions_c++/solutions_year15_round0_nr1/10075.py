#include<iostream>
using namespace std;
int main(){
	int t,size,i,j,k,count,invite;
	string a;
	cin>>t;
	k=0;
	while(t--){
		k++;
		cin>>size;
		cin>>a;
		count=0;
		invite=0;
		for(i=0;i<=size;){
			if(i<=count){
				count=count+(a[i]-'0');
				i++;
			}
			else{
				i--;
				a[i]=((a[i]-'0')+1)+48;
				invite++;
			}
		}
		cout<<"Case #"<<k<<": "<<invite<<"\n";
	}
}
