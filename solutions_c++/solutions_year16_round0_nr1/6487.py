#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

using namespace std;

int main()
{
  unsigned int cases;
  cin >> cases;

  for(auto c = 1 ; c <= cases ; ++c){
    
    long n{};
    cin >> n;
    
    auto orignal_n = n;
      
    long last_n { -1 };
    long i { 2 };
    bitset<10> mask { 0 };
    
    while (true) {
      
      if (last_n == n) {
        cout << "Case #" << c << ": " << "INSOMNIA" << endl;
        break;
      }
      
      long remaining { n };
      bool quit { false };
      
      while (remaining != 0) {
        
        auto digit = remaining % 10;
        
        mask.set(digit, 1);
        
        if(mask.count() == 10)
        {
          cout << "Case #" << c << ": " << n << endl;
          quit = true;
          break;
        }
        
        remaining /= 10;
      };
      
      if(quit)
        break;
      
      last_n = n;
      n = orignal_n * i++;
    }
  }

  return 0;
}
