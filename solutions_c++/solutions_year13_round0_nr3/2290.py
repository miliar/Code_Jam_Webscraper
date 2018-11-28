#include<iostream>
#include<vector>
using namespace std;
#define MAX 10000000
vector<long long> list;
bool isPalindrome(long long  x) {
  if (x < 0) return false;
  long long div = 1;
  while (x / div >= 10) {
    div *= 10;
  }       
  while (x != 0) {
    long long l = x / div;
    long long r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}
void init()
{
for(long long i =1;i<=MAX;i++)
{

if(isPalindrome(i) && isPalindrome(i*i))
 list.push_back(i*i);

}

}
int main()
{
int test,t=1;
long long l,r;
cin>>test;
init();
while(t<=test)
{
cin >> l>> r;
int i;
int sz = list.size();
for( i =0;i<sz;i++)
{
if( list[i] >=l)
  break;
}
int count = 0;
for(int j =i;j<sz;j++)
{
//cout << list[j]<<" ";
 if(list[j] <= r)
  count++;
  
}
cout <<"Case #"<<t<<": ";
cout << count <<endl;
t++;
}
return 0;
}
