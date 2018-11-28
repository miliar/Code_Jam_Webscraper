#include<iostream>
#include<string>
#include<vector>
#include<stdio.h>
using namespace std;

int check_status(string s[], char c)
{
  bool flag;
  
  // In Row
  for(int i=0;i<4;i++)
    {
      flag = true;
      for(int j=0;j<4;j++)
	{
	  if(s[i][j]!= c && s[i][j] != 'T')
	    {
	      flag=false;
	      break;
	    }
	}
      if (flag)
	return 1;
    }
  
  // In column
  for(int i=0;i<4;i++)
    {
      flag = true;
      for(int j=0;j<4;j++)
	{
	  if(s[j][i]!=c && s[j][i] != 'T')
	    {
	      flag=false;
	      break;
	    }
	}
      if (flag)
	return 1;
    }

  // In  diagonal
  flag=true;
  for(int i=0;i<4;i++)
    {
      if(s[i][i]!=c && s[i][i] != 'T')
	{
	  flag=false;
	  break;
	}
    }
  if(flag)
    return 1;
  
  // In digonal
  flag=true;
  int k=3;
  for(int i=0;i<4;i++)
    {
      if(s[i][k]!=c && s[i][k] != 'T')
	{
	  flag=false;
	  break;
	}
      k--;
    }
  if(flag)
    return 1;

  
  // Check '.'
 
  for(int i=0;i<4;i++)
    {
      flag = false;
      for(int j=0;j<4;j++)
	{
	  if(s[i][j]=='.')
	    {
	      flag=true;
	      break;
	    }
	}
      if (flag)
	return 2;
    }

 
  return 0;
}


int main(){
  string s[4];
  int t;
  cin >> t;
  int m=t;
  int i=0;
  while(m--)
    {
      for(int j=0;j<4;j++)
	cin >> s[j];
      int status=check_status(s,'X');
      int status1=check_status(s,'O');
      if(status==1)
	printf("Case #%d: X won\n", i+1);
      else if(status1==1)
	printf("Case #%d: O won\n", i+1);
      else if(status==0 && status1 ==0)
	printf("Case #%d: Draw\n", i+1);
      else if (status==2 && status1==2)
	printf("Case #%d: Game has not completed\n", i+1);
      i++;
	
    }
  
  return 0;
}
