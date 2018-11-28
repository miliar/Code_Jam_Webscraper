#include<bits/stdc++.h>
using namespace std;
int main()
{
	  freopen("inputo.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
	int t,x,r,c,i,a=1;
	cin>>t;
	while(a<=t)
	{
		cin>>x>>r>>c;
	    int flag;  
	    
	    if(x==1)
		flag=0;
		else if(x==2)
		{
			if(r%2==0 || c%2==0)
			flag=0;
			else
			flag=1;
		} 
		else if(x==3)
		{
			if((r%3==0 && c>=2)||(c%3==0 && r>=2))
			flag=0;
			else
			flag=1;
		}
		else if(x==4)
		{
			if((r%4==0 && c>=3)||(c%4==0 && r>=3))
			flag=0;
			else
			flag=1;
		}
		
		
		
		if(flag)
		cout<<"Case #"<<a<<": RICHARD"<<"\n";
		else
		cout<<"Case #"<<a<<": GABRIEL"<<"\n";
		
		 a++;
	}
	return 0;
}
