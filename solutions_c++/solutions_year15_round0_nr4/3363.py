#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
//#define max 100
using namespace std;
//int numb=0;
//int max=0;
unsigned long long n,t,k,q,r,n1,n2,x;
string s,st;
char c;
int arr[100000];
int main()
{
  cin>>n;
  for(int i=0;i<n;i++)
  {
    cin>>t>>x>>k;
    cout<<"Case #"<<(i+1)<<": ";
    if(t>=7||((t+1)/2)>min(x,k)||(x*k)%t!=0||t>max(x,k))
      cout<<"RICHARD";
    else
    {
      if((t==3&&(min(x,k)<2||max(x,k)<3))||(t==4&&(min(x,k)<3||max(x,k)<4))||(t==5&&(min(x,k)<3||max(x,k)<5))||(t==6&&(min(x,k)<3||max(x,k)<5))||(t==6&&(min(x,k)<4||max(x,k)<6)))
        cout<<"RICHARD";
      else
        cout<<"GABRIEL";
    }
    cout<<endl;
  }
  return 0; 
}