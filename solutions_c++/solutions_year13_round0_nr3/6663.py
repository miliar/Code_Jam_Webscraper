#include<iostream.h>
#include<math.h>
#include<fstream.h>
#include<conio.h>
 void main()
 {clrscr();
  int t,a,b,i=0,j=0,k,l,n,ans,count=0;
  float f;
  ifstream fin("input.txt");
  ofstream fout("output2.txt");
  fin>>t;
  for(n=0;n<t;n++)
   {
    count=0;
   fin>>a>>b;
      for(i=a;i<=b;i++)
	    {f=sqrt(i);
	     ans=f;
	     if(!(f-ans))
		 { if(i<10)
		      {count+=1;
		      }
		   if(i>10&&i<100)
		       {k=i/10;
			j=(i%10)*10+k;
		       }
		   if(i>100)
		       {k=i/100;
			j=(i%100)+k*100;
		       }
		   if(j==i)
		      {if(ans>10&&ans<100)
			   {k=ans/10;
			    l=(ans%10)*10+k;
			    }

		       if(l==ans)
			  {count+=1;
			  }
		      }
		  }

	     }
   fout<<"Case #"<<n+1<<": "<<count<<"\n";
	     }
}






