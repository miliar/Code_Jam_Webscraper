#include <iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	int t,neg_flag=0,test=1,i;
	cin>>t;
	while(t--)
	{
			  char str[105],ans=0;
			  cin>>str;
			  int l=strlen(str);
			  for(i=0;i<l;i++)
			  {
							  if(str[i]=='-') neg_flag=1;
							  else
							  if(str[i]=='+' && neg_flag == 1 )
							  {
											 neg_flag=0;
											 ans+=2;
							  }
			  }
			  if(neg_flag == 1 )
			  {
 			   				 neg_flag=0;
							 ans+=2;
              }
              if(str[0]=='-') ans--;
			  printf("Case #%d: %d\n",test++,ans);
	}
	return 0;
}
