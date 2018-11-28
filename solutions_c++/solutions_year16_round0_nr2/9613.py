#include<stdio.h>
#include <bits/stdc++.h>
#include<string.h>
using namespace std;
int main()
{   freopen("a.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,t,stop=1,change,curr_char,prev_char,k,last_char,length,i;
    char a[100];
    scanf("%d",&t);
    k=1;
    while(t--)
    { change=0;
	  scanf("%s",a);
	  prev_char=a[0];
	  length=(unsigned)strlen(a);
	  for(i=1;i<length;i++)
	  { if(a[i]!=prev_char)
	    { change++;
	      prev_char=a[i];
		}
		
	  }
	  if(a[length-1]==43)
	    change--;
	  printf("Case #%d: %d\n",k,change+1);
	  k++;  
      
	}
	return 0;
}
