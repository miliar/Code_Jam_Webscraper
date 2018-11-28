#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;
int main()
{   freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);  
  int n,i,t,k=1,p[27],m,big1,big2,big1index,big2index,temp,diff;
  scanf("%d",&t);
  while(t--)
  { scanf("%d",&n);
    m=n;
    scanf("%d%d",&p[1],&p[2]);
    big1 = p[1];
    big2 = p[2];
    big1index=1;
    big2index=2;
    if (big1 < big2)
    {
        temp = big1;
        big1 = big2;
        big2 = temp;
        big1index=2;
        big2index=1;
    }
    
    for (i = 3; i <=m;	i++)
    {   scanf("%d",&p[i]);
        if (p[i] >= big1)
        {
            big2 = big1;
            big2index=big1index;
            big1 = p[i];
            big1index=i;
        }
        else if (p[i] > big2)
        {
            big2 = p[i];
            big2index=i;
        }
    }
    printf("Case #%d:",k);
    k++;
    diff=big1-big2;
    if(diff%2==1)
     {
	   printf(" %c",big1index+64);
	   diff--;
     }
   
    while(diff)
    { printf(" %c%c",big1index+64,big1index+64);
      diff-=2;
	}
	p[big1index]=p[big2index];
	for(i=1;i<=m;i++)
	{ if(i==big1index || i== big2index)
	    continue;
	  if(p[i]%2==1)
      { 
	    printf(" %c",i+64); 
		p[i]--;
	  }
     while(p[i])
     {  printf(" %c%c",i+64,i+64); 
		p[i]-=2;
	 }
	 
	}
	
	diff=p[big1index];
	
    while(diff)
    { printf(" %c%c",big1index+64,big2index+64);
      diff--;
	}
	printf("\n");
  }
  return 0;
}
