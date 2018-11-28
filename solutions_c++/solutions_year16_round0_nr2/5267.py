#include <iostream>

using namespace std;

int l;
char a[101];

long int coin(long int count){
	
	int i,j=0,flag=0;
	
	for(i=0;i<l;i++){
		if(a[i]=='-'){
			flag=1;
			break;
		}
	}
	if(flag==0)
		return count;

	char p = a[0];
	
	i=1;
	while(a[i]==p)
		i++;

	if(i==l)
		i--;

	if(p=='-' && a[i]=='+'){
		while(j<i)
			a[j++]='+';
		return coin(count+1);
	}
	else if(p=='+' && a[i]=='+'){
		return coin(count);
	}
	else if(p=='+' && a[i]=='-'){
		while(j<i)
			a[j++]='-';
		return coin(count+1);
	}
	else {
		while(j<=i)
			a[j++]='+';
		return coin(count+1);
	}
}

int main(){
	int i,t,j;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>a;
		for(l=0;a[l]!='\0';l++);
		if(l==1){
			if(a[0]=='-'){
				cout<<"Case #"<<i<<": "<<1<<endl;
			}
			else {
				cout<<"Case #"<<i<<": "<<0<<endl;
			}
		}
		else{
			j=coin(0);
			cout<<"Case #"<<i<<": "<<j<<endl;
		}
	}
		return 0;
	}