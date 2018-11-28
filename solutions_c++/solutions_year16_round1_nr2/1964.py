#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <vector>
#include <map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t,N,temp;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  map<int,int> count;
  for (int i = 1; i <= t; ++i) {
    cin>>N;
    cout << "Case #" << i << ": " ;
    for (int j=1;j <= 2*N-1 ;++j)
        for(int k=1;k <= N; ++k){
        cin >> temp;  // read n and then m.
        ++count[temp];
        }
    int highest = count.rbegin()->first;     // key value of last element
    std::map<int,int>::iterator it = count.begin();
    do {
        if(it->second%2!=0)
         cout<<it->first<<" ";
    } while ( (*it++).first!= highest);
    cout<<endl;
    count.clear();
  }
  return 0;
}






