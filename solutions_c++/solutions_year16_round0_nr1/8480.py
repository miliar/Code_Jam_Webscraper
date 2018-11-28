#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
typedef int MyInt;
void getNum(int n, std::set<int>& temp) {
  while (n>0) {
        temp.insert(n%10);
        n = n/10;
   }
}


void solve() {
  int num;
  std::cin >> num;
  if (num != 0) {
	  std::set<int> uList;
	  int i = 0;
	  while(uList.size()!=10) {
	   	getNum((i+1) * num, uList);   	
	   	i++;
	  }
	  std::cout << i * num << std::endl;  
  }  
  else {
  	std::cout << "INSOMNIA" << std::endl;
  }
}

int main() {
  int tn;
  std::cin >> tn;
  forn(t, tn) {
    std::cout << "Case #" << t + 1 << ": ";
    solve();
  }
	
  return 0;
}


