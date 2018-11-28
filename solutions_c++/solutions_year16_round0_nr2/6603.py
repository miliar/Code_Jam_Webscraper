#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	int t,i=1,count;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		count=0;
		int j=0,l=s.length();
        while(j<l)
        {
        	if(s[j]=='+')j++;
        	if(s[j]=='-'){
        		if(j==0){
        			int k;
        			for(k=0;k<l;k++)
					   if(s[k]=='+')break;
					if(k==l){
					   count++;
					   break;
				    }
				    j=k;
				    count++;
				}
				else
				{
					while(s[j]=='-')j++;
					count+=2;
				}
			}
	    }
	    
		cout<<"Case #"<<i<<": "<<count<<endl;
	    i++;
	}
	return 0;
}
