//In the Name of God
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;
typedef long long LL;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

LL t , n , cur , cur1 , ans , ted , T = 1;
string s;

bool f(LL k){
  if(s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' || s[k] == 'u')
    return true;
  return false;
}

int main(){
  fin >> t;
  while(t--){
    ans = ted = 0;
    cur = cur1 = -1;
    fin >> s >> n;
    for(LL i = 0 ; i < s.size() ; i++){
      if(f(i)){
	ted = 0;
	cur1 = -1;
      }
      else{
	if(cur1 == -1)
	  cur1 = i;
	ted++;
	if(ted == n)
	  cur = cur1;
	else if(ted > n){
	  cur++;
	  cur1++;
	}
      }
      ans += cur + 1;
    }
    fout << "Case #" << T << ": " << ans << endl;
    T++;
  }
  return 0;
}
