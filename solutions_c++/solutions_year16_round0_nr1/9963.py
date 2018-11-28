#include <iostream>
#include <fstream>
using namespace std;
int main() {
  long long t, n;
  ifstream fin {"A-large.in"};
  ofstream fout {"A-small.out"};
  int a[10];
  for(int j = 0; j < 10; ++j)
         a[j] = 0;
  fin >> t;
  int m;
  bool f = true;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    fin >> n;  // read n and then m.
    m = 1;
    f = true;
    int x;
    if(n == 0){
        fout << "Case #" << i << ": INSOMNIA\n";
        continue;
    }
    while(f) {
        x = n*m;
        m++;
        while(x){
            a[x%10] = 1;
            x /=10;
        }
        f = false;
        for(int j = 0; j < 10; ++j)
            if(a[j] == 0){
                f = true;
                break;
            }

    }
    fout << "Case #" << i << ": " << n*(m-1) << endl;
    for(int j = 0; j < 10; ++j)
            a[j] = 0;
  }
}
