#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include<fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    freopen("B-large.in","r",stdin);
     freopen("outputB.txt","w",stdout);

  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int in = 1; in <= t; ++in) {
    cin >> n;  // read n and then m.
    int ara[2505];
    int a;
    int max=0;
    for(int i=1;i<=2500;i++) ara[i]=0;
    for(int i=0;i<2*n-1;i++){
        for(int j=0;j<n;j++){
            cin>>a;
            ara[a]++;
            if(a>max) max=a;
        }
    }
    cout << "Case #" << in << ":";
    for(int i=1;i<=max;i++){
        if(ara[i]%2) {
            printf(" %d",i);
        }
    }
    cout<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  fclose(stdin);
  fclose(stdout);
}

