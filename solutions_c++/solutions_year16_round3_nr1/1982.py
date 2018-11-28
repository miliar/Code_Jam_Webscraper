#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

typedef unsigned long long BigInt;

vector<BigInt> P;
vector<char> Name;
BigInt senators_left;

bool not_majority(int i)
{
     double half_senators = (senators_left-1)/2.0;
     for (int j=0;j<P.size();j++){
         if (j==i) continue;
         if (P[j] > half_senators) return false;
     }
     return true;
}

bool not_majority(int i1, int i2)
{
     double half_senators = (senators_left-2)/2.0;
     for (int j=0;j<P.size();j++){
         if (j==i1 || j==i2) continue;
         if (P[j] > half_senators) return false;
     }
     return true;
}

bool  remove_two(string &s)
{
     for (int i1=0;i1<P.size();i1++){
         if (P[i1]>0){
            for (int i2=i1+1;i2<P.size();i2++){
                if (P[i2]>0 && not_majority(i1,i2)){
                   P[i1]--;
                   P[i2]--;
                   senators_left -= 2;
                   s = "ab";
                   s[0] = Name[i1];
                   s[1] = Name[i2];
                   return true;
                }
            }
         }
     }
     return false; 
}

bool remove_one(string &s)
{
     for (int i=0;i<P.size();i++){
         if (P[i]>0 && not_majority(i)){
            P[i]--;
            senators_left--;
            s = " ";
            s[0] = Name[i];
            return true;
         }
     }
     return false;
}

int main()
{
  BigInt T, N;
  
  cin >> T;
  
  for (BigInt c=1;c<=T;c++){
      cin >> N;
      senators_left = 0;
      cout << "Case #" << c << ": ";
      
      P = vector<BigInt>(N);
      Name = vector<char>(N);
      for (BigInt i=0;i<N;i++){
          cin >> P[i];
          senators_left += P[i];
          Name[i] = 'A'+i;
      }
      
      string s;
      while (senators_left){
            if (!remove_two(s)){
               if (!remove_one(s)){
                  cout << "Error!\n";
               }else cout << s << " ";
            }else cout << s << " ";      
      }
      
      cout << endl; 
  }
  return 0;
}
