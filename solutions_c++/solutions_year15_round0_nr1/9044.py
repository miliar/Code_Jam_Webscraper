#include<bits/stdc++.h>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
    int t;
    cin>>t;
    int r=t;
    while(t--)
    {
	int n;
    	cin>>n;
        string s;
        cin>>s;
        
        //int n=s.length();
    	int sum=int(s.at(0)-48);
    	int req=0;
        for(int i=1;i<=n;i++)
        {
	    if((s.at(i)-48)!=0)
            {
		if(sum<i)
        	{
			req+=(i-sum);
			sum=sum+i-sum;       
        	}
            	sum=sum+(s.at(i))-48;
	    }   
        }
        cout<<"Case #"<<r-t<<": "<<req<<"\n";
    }
    return 0;
}