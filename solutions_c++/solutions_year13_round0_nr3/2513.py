#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int checknum(string x,string y,string z)
{
    
    int lx,ly,lz,fa=0,fb=0;
    lx=x.length();
    ly=y.length();
    lz=z.length();
    if((lx>ly) || (lx==ly && x>=y))
    fa=1;
    if((lx<lz) || (lx==lz && x<=z))
    fb=1;
    if(fa==1 && fb==1)
    return 1;
    else
    return 0;
    }



int main()
{
int t,c,i,count=1,p=0;
string r,b;
string arr[39] = { "1","4","9","121","484","10201","12321","14641","40804","44944","1002001",
"1234321","4008004","100020001","102030201","104060401","121242121","123454321","125686521",
"400080004","404090404","10000200001","10221412201","12102420121","12345654321","40000800004",
"1000002000001","1002003002001","1004006004001","1020304030201","1022325232201","1024348434201",
"1210024200121","1212225222121","1214428244121","1232346432321","1234567654321","4000008000004","4004009004004"};
cin>>t;
while(t--)
{
    cin>>r>>b;
    c=0;
    for(i=0;i<39;i++)
    {
                     p=0;
      p=checknum(arr[i],r,b);            
    if(p == 1)
    c++;   
}
    cout<<"Case #"<<count++<<": "<<c<<endl;   
          }
return 0;
}
