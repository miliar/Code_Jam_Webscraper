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
unsigned long long n,t,k,q,r,n1,n2;
string s,st;
char c;
int arr[1001];
int main()
{
  cin>>n;
  for(int i=0;i<n;i++)
  {
    cin>>t;
    cin>>s;
    k=0;r=0;
    for(int j=0;j<=t;j++)
    {
      q=s.at(j)-'0';
      if(k>=j)
      {
        k+=q;
      }
      else
      {
        k++;r++;
        k+=q;
      }
    }
    cout<<"Case #"<<(i+1)<<": "<<r<<endl;
  }
  return 0; 
}