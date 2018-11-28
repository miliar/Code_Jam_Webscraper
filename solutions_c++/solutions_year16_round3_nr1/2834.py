#include<iostream>
using namespace std;
int main()
{ int t,k;
 cin>>t;
 for(k=1;k<=t;k++)
 {  int n,j,a[10000]={0},tot=0,i,si,li,l,s;
    cin>>n;
    for(i=1;i<=n;i++)
      { cin>>a[i];
        tot+=a[i];
     } 
      char ch,ch1;
      cout<<"Case "<<"#"<<k<<": ";
      while(tot)
	  { //cout<<tot<<" ";
	    l=0; s=0; li=0; si=0;
	    for(i=1;i<=n;i++)
	     { if(a[i]>l)
	        { l=a[i];
	          li=i;
	         } 
	     }
	     for(i=1;i<=n;i++)
	     { if(a[i]>s && i!=li)
	          { s=a[i]; 
	            si=i;
	          }
	      }
	    
	   a[si]--; a[li]--;
	   if(tot==3)
	    {  if(l==1 &&s==1)
	        { cout<<char(64+li)<<" ";
	            a[si]++;
	             tot--;
	             continue;
	        }
	    }
     if(li>=1)
      { tot--;
         li+=64;
         ch=li; 
         cout<<ch;
      }
      if(si>=1)
       { tot--; 
       si+=64;
       //cout<<" "<<si;
         ch1=si;
          cout<<ch1<<" ";
       }
   }
   cout<<endl;
}
}
   
		     
	     
      
 