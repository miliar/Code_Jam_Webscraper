#include <iostream>

using namespace std;

int *compute(int k, int c, int s)
{
  int *output = new int[k];
  output[0] = 0;
  
  if (c == 1) {
    if (s < k) {
      return output;
    }
    for (int i=0;i<k;i++){
      output[i] = i+1;
    }
    return output;
  }
  
  if (s < k-1) {
    return output;
  }
  
  if (k == 1) {
    output[0] = 1;
    return output;
  }
  
  for (int i=1;i<k;i++){
    output[i-1] = i*k;
  }
  output[k-1]=0;
  
  return output;
}

void out(int * output, int length)
{
  if (output[0] == 0) {
    cout << "IMPOSSIBLE";
    return;
  }
  
  cout << output[0];
  for (int i = 1; i < length; i++) {
    if (output[i] != 0)
      cout << ' ' << output[i];
  }
}

int main(int argc, char **argv) {
  
    int t;
    cin >> t;
    
    int k, c, s;
    
    string output;
    
    for (int i = 1; i <= t; i++) {
      cin >> k;
      cin >> c;
      cin >> s;
      cout << "Case #" << i << ": ";
      
      out(compute(k, c, s), k);
      
      cout << endl;
      
    }
    
    return 0;
}
