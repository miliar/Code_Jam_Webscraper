#include<iostream>
#include <fstream>
#include<math.h>
using namespace std;
int main(){
    int num,r,sum,temp;
    int min,max,m,n;
    float p;int count=0;
 ifstream myfile;
  myfile.open ("C-small-attempt0.in");
  ofstream fileout("fileout.txt");
  myfile>>n;
  for(int j=1;j<=n;j++)
  {count=0;
   
    myfile>> min;

    
    myfile>>  max;

    for(num=min;num<=max;num++){
         temp=num;
         sum=0;

         while(temp){
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
         }
         if(num==sum)
            { 
				p=sqrt(num);
       		m=p;
       		if(m==p)
			{
				
         temp=m;
         sum=0;

         while(temp){
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
         }
         if(m==sum)
         {
         	count++;
         }
				
				
			
			
			
			
			}
    }}
    fileout<<"Case #"<<j<<": "<<count<<"\n";
}myfile.close();
  fileout.close();
    return 0;
}

