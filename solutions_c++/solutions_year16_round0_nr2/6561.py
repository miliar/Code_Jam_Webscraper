#include <iostream>
#include <cstring>
using namespace std;

int a[100];

void cleararr()
{
	int i;
	for(i=0;i<100;i++){
		a[i]=0;
	}
}

int nhappy(int len){
	int i;
	for(i=0;i<len;i++){
		if(a[i]==1){
			return 0;
		}
	}
	return 1;
}

void findminus(int len){
	int i,j;
	for(i=len-1;i>=0;i--){
		if(a[i]==1){
			//cout<<"i="<<i<<endl;
			for(j=0;j<=i;j++){
				a[j]=1-a[j];
			}
			break;
		}
	}
}

void printa(int len){
	int i;
	for(i=0;i<len;i++){
		cout<<a[i];
	}
	cout<<endl;
}

int main() {
	// your code goes here
	int c,n,t,i,j,len,count;
	char s[100];
	cin>>t;
	for(i=1;i<=t;i++){
		//cleararr();
		cin>>s;
		j=0;
		len=strlen(s);
		//cout<<strlen(s)<<endl;
		while(j<len){
			if(s[j]=='+'){
				a[j]=0;
			}
			else{
				a[j]=1;
				//cout<<"hi";
			}
			j++;
		}
		count=0;
		while(!nhappy(len)){
		//while(count<5){
			//printa(len);
			findminus(len);
			count++;
		}	
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}