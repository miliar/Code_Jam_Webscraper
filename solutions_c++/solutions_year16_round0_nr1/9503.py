#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;
int main()
{   freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,t,a[10],stop=1,i,j,k,new_n;
    scanf("%d",&t);
    k=1;
    while(t--)
    { memset(a,0,sizeof(a));
      stop=1;
	  scanf("%d",&n);
      if(n==0)
        printf("Case #%d: INSOMNIA\n",k);
      else
	    { i=1;
	      j=0;
		  while(stop)
	      { new_n=i*n;
	        while(new_n)
	        { 
			    if(a[new_n%10]==0) 
	            { j++;
	              a[new_n%10]=1;
			    }
	            
	            if(j==10)
	            { stop=0;
	              break;
				}
				new_n=new_n/10;
			}
			i++;
		  }
		  
		  printf("Case #%d: %d\n",k,(--i)*n);
		}  
        k++;
        
	}
	 return 0;
}
	 
