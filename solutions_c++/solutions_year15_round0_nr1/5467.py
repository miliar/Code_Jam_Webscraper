#include <iostream>
#include "bits/stdc++.h"
using namespace std;
int main() {
	int t;int u=0;
	  scanf("%d",&t);
	    while(t--)
	    {
	    	u++;
	    	 long long h;
	    	   scanf("%lld",&h);
 	  char s[1005];
	    	long long khadebande=0;
	      
	    	     scanf("%s",s);
	    	    long long ans=0;
	    	    //scanf("%s",&s);
	    	for(int i=0;i<=h;i++)
	    	{
	    		if(khadebande<i)
	    		{
	    			ans+=i-khadebande;
	    			khadebande+=i-khadebande;
	    		}
	    	
	    		 
	    		 	khadebande+=s[i]-'0';
	    		 //cout<<khadebande<<" ";
	    	}
	    	printf("Case #%d: %d\n",u,ans);
	    }
	return 0;
}