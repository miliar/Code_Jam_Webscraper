#include <iostream>
using namespace std;
freopen("input_file_name.in","r",stdin);
freopen("output_file_name.out","w"stdout);
int main() {
	  int i,k,l,T,a[10],rem;
	  long int num,temp,N;
	  for(l=0;l<=9;l++)
	    a[l]=l;
	    cin>>T;
	  for(l=1;l<=T;l++)
	    {
	        i=2;
	        cin>>N;
	        num=temp=N;
	        if(N==0)
	     cout<<"\nCase #"<<l<<": "<<"INSOMNIA";
	    else
	    {
	        while(1)
	         {
	             while(temp != 0)
	               {
	                   rem=temp%10;
	                   switch(rem)
	                    {
	                        case 0: a[0]=-1;break;
	                        case 1: a[1]=-1;break;
	                        case 2: a[2]=-1;break;
	                        case 3: a[3]=-1;break;
	                        case 4: a[4]=-1;break;
	                        case 5: a[5]=-1;break;
	                        case 6: a[6]=-1;break;
	                        case 7: a[7]=-1;break;
	                        case 8: a[8]=-1;break;
	                        case 9: a[9]=-1;break;
	                    }
	                    temp=temp/10;
	               }
	               for(k=0;k<=9;k++)
	                  {
	                      if(a[k] != -1)
	                        break;
	                  }
	                  if(k==10)
	                  {
	                      for(k=0;k<=9;k++)
	                        a[k]=k;
	                       cout<<"\nCase #"<<l<<": "<<num;
	                       break;
	                  }
	            num=i*N;  
	            temp=num;
	            i++;
	         }
	    } 
	 }
	return 0;
}
