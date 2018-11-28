#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	unsigned long int test;
	cin>>test;
	unsigned long int temp1=1;
	
	while(test--){
		 char str[2000];
		scanf("%s",str);
		char temp[2000];
		char t=str[0];
		temp[0]=t;
		int k=1;
		for (int i = 1; i < strlen(str); ++i)
		{
			
			if(str[i]<t){
				temp[k++]=str[i];
				
			}
			else{
				
				 char tempstr[2000];
				for (int j = 0; j < k; ++j)
				{
					tempstr[j]=temp[k-j-1];

				}
				tempstr[k++]=str[i];

				t=str[i];
				
				for (int j = 0; j < k; ++j)
				{
					temp[j]=tempstr[k-j-1];

				}

				
			}
		}
		cout<<"Case #"<<temp1<<": ";
		temp1++;
		for (int i = 0; i < k; ++i)
		{
			printf("%c",temp[i]);
		}
		cout<<endl;

	}
	return 0;
}	