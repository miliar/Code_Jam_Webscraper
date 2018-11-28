#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define lli long long int

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
	freopen("outd0.txt","w",stdout);
	lli t,x,r,c,flag,k=1;
	cin>>t;
	while(t--)
	{
              cin>>x>>r>>c;
              flag=1;
              
              
              if((r*c)%(x)!=0){flag=0;//cout<<"1"<<(r*c)%(x);
              cout<<"Case #"<<k<<": RICHARD\n";}
              if((x>=3 && (r<2 || c<2)) && flag){flag=0;//cout<<"2"<<r<<c;
               cout<<"Case #"<<k<<": RICHARD\n";}
              if(((x==2 ) && (r*c)%2!=0) &&flag){flag=0;//cout<<"3"<<(r*c)%2;
               cout<<"Case #"<<k<<": RICHARD\n";}
              if((x==4) && (r*c)%4!=0 && flag){flag=0;//cout<<"4"<<(r*c)%4;
               cout<<"Case #"<<k<<": RICHARD\n";}
              if((x==4 && (r<3 || c<3)) && flag){flag=0;//cout<<"2"<<r<<c;
               cout<<"Case #"<<k<<": RICHARD\n";}
              else if(flag)
              cout<<"Case #"<<k<<": GABRIEL\n"; 
              k++;
    }
    
    return 0;
}
