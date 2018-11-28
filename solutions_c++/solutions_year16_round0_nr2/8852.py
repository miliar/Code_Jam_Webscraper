#include<bits/stdc++.h>
using namespace std;
char s[102];
long long int cnt=0;
int main()
{
	int t; scanf("%d",&t);
	
	for(int test=1;test<=t;test++)
	{
		scanf("%s",s);
		cnt=0;
		int length=strlen(s);
		while(true)
    	 {
    	   int index=0;
    	   if(s[index]=='-')
    	   	{ 

    	   		while(s[index]=='-'&& index<length)  index++;
    	        for(int j=0;j<index;j++) s[j]='+';
    	        cnt++;
    	 	}
     	    else
    	    { 
    	    	int j;
    	        for(j=0;j<length;j++)
    	        { 
    	        	if(s[j]=='-') break;
    	        }
    	        if(j== length) break;
     			while(s[index] =='+'&& index<length) index++;
    	        for(j=0;j<index;j++) s[j]='-';
    	        cnt++;
    	    } 
		}
		printf("Case #%d: %lld\n",test,cnt);
	}
	return 0;
}