#include <bits/stdc++.h>
using namespace std;
int main()
{   int t,r=1;
	/*#ifndef ONLINE_JUDGE
	    freopen("input.txt","r",stdin);
	    // freopen("output.txt","w",stdout);
	  #endif*/
	cin>>t;
	while(t--)
	{  
      string s; long long ans = 0;
      cin>>s;
      int i=0;
      for( ; i<=s.size()-1;)
      {
        //cout << "hi";
      	i=0;
      	if(s[0] == '-')
      	
      	{ 
          //cout << "ti ";
      		ans++;
      		while( i<=s.size()-1 && s[i]=='-' )
      		{
            //cout << "1 ";
      			i++;
      		}
      		for(int j=0,k=i-1;j<k;j++,k--)
          	{
              //cout << "2 ";
          	   swap(s[j],s[k]);
          	}

          for(int j=0;j<i;j++)
           
           { 
            //cout << "ki";
            if(s[j]=='-')
          		s[j]  = '+';
          	else
          		s[j]  = '-';
           }
        }
        else
        {
        	//ans++;
        	while( i<=s.size()-1 && s[i]=='+' )
        	{
        		i++;
        	}
        	for(int j=0,k=i-1;j<k;j++,k--)
          	{
          	   swap(s[j],s[k]);
          	}

          for(int j=0;j<i;j++)
           
           { if(s[j]=='-')
          		s[j]  = '+';
          	else
          		s[j]  = '-';
           }
           if(i>s.size()-1)
        {
          break;
        }
        ans++;
        }

        //cout << s << endl;
      }
cout<<"Case #"<<r<<": "<<ans<<endl;
      r++;
    }
    return 0;
}