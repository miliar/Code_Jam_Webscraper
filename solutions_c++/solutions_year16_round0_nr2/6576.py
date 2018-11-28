#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void maneuver(string& cakes, int start, int end)
{
  if (start != 0)
    return;
  
  if(end > cakes.length())
    return;
  
  if(start == end){
    cakes[start] = (cakes[start] == '+') ? '-' : '+';
    return;
  }
  
  string temp = cakes.substr(start, end + 1);
  auto reverse_itr = temp.rbegin();
  
  for (int i = 0 ; i < temp.length(); ++i) {
    cakes[i] = ((*reverse_itr) == '+') ? '-' : '+';
  }
}

int main()
{
  unsigned int cases;
  cin >> cases;

  for(auto c = 1 ; c <= cases ; ++c){
    
    string cakes{};
    cin >> cakes;
    
    int m{};
    
    while (true) {
      
      bool starts_with_happy = (cakes[0] == '+');
      bool flipped {false};
      
      if (cakes.length() == 1) {
        if (!starts_with_happy) {
          cakes[0] = '+';
          ++m;
        }
        
        break;
      }
      
      for (auto i = 1; i < cakes.length(); ++i) {
        
        if (starts_with_happy && cakes[i] != '+') {
          // flip from start ... i - 1
          maneuver(cakes, 0, i - 1);
          ++m;
          flipped = true;
          break;
        }
        else
          if (!starts_with_happy && cakes[i] == '+') {
            // flip from start ... i - 1
            maneuver(cakes, 0, i - 1);
            ++m;
            flipped = true;
            break;
          }
      } // end for
      
      if (flipped == false && starts_with_happy) {
        break;
      }
      else
        if (flipped == false && !starts_with_happy) {
          // flip from start to end
          maneuver(cakes, 0, cakes.length());
          ++m;
        }
    }; // end while
    
    cout << "Case #" << c << ": " << m << endl;
  }

  return 0;
}
