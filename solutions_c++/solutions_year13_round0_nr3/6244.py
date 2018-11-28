#include<iostream>
#include<math.h>

using namespace std;

int palindrome(int x)	{
  int tmp=x;
  int digit,rev=0;
  
  while(x!=0)	{
    digit=x%10;
    rev=rev*10+digit;
    x=x/10;
  }
  if(tmp==rev)
     return 1;
  return 0;
}

int main()	{
  int tc;
  
  cin>>tc;
  for(int i=0;i<tc;i++)	{
    int a,b;
    int cnt =0;
    cin>>a>>b;
    
    for(int j=a;j<=b;j++)	{
      if(palindrome(j))	{
	float x=sqrt(j)-int(sqrt(j));
	if(x==0)
	if(palindrome(sqrt(j)))	{
	  cnt++;
	}
      }
    }
    
    cout<<"Case #"<<i+1<<": "<<cnt<<endl;
  }
  return 0;
}