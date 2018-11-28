
#include <string.h>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <unordered_set>
#include <thread>
#include <mutex>
#include <future>

using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   int tst;
   cin >> tst;
   for(int t = 1; t<=tst; t++){

       printf("Case #%d:",t);
       int n;
       cin >> n;
       // if(t == 18) cout << n << "\n";
       priority_queue<pair<int,char> > q;
       char c = 'A';
       int sum = 0;
       int x;
       for(int i = 0; i < n; i++,c++){

           cin >> x;
           // if(t == 18) cout << x << " ";
           sum += x;
           q.emplace(x,c);
       }
       while(q.size()){
           pair<int,int> p = q.top();
           q.pop();
           string s;
           s += p.second;
           p.first--;
           sum--;
           if(q.size()){
            pair<int,int> p2 = q.top();
            if(p2.first * 2 > sum) {
                s += p2.second;
                p2.first--;
                sum--;
                q.pop();
                if(p2.first) q.push(p2);
            }
           }
           if(p.first)
               q.push(p);
           printf(" %s",s.c_str());
       }
       printf("\n");
   }
    return 0;
}