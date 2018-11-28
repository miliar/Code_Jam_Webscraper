#include <string>
#include <iostream>

int a[10001];

int multab[3][8] = 
{
  { 1, 4, 7, 2, 5, 0, 3, 6 },
  { 2, 3, 4, 5, 6, 7, 0, 1 },
  { 3, 6, 1, 4, 7, 2, 5, 0 },
};

int main()
{
  int T;
  std::cin >> T;
  
  for (int t=1; t <= T; t++)
  {
    int L, X;
    std::cin >> L >> X;
    std::string s;
    std::cin >> s;
    
    int prod = 0;
    a[0] = prod;
    
    for (int x=0; x<X; x++)
      for (int l=0; l<L; l++)
        a[L*x + l + 1] = prod = multab[s[l]-'i'][prod];
        
    int possible = 0;
    if (a[L*X] == 4)
      for (int i=1; i<L*X; i++)
        if (a[i] == 1)
          for (int j=i+1; j<L*X; j++)
            if (a[j] == 3)
              possible = 1;
    std::cout << "Case #" << t << ": " << (possible ? "YES" : "NO") << std::endl;
  }
  return 0;
}
