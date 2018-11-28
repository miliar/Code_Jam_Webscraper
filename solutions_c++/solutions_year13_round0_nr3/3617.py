#include<iostream>
#include<stdio.h>
using namespace std;
unsigned long long int arr[39]={
 /*1 digit*/      1, 4, 9,
 /*3 digit*/      121, 484,
 /*5 digit*/      10201, 12321, 14641, 40804, 44944,
 /*7 digit*/      1002001,1234321, 4008004,
 /*9 digit*/      100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404,
 /*11 digit*/     100002000, 102214122, 121024201, 123456543, 400008000,
 /*13 digit*/     100000200, 100200300, 100400600, 102030403, 102232523, 102434843,
                  121002420, 121222522, 121442824, 123234643, 123456765, 400000800, 400400900};
unsigned long long int a1[18]={01,01,21,21,04,0001,2001,4001,0201,2201,4201,0121,2121,4121,2321,4321,0004,4004};
unsigned long long int a,b,t,c,i,k=1;
unsigned long long int a2[39];
int comp(unsigned long long int, int);
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
     for(i=0;i<39;i++)
     {
                        if(i<21)
                        a2[i]=arr[i];
                        else if(i>=21 &&i<26)
                             a2[i]=arr[i]*100+a1[i-21];
                        else if(i>=26)
                             a2[i]=arr[i]*10000+a1[i-21];
                             }
  //  for(i=0;i<39;i++)
  //                   cout<<a2[i]<<endl;
    cin>>t;
    cin.ignore();
    do
    {
        cin>>a>>b;
        c=0;
        for(i=0;i<39;i++)
        {
                    if(a2[i]>=a && a2[i]<=b)
                    c++;
        }
                cout<<"Case #"<<k<<": "<<c<<"\n";
    }while(k++!=t);
    return 0;
}
