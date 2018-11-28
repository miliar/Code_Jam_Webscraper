#include <iostream>
#include<stdio.h>
using namespace std;
 
int main()
{
  int cases, max, a,min=0,no,i,peo=0;
  string s;                 
  scanf("%d",&cases); 
  for(int c=1; c<=cases; c++)
  {
    scanf("%d",&max);
    cin>>s;
    for(i=0;i<=max;i++)
    {	
    	if(peo<=i)
    	{
    		min = min+(i-peo);
    		peo = peo+(i-peo);	
    	}
    	peo=peo+((int(s[i]))-48);
    }
    printf("Case #%d: %d\n",c,min);
    min=0;
    peo=0;
  }
  return 0;
}
