#include<iostream>
using namespace std; 
typedef long long int ll;

int main()
{ freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
 ll k,t;
 cin>>t;
 for(k=1;k<=t;k++)
 {ll n,total=0,temp,temp2,rem,count[10]={0},i=1;
 cin>>n; 
 cout<<"Case #"<<k<<": ";
 if(n==0)
 {cout<<"INSOMNIA";}
 else
 {
 while(true)
 {temp=i*n;
  temp2=temp;
  while(temp!=0)
  {rem=temp%10;
   temp=temp/10;
   count[rem]++;
   if(count[rem]==1)
   {total++;
   if(total==10)
   {cout<<temp2;
   goto end;
   }
   }
  }
  i++;
 }
 
 }
end:
	cout<<endl;
 
 }
return 0;
}
