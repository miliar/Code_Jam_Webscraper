#include<iostream>
#include<fstream>
using namespace std;

fstream f1,f2;
int main()
{char c;
     int a,b,f,count=0,i,cas,u=0;
    f1.open("C-small-attempt7.in",ios::in);
    f2.open("out.out",ios::out);
    f1>>cas;
    while(f1)
    {
    count=0;

        f1>>a;
        f1.get(c);
        f1>>b;
        for(i=a;i<=b;i++)
        {
         if(i==1||i==4||i==9||i==121||i==484)
        count++;
         }

if(u<cas)
    {


 f2<<"Case #"<<u+1;
 f2<<": ";
 f2<<count;
 f2<<"\n";
 u++;
    }
}
f1.close();
f2.close();
return 0;
}
