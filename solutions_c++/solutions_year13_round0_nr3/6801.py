#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
int palin(int a)
{
if(a<9)
return 1;
 
int temp,reverse; 
reverse=0;
temp = a;
 
   while(temp!=0)
   {
      reverse = reverse*10;
      reverse = reverse+(temp%10);
      temp = temp/10;
   }
 
   if (reverse==a)
    {
    return 1;
    }
   else
   {
     return 0;
   }
    
}
 
int main()
{

ifstream ifile("e:/fairsquare.txt");
ofstream ofile("e:/fairans.txt");
    int t,a,b,i,cnt,j=1;
   ifile>>t;
    while(t--)
    {
        cnt=0;
        ifile>>a>>b;
        for(i=a;i<=b;i++)
        if((palin(i))&&(palin(sqrt(i)))&&(sqrt(i)-floor(sqrt(i))==0))
        cnt++;
        ofile<<"Case #"<<j<<": "<<cnt<<"\n";
        j++;
        
    }
    return 0;
}
