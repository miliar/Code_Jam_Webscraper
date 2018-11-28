#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include<fstream>
#include<cstring>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
char str[105];
char sign[2];
int pancake(int index, int charindex){
    int move=0;
    for(int i=index;i>=0;i--){
        if(str[i]!=sign[charindex]){
            move=1+pancake(i-1,(charindex+1)%2);
            break;
        }

    }
    return move;
}
int main() {
    freopen("B-large.in","r",stdin);
     freopen("outputB.txt","w",stdout);
    sign[0]='+';
    sign[1]='-';
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> str;  // read n and then m.
    int len=strlen(str);
    int ans=pancake(len-1,0);
    cout << "Case #" << i << ": " << ans << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  fclose(stdin);
  fclose(stdout);
}

