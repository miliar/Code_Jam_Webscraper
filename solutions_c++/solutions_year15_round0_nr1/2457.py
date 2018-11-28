#include<iostream>
using namespace std;
#include<bits/stdc++.h>
int main()

 {
 	  freopen("abc.txt","r",stdin);
 	  freopen("pqr.txt","w",stdout);
 	int t;
 	
 	 cin>>t;
 	 int tt=1;
 	   while(t--)
 	    {
 	    	int n;
 	    	 cin>>n;
 	    	   char arr[100000];
 	    	    cin>>arr;
 	    	    //int ans=0;
 	    	    int len=strlen(arr);
 	    	  long long   int sum=0;
 	    	  long long int ans=0;
 	    	     for(int i=0;i<len;i++)
 	    	      {
 	    	      	if(arr[i]!=0 && sum<i)
 	    	      	 {
 	    	      	 	 
 	    	      	 	 ans+=i-sum;
 	    	      	 ///	  cout<<"ans "<<ans<<endl;
 	    	      	 	 sum+=i-sum;
 	    	      	 	 
 	    	      	 }
 	    	      	 
 	    	      	  sum+=arr[i]-'0';
 	    	      	 //cout<<"sum "<<sum<<endl;
 	    	      }
 	    	        cout<<"Case #"<<tt++<<": "<<ans<<endl;
 	    }
 	    return 0;
 }
