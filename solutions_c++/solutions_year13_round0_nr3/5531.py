#include<iostream>
using namespace std;
int check(int);
int main()
{    
int r=1,l=0,u,t,c,d,z,f=1,count;
cin>>t;
while(t!=0)
{
cin>>c;
cin>>d;
count=0;
r=0;
while((r*r)<c) 
r++;
while((r*r)<=d){
           u=check(r*r);
            if(u==1)
            {
            if(z=check(r)==1)
            count++;
            }
r++;
l++;    
}
cout<<"Case #"<<f<<": "<<count<<"\n";
f++;
t--;
}
return 0;
}

int check(int num)
{    
     int n, digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if (n == rev)
     return 1;
     else
     return 0;
}    


