// sort algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector

using namespace std;
int main () {
  int test;
  cin>>test;
  int i=1;
while(i<=test){
  cout<< "Case #"<<i<<": ";
  int n;
  cin>>n;
  int sum=0;
  string temps;
  cin>>temps;
  int ans=0;
  for(int j=0;j<=n;j++)
{
  if(temps[j] != '0'){
    if(sum<j){
      ans+= j-sum;
      sum =j;
    }

  sum += temps[j]-'0';
}

}

 i++;
 cout << ans<<endl;

}
  return 0;
}
