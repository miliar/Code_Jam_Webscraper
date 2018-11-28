#include <fstream>
#include<iostream>
#include<math.h>
using namespace std;
int ispal(int q)
{
    int temp=q,sum=0,r;
    while(q){
         r=q%10;
         q=q/10;
         sum=sum*10+r;
    }
    if(temp==sum)
        return 1;
    else
         return 0;

}
int main () {
   fstream fin,fout;
   int n,a,b,index,aa[100],ba[100],temp,k,count=0;
   float z;
   fout.open("fout.txt",ios::out);
   fin.open ("C-small-attempt0.in",ios::in);
   fin>>n;
    for(index=0;index<n;index++)
    {    count=0;
         fin>>a>>b;
         do{
            z= sqrt((float)(a));
            if (z ==(int)z)
            {   if(ispal(a)&&ispal(int(z)))
                {count++; }
            }
            a++;
           }while(a<=b);
           
          fout<<"Case #"<<index+1<<": "<<count<<"\n";
    }  
   fin.close();
   fout.close();
  return 0;
}
