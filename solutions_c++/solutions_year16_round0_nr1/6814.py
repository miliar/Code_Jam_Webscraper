#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include<fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    freopen("A-large.in","r",stdin);
     freopen("outputA.txt","w",stdout);

  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int in = 1; in <= t; ++in) {

    cin >> n ;  // read n and then m.
    if(n==0){
          cout << "Case #" << in << ": INSOMNIA"  << endl;
    }
    else{
        int ara[10];
        for(int i=0;i<10;i++) ara[i]=0;
        bool flag=true;
        int i=0;
        while(flag){
            i++;
            long int a=n*i;
            while(a){
                ara[a%10]=1;
                a=a/10;
            }
            flag=false;
            for(int j=0;j<10;j++){
                if(ara[j]==0){
                    flag=true;
                    break;
                }
            }
        }
          cout << "Case #" << in << ": " << n*i << endl;
    }

    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  fclose(stdin);
  fclose(stdout);
}

