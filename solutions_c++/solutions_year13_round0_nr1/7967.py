#include<stdio.h>
#include<algorithm>
#include<map>
#include<cctype>
#include<ctime>
#include<set>
#include<string.h>
#include<sstream>
#include<numeric>
#include<vector>
#include<queue>
#include<stdlib.h>
#include<iostream>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define scan(x) scanf("%d",&x)
#define f(i,a,n) for(i=a;i<n;i++)
#define ulli unsigned long long int 64

// freopen("input.txt","r',stdin);
/*
 * 
 
  ostringstream oss;
 oss << 1 << "any string";
 to convert oss to string use - oss.str():
 
 
 */
const int size = 1<<18;
char buff[size];
int lp=0,up=0;
char read_char()
{
  if(lp==up)
  {
    up=fread(buff,sizeof(char),size,stdin);
    if(up==0)
      return 0;
    lp=0;
  }
  return buff[lp++];
}
int read_int()
{
  char c;
  do{
    c=read_char();
  }while(c<'0' || c>'9');
  
  int val=0;
  for(;c>='0' && c<='9';c=read_char())
    val=(val<<3) +(val<<1) + c-'0';
  
  return val;
}

main()
{
    int t,i,n=4,j,x=0;
    scanf("%d",&t);
    while(t--)
    {
      i=0;
      j=0;
      char ch[n][n];
      //vector< vector<char> >ch(n,vector<char>(n));
      F(i,n)
	scanf("%s",ch[i]);
	
      int flag=0,draw=1;
      char c='\0',m='\0';

      map<char,int>mp;
      mp['X']=0;
      mp['O']=1;
      mp['T']=2;
      
      F(i,n)
      {
	vector<int>arr(3,0);
	c=ch[i][0];
	arr[mp[c]]++;
	flag=1;
	f(j,1,n)
	{
	  if(ch[i][j]=='.')
	  {
	    flag=0;
	    draw=0;
	    break;
	  }
	  arr[mp[ch[i][j]]]++;
	}
	
	if(flag)
	{
	if(arr[0]>0)
	{
	  if(arr[0]==4 || (arr[0]==3 && arr[2]==1))
	  {  
	    flag=2;
///	    printf("if %d %c\n",i,c);
	    c='X';
	    break;
	  }
	  else 
	  {
	    flag=0;
	  }
	}
	else
	{
	  if(arr[1]==4 || (arr[1]==3 && arr[2]==1))
	  {
	    flag=2;
///	    printf("else %d %c\n",i,c);
	    c='O';
	    break;
	  }
	  else
	    flag=0;
	}
	}
      }
      
      if(flag!=2)
      {
      F(i,n)
      {
	vector<int>arr(3,0);
	c=ch[0][i];
	arr[mp[c]]++;
	flag=1;
	f(j,1,n)
	{
	  if(ch[j][i]=='.')
	  {
	    flag=0;
	    draw=0;
	    break;
	  }
	  arr[mp[ch[j][i]]]++;
	}
	
	if(flag){
	if(arr[0]>0)
	{
	  if(arr[0]==4 || (arr[0]==3 && arr[2]==1))
	  {  
	    flag=2;
///	    printf("if2 %d %c\n",i,c);
	    c='X';
	    break;
	  }
	  else 
	  {
	    flag=0;
	  }
	}
	else
	{
	  if(arr[1]==4 || (arr[1]==3 && arr[2]==1))
	  {
	    flag=2;
///	    printf("else2 %d %c\n",i,c);
	    c='O';
	    break;
	  }
	  else
	    flag=0;
	}
	  
	}
      }
      }
      
      if(flag!=2)
      {
	vector<int>arr(3,0);
	F(i,n)
	 if(ch[i][i]!='.')
	  arr[mp[ch[i][i]]]++;
	 else
	   break;
	 
	if(arr[0]==4 || (arr[0]==3 && arr[2]==1)){
	  flag=2;
//	    printf("diag if2 %d %c\n",i,c);
	  c='X';
	}
	else if(arr[1]==4 || (arr[1]==3 && arr[2]==1))
	{
	  flag=2;
//	    printf("diag else2 %d %c\n",i,c);
	  c='O';
	}
	
	if(flag!=2)
	{
	  vector<int>arr(3,0);
	  for(i=n-1;i>=0;i--)
	    if(ch[n-1-i][i]!='.')
	      arr[mp[ch[n-1-i][i]]]++;
	    else
	      break;
	  if(arr[0]==4 || (arr[0]==3 && arr[2]==1)){
	    flag=2;
	    c='X';
//	    printf("diag if3 %d %c\n",i,c);
	  }
	  else if(arr[1]==4 || (arr[1]==3 && arr[2]==1))
	  {
	    flag=2;
	    c='O';
//	    printf("diag else3 %d %c\n",i,c);
	  }
	}
      }
      
      printf("Case #%d: ",++x);
      if(flag==2)
      {
	printf("%c won\n",c);
      }
      else
      {
	if(draw)
	  puts("Draw");
	else
	{
	  puts("Game has not completed");
	}
      }
      
    }

  return 0;
}
