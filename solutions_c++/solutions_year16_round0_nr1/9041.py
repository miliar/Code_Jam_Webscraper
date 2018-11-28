#include<bits/stdc++.h>
#define ll long long int
using namespace std;

set<int>s;
int digit(ll n)
{
    ll temp=n,r=0;
    while(temp!=0)
    {
        r=temp%10;
        s.insert(r);
        temp/=10;
    }
}

int main()
{
    freopen("input2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int test;
    cin >> test;
    for(int k=1;k<=test;k++)
    {
      ll n,i=1,last=0;
      cin >> n;
      if(n==0)
        cout << "Case #" << k << ": " << "INSOMNIA" << endl;
      else{
      while(s.size()!=10)
      {
          last=i*n;
          digit(last);
          i++;
      }
      cout << "Case #" << k << ": " << last << endl;

      }
      s.clear();
    }



}
