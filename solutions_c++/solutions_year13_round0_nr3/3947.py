#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX_NUM		150

int check(unsigned long long int orig)
{
  unsigned long reversed = 0, n = orig;

  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return orig == reversed;
}

int find(double begin, double end)
{
    long long int sB=(long long int)sqrt(begin);
    long long int sE=(long long int)sqrt(end);
    //cout<<sB<<" "<<sE<<endl;
    int count=0;
    for(long long int i=sB;i<=sE;i++)
    {
            if(check(i)==1&&check(i*i)==1&&i*i>=begin)
              {
                    count+=1;
                   // cout<<i<<"is right"<<endl;
              }
    }
    return count;
}



int main() {
//freopen("C-small-attempt2.in","r",stdin);
 //freopen("key.txt","w",stdout);
int T=0;
cin>>T;
	double begin;
    double end;
for(int i=1;i<=T;i++)
{
        
        cin>>begin>>end;
      // cout<<begin<<" "<<end<<endl;
        cout<<"Case #"<<i<<": "<<find(begin,end)<<endl;;
}

}
