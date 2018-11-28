#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
  int t, l, count, j;
  string s, temp;
  bool flag;

  cin>>t;
  for(int i=1; i<=t; i++)
    {
      cin>>s;
      flag=0;
      count=0;

      while(flag==0)
	{
	  j=0;
	  while(s[j+1]!= '-' && s[j] == '+' && j<s.length())
	    {
	      j++;
	    }
	  if(s[j] == '+' && j!=s.length()-1)
	    {
	      l=0;
	      for(int k=j; k>=0; k--)
		{
		  if(s[k] == '-')
		    s[k] = '+';
		  else if(s[k] == '+')
		    s[k] = '-';
		  temp[l++] = s[k];
		}
	      l=0;

	      for(int k=0; k<=j; k++)
		{
		  s[k] = temp[l++];
		}
	      count++;
	      //cout<<"1st:"<<count<<endl<<s<<endl;
	    }
	  
	  for(j=s.length()-1; j>=0; j--)
	    {
	      if(s[j] == '-')
		{
		  l=0;
		  for(int k=j; k>=0; k--)
		    {
		      if(s[k] == '-')
			s[k] = '+';
		      else if(s[k] == '+')
			s[k] = '-';
		      temp[l++] = s[k];
		    }
		  l=0;

		  for(int k=0; k<=j; k++)
		    {
		      s[k] = temp[l++];
		    }
		  
		  count++;
		  //cout<<"2nd:"<<count<<endl<<s<<endl;
		  break;
		}
	    }
	  for(j=s.length()-1; j>=0; j--)
	    {
	      if(s[j] == '-')
		{
		  flag=0;
		  break;
		}
	      if(s[j] == '+')
		flag=1;
	    }
	}
      cout<<"Case #"<<i<<": "<<count<<endl;
    }

  return 0;
}
