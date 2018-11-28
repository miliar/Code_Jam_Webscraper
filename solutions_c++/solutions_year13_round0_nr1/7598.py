#include<iostream>

using namespace std;

int main()	{
  int tc;
  
  cin>>tc;
  
  char t[4][4];
  
  
  for(int i=0;i<tc;i++)	{
    for(int j=0;j<4;j++)	{
      for(int k=0;k<4;k++)	{
	cin>>t[j][k];
      }
    }
    int flag=0,j=0,k=0,tmp;
    if(j==0 && k==0)	{
      for(tmp=0;tmp < 3;tmp++)	{
	if(t[tmp][tmp]==t[tmp+1][tmp+1] && t[tmp][tmp]!= '.')
	  continue;
	else
	  if(t[tmp][tmp]=='T' || t[tmp+1][tmp+1]=='T')
	      continue;
	  break;
      }
      if(tmp==3)	{
	cout<<"Case #"<<i+1<<": "<<char(t[tmp][tmp]=='T' ? t[tmp-1][tmp-1] : t[tmp][tmp])<<" won"<<endl;
	flag=1;
 	continue;
      }
    }
    j=0;k=3;
    if(flag!=1)
    {
      for(tmp=0;tmp < 3;tmp++,j++,k--)	{
	if(t[j][k]==t[j+1][k-1] && t[j][k]!= '.')
	  continue;
	else
	  if(t[j][k]=='T' || t[j+1][k-1]=='T')
	    continue;
	  else
	    break;
      }
      if(tmp==3)	{
	cout<<"Case #"<<i+1<<": "<<char(t[j][k]=='T' ? t[j-1][k+1] : t[j][k])<<" won"<<endl;
	flag=1;
	continue;
      }
    }
    if(flag!=1)
    for(j=0;j<4;j++)	{
      for(tmp=0;tmp < 3;tmp++)	{
	if(t[j][tmp]==t[j][tmp+1] && t[j][tmp]!= '.')
	  continue;
	else
	  if(t[j][tmp]=='T' || t[j][tmp+1]=='T')
	    continue;
	  else
	    break;
      }
      if(tmp==3)	{
	cout<<"Case #"<<i+1<<": "<<char(t[j][tmp]=='T' ? t[j][tmp-1] : t[j][tmp])<<" won"<<endl;
	flag=1;
	break;
      }
    }
    if(flag!=1)
    for(k=0;k<4;k++)	{
      for(tmp=0;tmp < 3;tmp++)	{
	if(t[tmp][k]==t[tmp+1][k] && t[tmp][k]!= '.')
	  continue;
	else
	  if(t[tmp][k]=='T' || t[tmp+1][k]=='T')
	    continue;
	  else
	    break;
      }
      if(tmp==3)	{
	cout<<"Case #"<<i+1<<": "<<char(t[tmp][k]=='T' ? t[tmp-1][k] : t[tmp][k])<<" won"<<endl;
	flag=1;
	break;
      }
    }
    if(flag==0)	{
      for(j=0;j<4;j++)	{
	for(k=0;k<4;k++)	{
	  if(t[j][k]=='.' && flag != 1)	{
	    cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	    flag=1;
	    //break;
	  }
	}
      }
      if(flag!=1)	{
	cout<<"Case #"<<i+1<<": Draw"<<endl;
      }
    }
  }
  return 0;
}