#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    
    int n;
    int t,l,min,sum,temp,j=1;	
	cin>>t;
	string s;
	while(t--)
	{   min=sum=0;
	    cin>>n;
	    cin>>s;
	    l=s.length();
	    for(int i=0;i<l;i++)
	    {
	        sum+=s[i]-'0';
	        //cout<<sum;
	        if(sum<(i+1))
	        {
	           temp=sum;
	           sum+=i+1-sum;
	           min+=i+1-temp;
	        }
	        
	    }
	    cout<<"Case #"<<j<<": "<<min;
	    j++;
	    cout<<"\n";
	}
	return 0;
}