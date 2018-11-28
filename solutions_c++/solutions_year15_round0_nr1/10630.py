#include <iostream>
#include <fstream>
using namespace std;

main()

{
     int i,x,t,c=0,smax,k=0,sum=0;
    cin >>t;int s[t]; int n=t;
    while(t--)
    { cin>>smax;
    string a;
    cin >>a;
    for(i=0;i<t;i++)
        s[i]=0;

    for(i=0;i<smax+1;i++)
    {
       sum+=a[i]-'0';
       if((sum-1)<i)
       {
           c++;
           sum=sum++;
       }


    }
    s[k]=c;k++;c=0;sum=0;}

    for(i=0;i<n;i++)
   {

   cout<<"Case #"<<i+1<<":"<<" "<<s[i]<<endl;}

    return 0;}

