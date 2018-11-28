#include<iostream>
#include<vector>
using namespace std;
long long int v[]={1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
int main()
{
    long long int t,a,b;
    cin>>t;
    static int test=1;
    while(t--)
    {
              cin>>a>>b;
              int ctr=0;
              for(int i=0;i<39;i++)
              {
                      if((v[i]*v[i])>=a && (v[i]*v[i])<=b)ctr++;
              }
              cout<<"Case #"<<test++<<": "<<ctr<<endl;
    }
}

              
              
              
