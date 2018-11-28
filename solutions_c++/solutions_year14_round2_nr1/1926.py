#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("iinp.txt", "r", stdin);
	freopen("k.txt", "w", stdout);
	scanf("%d\n",&t);
	for(int tc = 1; tc <= t; tc++){
		printf("Case #%d: ", tc);
	    int n;char ta,tb; int tan=1, tbn=1;
	    int check=0,flag=0,res=0,suck=0;
	    scanf("%d",&n);
	    char a[101],b[101];
	    scanf("%s",a);
	    
	    scanf("%s",b);
	   // printf(" \n String a is : %s\n",a);
	    //	    printf(" \n String b is : %s\n",b);
	    for(int i=0,j=0; (a[i]!=0 || b[j]!=0); )
	     {
                if( a[i]== a[i+1]) 
                { i++; tan++; check=0;}
                else {ta=a[i]; check=1;}
                if(b[j] ==b[j+1])
                {j++; tbn++; flag=0;}
                else {tb=b[j];flag=1;}
                if(check && flag)
                { if( ta !=tb)
                   { res = 0; suck =1;break;}
                   else
                   { res += tbn>tan?(tbn-tan):(tan-tbn) ;   i++;j++; tan=tbn=1; }
                }
          }
          if(res==0 && suck)
           printf("Fegla Won\n");
           else
           printf("%d\n",res);
           }
	return 0;
}
			
