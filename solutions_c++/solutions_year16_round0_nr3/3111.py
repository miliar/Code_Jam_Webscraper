#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

long long n,j,cc;


long long base(vector<long long> a,long long b)
{
    long long sk,mu;
    mu=b;
    sk=1;
      for(int i=0;i<a.size();i++)
      {
          if(a[i]==1)sk+=mu;
          mu*=b;
      }
      sk+=mu;
      return sk;
}
int prime(long long sk)
{
    for(long long i=2;i<=sqrt(sk);i++)
    {
        if(sk%i==0)return i;
    }
    return -1;

}
   ifstream in("in.txt");
    ofstream out("out.txt");

void create(vector<long long> s)
{
    if(s.size()==n-2)
    {
        if(cc<j)
        {
        long long sk;bool ar=true;long long pr;vector<long long> ats;
        for(int k=2;k<=10;k++)
        {
            sk=base(s,k);
            pr=prime(sk);
            if(pr==-1)ar=false;
            else ats.push_back(pr);
        }
        if(ar)
        {
            out<<1;
             for(int i=s.size()-1;i>=0;i--)out<<s[i];out<<1;out<<" ";
            cc++;
            //for(int k=2;k<=10;k++)cout<<base(s,k)<<" ";cout<<endl;

             for(int i=0;i<ats.size();i++)out<<ats[i]<<" ";out<<endl;
        }
    }
    }
    else
    {
        s.push_back(1);
        create(s);
        s.pop_back();
        s.push_back(0);
        create(s);
    }
}

int main()
{
    int t;

    cin>>n>>j;
    out<<"Case #1:"<<endl;
    vector<long long> s;
    create(s);
    return 0;
}
