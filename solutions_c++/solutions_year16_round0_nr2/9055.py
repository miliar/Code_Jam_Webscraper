#include<iostream>
#include<string.h>
using namespace std;

int main(){
	int t,i,j;
	char s[100];

	cin>>t;

	for(i=0;i<t;i++){
		cin>>s;
		
		int count=0;
		j=1;
		while(j<strlen(s)){
			   if(s[j-1]!=s[j])
					count++;
			   		
			   
			   	j++;

		}

			if(s[strlen(s)-1]=='+')
			cout<<"Case #"<<i+1<<": "<<count<<endl;
			else
				cout<<"Case #"<<i+1<<": "<<count+1<<endl;
	

	}

}
