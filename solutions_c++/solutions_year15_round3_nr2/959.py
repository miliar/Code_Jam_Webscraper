#include<bits/stdc++.h>
using namespace std;
string target;
string keys;
int k,l,s;
int sub[8];
int z[25];

int sum;
int max1;

void eval()
{
	string work="";
	
	work+=target;
	
	work+="$";
	
	for(int i=0; i<s; i++)
	{
		work+=keys[sub[i]];
	}
	
//	cout<<work<<endl;
	
//	int X;
	
//	cin>>X;
	
	int n=work.length();
	
	int L = 0, R = 0;
	for (int i = 1; i < n; i++) 
	{
  	 if (i > R) 
	   {
       	L = R = i;
    	while (R < n && work[R-L] == work[R]) R++;
    	z[i] = R-L; R--;
  		}
		  else 
		{
    		int k = i-L;
    		if (z[k] < R-i+1) z[i] = z[k];
    		else 
			{
      		L = i;
     		 while (R < n && work[R-L] == work[R]) R++;
      		 z[i] = R-L; R--;
    		 }
		 }
	 }
	 
  int C=0;
  int temp=target.length();
  
  for(int i=1; i<n; i++)
  {
  	if(z[i]==temp)
  	C++;
  }
  
  //cout<<C<<endl;
  
 sum+=C;
 
 if(C>max1)
 max1=C;
	
}

void subsets(int x)
{
	if(x==s)
	{
		eval();
	}
	else
	{
		for(int i=0; i<k; i++)
		{
			sub[x]=i;
			subsets(x+1);
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		cin>>k>>l>>s;
		cin>>keys;
		cin>>target;
		
		for(int i=0; i<=7; i++)
		sub[i]=0;
		
		sum=0;
		max1=-1;
		subsets(0);
		
		double ss=sum;
		double ans=0;
		ans=(ss/pow(k,s));
		
		ans=max1-ans;
		//cout<<sum<<endl;
		cout<<"Case #"<<t<<": ";
		std::cout << std::setprecision(7) << ans << '\n';
	}
	return 0;
}
