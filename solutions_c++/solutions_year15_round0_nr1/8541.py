#include<iostream>
#include<vector>
#include <stdio.h>

using namespace std;
int main(){

freopen("A-large.txt","r",stdin);
freopen("out.txt","w",stdout);

int n,s;
cin>>n;
for(int i=0;i<n;i++){
	string num;
	cin>>s;
	cin>>num;	
	int res=0;
	int temps=0;
	for(int j=0;j<num.length();j++){
		if(num[j]=='0' && j==0){
			temps+=1;
			res+=1;
		}else if(num[j] !='0' && j > temps){
			int temp;
			temp = (j-temps);
			temps+=temp;
			res+=temp;
		}
		temps+=((int)num[j]-48);
		//cout<<j << "   " << temps<<"     " << res<<endl;
	}
	
	
	cout<<"Case #"<<i+1<< ": "<< res<<endl;	
}	
	
}
