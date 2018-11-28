#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  for(int z=1;z<=t;z++)
  {
    string s;
    cin>>s;
    int temp=0;
    for(int i=s.size()-1;i>=0;i--)
    {
      if(s[i]=='+')
	temp++;
      else
	break;
    }
    if(temp==s.size())
    {
      printf("Case #%d: %d\n",z,0);
      continue;
    }
    s=s.substr(0,s.size()-temp);
    int ans=0;
    while(1)
    {
      int temp=0;
      for(int i=0;i<s.size();i++)
      {
	if(s[i]=='-')
	  temp++;
      }
      if(temp==s.size())
      {
	printf("Case #%d: %d\n",z,ans+1);
	break;
      }
      for(int i=0;i<s.size();i++)
      {
	if(s[i]=='+')
	{
	  if(i!=0)
	    ans+=2;
	  else
	    ans+=1;
	  for(int k=i;k<s.size();k++)
	  {
	    if(s[k]=='-')
	      break;
	    s[k]='-';
	  }
	}
      }
    }
    //printf("Case #%d: %d\n",z,ans);
  }
  return 0;
}
      
      