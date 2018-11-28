#include <bits/stdc++.h>
#include<math.h>
using namespace std;
int main()
{   freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    long long int n,t,i,a[50][16],con[11],b[]={1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},div[11],l,u,j,o,q,m;
    t=50;
    while(t--)
    { //printf("ttttttttt=%d\n",t);
      memset(div,0,sizeof(div));
	  n=0;
      l=2;
	  u=15;  
	  for(j=2;j<=10;j++)
	  { n=0;
	   //printf("j=%d\n",j); 	
	  u=15;	
	  //printf("aaaa1\n");
	  for(i=0;i<16;i++)
        { 
		  o=pow(j,i);
          //u++;
          n=n+o*b[u];
          u--;
        }
       con[j]=n;
       //printf("con[%lld]=%lld\n",j,con[j]);
      //printf("aaaa2\n");
      for(i=2;i<=con[j]/2;i++)
	  { 
	    q=0;
	    if(i==100000)
	      break;
	    if(con[j]%i==0)
	    {  //printf("i=%lld",i);
		    div[j]=i;
		    break;
	      
		}
	  } 
	   //printf("\nccccccc1\n");
	   if(div[j]!=0 && j==10)
	   {
	     
		 j=1;  
		 break;  
		 
	   }
       
       //printf("\nccccccc2\n");
       if(div[j]==0)
	   {
	     i=14;
	     while(b[i]==1)
	       i--;
	     b[i]=1;
		 for(i++;i<15;i++)
		   b[i]=0;
		 memset(div,0,sizeof(div));
	     n=0;  
		 j=1;    
	   }  
	   //printf("j complete");
     }
     
	 for(i=0;i<16;i++)
	   printf("%lld",b[i]); 
	 for(i=2;i<=10;i++)
	   printf(" %lld",div[i]);  
	 printf("\n");
	 i=14;
	     while(b[i]==1)
	       i--;
	     b[i]=1;
		 for(i++;i<15;i++)
		   b[i]=0;
	}
	
	return 0;
}
/*
for(j=3;j<11;j++)
     {  o=j-1;
       for(i=2;i<=con[j]/2;i++)
       { if(con[j]%i==0)
          {  printf("qqqqqqq");
		     for(;o>=2;o--)
              if(i==div[o])
                 { //div[j]=0;
                   printf("aaaaaa");
                   break;
				 }
            if(o==1)
              div[j]=i;
			       
		  }
	   }
     }
*/
