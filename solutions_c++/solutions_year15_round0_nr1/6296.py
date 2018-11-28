#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T,i,j;
  
  scanf("%d\n", &T);
  
  for(int i=1; i<=T ; i++)
  {
  	printf("Case #%d:", i);
  	
	int S,cnt=0,sum=0,val;
  	char str[1002];
	scanf("%d %s", &S, str);  	

  	//int len=str.length();
  	
	for(int j=0;j<(S+1);j++)
  	{
  		val=str[j];
  		val=val-48;
  		//cout<<"val"<<val;
  		if(sum>=j)
  		{
  			sum=sum+val;
			continue;	
		}
  		else
  		{
  			if(val==0)
  				sum=sum+1;
  			else
  				sum=sum+(val+1);
  			cnt=cnt+1;
		}
	}
	printf(" %d\n",cnt);
  }
  return 0;
}
