#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("C-smallN.in", "r", stdin);
	freopen("op.txt", "w", stdout);
	scanf("%d\n",&t);
	int square[5]= {1,4,9,121,484};
	for(int tc = 1; tc <= t; tc++)
    { 
        int a,b;
        int la=-1, lb=-1;
		printf("Case #%d: ", tc);
	    scanf("%d %d\n", &a, &b);
	    //printf(" %d %d \n",a,b);
	    for(int i=0; i<5; i++)
	    { if( square[i]>=a )
	      { la = i;  break; }
        }
        for(int i=0; i<5; i++)
	    { if( square[i]<=b )
	       lb = i;  
        }
        //printf("\n value of la and lb is %d  and %d \n",la,lb);
      if(la==-1 || la>lb )
      printf("0\n");
      else
      printf("%d\n",lb-la+1);
     }
	  
      return 0;
}
			
