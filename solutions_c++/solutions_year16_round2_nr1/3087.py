#include<bits/stdc++.h>
#define ll long long 
using namespace std;
int main()
{
//	freopen("in.txt","r",stdin);//
//	freopen("out.txt","w",stdout);
   int t;
   cin>>t;int test=1;
   while(t--)
   {
   	string s;
   	cin>>s;
    ll arr[150]={0};
	for(int i=0;i<s.length();i++)
	{
		arr[s[i]]++;
	}	 
	   
	     ll  dp[12]={0};
     	int x;
     	
		 x=arr['Z'];
	     dp[0]=x;//arr['Z'];
		arr['Z']-=x;
		arr['E']-=x;
		arr['R']-=x;
		arr['O']-=x;
        
		x=arr['W'];
        dp[2]=x;
		arr['W']-=x;
		arr['T']-=x;
		arr['O']-=x;
	 
        x=arr['U'];
    	dp[4]=x;
        arr['U']-=x;
		arr['F']-=x;
		arr['R']-=x;
		arr['O']-=x;
 
 
		x=arr['X'];
		dp[6]=x;
		arr['X']-=x;
		arr['I']-=x;
		arr['S']-=x;
   		
		   x=arr['G'];
		dp[8]=x;
		arr['E']-=x;
		arr['I']-=x;
		arr['G']-=x;
		arr['H']-=x;
		arr['T']-=x;


   		x=arr['F'];
		dp[5]=x;
		arr['F']-=x;
		arr['I']-=x;
		arr['V']-=x;
		arr['E']-=x;
	
		 x=arr['V'];
		 dp[7]=x;
		arr['S']-=x;
		arr['E']-=x;
		arr['V']-=x;
		arr['E']-=x;
		arr['N']-=x;

  		x=arr['R'];
		dp[3]=x;
		arr['T']-=x;
		arr['H']-=x;
		arr['R']-=x;
		arr['E']-=x;
		arr['E']-=x;


    	 x=arr['O'];
		dp[1]=x;
		arr['O']-=x;
		arr['N']-=x;
		arr['E']-=x;
	//	arr['T']-=x;
	
	
   		x=arr['E'];
		dp[9]=x;
		arr['N']-=x;
		arr['I']-=x;
		arr['E']-=x;
		arr['N']-=x;
		//arr['T']-=x;
	

	cout<<"Case #"<<test<<": ";
   for(int i=0;i<10;i++)
   {
   	 for(int j=0;j<dp[i];j++)
   	  cout<<i;
   }	
	
	cout<<endl;
	
	test++;
   	
   }

	return 0;
}
