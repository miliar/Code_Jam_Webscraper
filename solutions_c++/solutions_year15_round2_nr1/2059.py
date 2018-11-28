#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <cmath>
#include <deque>
using namespace std;
int rev(int a) {
     int b=0;
     while(a>0) {
                b=b*10+a%10;
                a/=10;
                }
                return b;
                }
int main() {
    ifstream fin("A-small-attempt4.in");
    ofstream fout("output.txt");
    vector<int> v(100000000, 99999);
    v[1]=1;
    for(int i=1; i<=1000000; i++) {
            v[i+1]=min(v[i+1], v[i]+1);
            v[rev(i)]=min(v[rev(i)], v[i]+1);
            }
    int t;
    fin >> t;
    for(int i=0; i<t; i++) {
            long long n;
            fin >> n;
            fout << "Case #" << i+1 << ": " << v[n] << endl;
            }
    return 0;
}
