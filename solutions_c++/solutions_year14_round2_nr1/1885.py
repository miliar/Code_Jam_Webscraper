/*krypto.............................jagsxi...!! */
#include<bits/stdc++.h>
using namespace std;
int fastread( int* a) 
{ char c=0; 
while (c<33) 
c=getchar_unlocked(); 
*a=0; 
while (c>33) { 
*a=*a*10+c-'0'; 
c=getchar_unlocked(); 
} 
return 0; }

int main()
{
	int t, n,tt=0;  
fastread(&t);
	string s[103];
	while(t--)
	{ 
		tt++;
		
		
		int ans=0,i,j,k,l,ct1,ct2,flag=0;
		cin>>n;
		
		for(i=0;i<n;i++)
		 cin>>s[i];
		 
		 cout<<"Case #"<<tt<<": ";
		 
		for(i=0,k=0;i<s[0].length() && k<s[1].length();)
		{  
			if(s[0][i]!= s[1][k])
			{
				 flag=1;
				 break;
			}	 
			
			j=i,ct1=ct2=0;
			for(;s[0][j]==s[0][i];i++)
			 ct1++;
			
			l=k;
	        for(;s[1][k]==s[1][l];k++)
			 ct2++;
			 
			ans+=(ct1-ct2>0 ? ct1-ct2:ct2-ct1);
		}	
			 	 
		if(flag==0 && i==s[0].length() && k==s[1].length() )
		 cout<<ans<<endl;
		 
		else
		 cout<<"Fegla Won\n"; 
    }  	  
	return 0;
}		
