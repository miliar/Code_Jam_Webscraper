#include<iostream>
#include<conio.h>
#include<math.h>
#include<fstream>
#include <string>
using namespace std;

int main()
{
   long long sum,a,b,c,rem,i,num,mum,count,t,p=0,x[20000];
   double xp;
   int k=1,l=2;
    string line[20000];
   ifstream myfile ("C.in");
   ofstream fout("D.out");
 
    while ( myfile )
    {
           myfile>>line[p];
       x[p]= atoi(line[p].c_str());
         p++;
    }
  
   t=x[0];
   for(int j=1;j<=t;j++)
   {
           count=0;
           
   a=x[k];
   b=x[l];
   for(i=a;i<=b;i++)
   {  
        xp=sqrt((double)i);
        if(i==(xp*xp))
        {       
                 sum=0;
                 num=i;
                 while(num!=0)
                 {
                            rem=num%10;
                            num=num/10;
                            sum=sum*10+rem;
                 }
                 if(i==sum)
                 {
                            sum=0;
                            mum= (double)xp;  
                            c=mum;     
                            while(mum!=0)
                            {
                                             rem=mum%10;
                                             mum=mum/10;
                                             sum=sum*10+rem;
                            }
                            if(c==sum)
                            {
                                          count++;
                            }
                  }
        
         } 
   }
   
   fout<<"Case #"<<j<<": "<<count<<"\n";
  

 
k=k+2;
l=l+2;
}
  
  myfile.close();
  fout.close();
  getch();
  return 0;
}
