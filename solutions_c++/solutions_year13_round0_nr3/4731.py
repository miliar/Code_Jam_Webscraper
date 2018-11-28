#include<fstream>
#include<iostream>


using namespace std;
long long pow2(long long a)
{
    return (a*a);
}

long long rev(long long n)
{
      long long a,s=0;
      while(n)
      {
      a=n%10;
      n=n/10;
      s=(s*10)+a;
      }
      return s;
}
 
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    long long t,count=0,palc=0,j=0;
    long long power;
    long long a,b;
    
    long long arr[40]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001};
    
    /*for(int i=0;i<40;i++)
    cout<<i<<"="<<pow2(arr[i])<<endl;
    */
    fin>>t;
    while(t--)
    {
              count++;
              palc=0;
              fin>>a>>b;
              for(int i=0;i<40;i++)
              {
                      if(pow2(arr[i])>=a && pow2(arr[i])<=b)
                      palc++;
              }
              fout<<"Case #"<<count<<": "<<palc;
              fout<<endl;
    }
    return 0;
}
