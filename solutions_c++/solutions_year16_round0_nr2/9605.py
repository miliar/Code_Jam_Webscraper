#include <iostream>
#include <algorithm>
#include <string>
#define ll long long 

using namespace std;
int main() 
{
	freopen("B-large.in","r",stdin),freopen("op.out","w",stdout);
	// your code goes here
	ll t,ct=1;
	cin>>t;
	while(t--)
	{
	    ll n,k,count,i,h,l;
	    string s;
	    char temp;
	    cin>>s;
	    k=s.size()-1;
	    count=0;
	    while(k!=0)
	    {
	        if(s[k]=='+')
	        {
	            k--;
	        }
	        else
	        {
	            ll temp2=0;
	            if(s[0]=='+')
	            {
	                while(s[temp2]=='+')
	                {
	                    s[temp2]='-';
	                    temp2++;
	                }
	                
	            }
	            else
	            {
	                h=0;l=k;
	                while (h < l) {
                      temp = s[h];
                      s[h] = s[l];
                      s[l] = temp;
                      h++;
                      l--;
                    }
	                for(i=0;i<=k;i++)
	                {
	                    if(s[i]=='+')
	                    {
	                        s[i]='-';
	                    }
	                    else
	                    {
	                        s[i]='+';
	                    }
	                }
	            }
	            count++;
	        }
	    }
	    if(s[0]=='-')
	    count++;
	    cout<<"Case #"<<ct<<": "<<count<<endl;
	    ct++;
	}
	return 0;
}
