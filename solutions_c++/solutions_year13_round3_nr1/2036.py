#include <iostream>

using namespace std;

inline
bool isConsonant(char l)
{
  return !(l == 'a' || l == 'e' || l == 'i' || l == 'o' || l == 'u');
}

int main()
{
  int T, i, j, cons, n, prev;
  long long int substr_n, length;
  char letter;
  string name;

  cin >> T;
  
  for (int t = 0; t < T; ++t) {

    cons = 0;
    i = 0;
    substr_n = 0;
    prev = 0;
    cin >> name;
    length = name.length();
    cin >> n;

    while (name[i] != 0) {
      
      letter = name[i];
      
      if (isConsonant(letter)) {
	
	if (cons++ == 0) {
	  j = i;
	}
	if (cons == n) {
	  substr_n += (j - prev + 1) * (length - i);
	  prev = ++j;
	  --cons;
	}
	
      } else {
	cons = 0;
      }
      
      ++i;  
    }
    
    cout << "Case #" << t + 1 << ": " << substr_n << endl;
    
  }
  
}