#include<iostream>
using  namespace std;
#include<stdlib.h>
#include<stdio.h>
int compare(const void *a, const void *b)
 {if ((*(double *) a)-*((double *) b)<0) return -1;
  return 1;
 }
double a[1000005],b[1000006];
int main()
 {int t,n,k,i,j;
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
 cin>>t;

 for(k=1;k<=t;k++)
   {  int normal=0, abnormal=0;
   	  cin>>n;
   	  
   	  for(i=0;i<n;i++)
   	    cin>>a[i];
   	  for(i=0;i<n;i++)
   	    cin>>b[i];
   	  qsort(a,n,sizeof(double),compare);
   	  qsort(b,n,sizeof(double),compare);
      j=0;
	  for(i=0;i<n;i++)
  		  {while(j<n && b[j]<a[i])
  		     {normal++;
  		      j++;
  		     }
  		     j++;
  		  }
  	  for(i=0,j=0;i<n;i++)
  	    {if(a[i]>b[j])
  	       {j++;
  	       abnormal++;
  	      }
  	     
  	       
  	    }
  	  
   	 cout<<"Case #"<<k<<": "<<abnormal<<" "<<normal<<endl;;
   }
 
 
}
