#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;

ifstream in("C-large-1.in"); ofstream out("C.out");

bool flag = false;
long long A, B;
string s;
int N, result, l=1;


bool isPalindrome(long long l) {
    string s; stringstream st; st<<l; s = st.str();    
    return(s==string(s.rbegin(),s.rend()));
    }

int main()
{
    in>>N;
    set<long long> pal;
    for(long long i = 1LL; i<=2001002; i++)
             {
                  if(isPalindrome(i))
                  { 
                  if(isPalindrome(i*i)) pal.insert(i*i);
                  }
            }
               
    while(N--)
    {
          if(flag) out<<endl; flag = true;
          in>>A>>B;
          result = distance(pal.lower_bound(A), pal.lower_bound(B));
          if(pal.count(B)) result++;
          out<<"Case #"<<l<<": "<<result;
          l++;
              
              }
    
    
    }
