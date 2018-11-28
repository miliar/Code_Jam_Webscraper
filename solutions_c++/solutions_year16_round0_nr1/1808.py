// Example program

#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void sheep(int n);
int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    cout << "Case #" << i << ": " ;
    sheep(n);
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}

void sheep(int n){
    if(n==0) {
        cout<<"INSOMNIA"<<endl;
        return;
    }
    int flag = 1, i = 1, temp;
    vector<int> a(10);
    for(int j=0;j<10;j++)
        a[j]=0;
    while(flag!=0){
        temp = i*n;
        while(temp!=0){
            if(a[temp%10]==0)
                a[temp%10] = 1;
            temp = temp/10;
        }
        if ( std::find(a.begin(), a.end(), 0) == a.end()){
        flag = 0;
        cout<<i*n<<endl;
        return;
        }
        i++;
    }
    }
