#include<iostream>
#include<string>
#include<cmath>
#include<fstream>
using namespace std;

int fair(int l)
{
 int m=0,c=l;
 while(c>0)
 {
           m *= 10;
           m += c%10;
           c /= 10;
 }
 if(m == l)
 {
  return(1);
 }
 else
 {
  return(0);
 }
}
           
           

int square(int c)
{
 int t1;
 t1=(int)sqrt(c);
 if((t1*t1)==c)
 {
  int temp2=fair(t1);
  return(temp2);
 }
 else
 {
  return(0);
 } 
}
int main()
{
 int T,l,h,t=0,count=0,size;
 ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("result.txt");
 fin>>T;
 while(t<T)
 {
   fin>>l>>h;
   size=h-l+1;
   for(int k=l;k<=h;k++)
   {
           if(fair(k) && square(k))
           {
                      ++count;
           }
           
                      
    
             
    
   }
   int temp=t+1;
   fout<<"Case #"<<temp<<": "<<count<<"\n";
   count=0;
   ++t;
  }
  fout.close();
  return(0);
}
