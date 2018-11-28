#include <iostream>
#include <vector>

using namespace std;

const int MAX_ITER = 10000;

int main(int argc, char *argv[]){
  int cases;
  
  cin >> cases;

  for(int i=1;i<cases+1;++i){
    int n_orig;
    cin >> n_orig;

    if(n_orig == 0){
      cout << "Case #" << i << ": INSOMNIA" << endl;
      continue;
    }

    vector<bool> seen(10, false); 
    int n_seen=0, iter=1, n = n_orig;
    while(iter < MAX_ITER && n_seen < 10){
      int num = n;
      do {
              
        if(seen[num%10] == false){
          ++n_seen;
          seen[num%10] = true;
        }

        num/=10;

      } while(num > 0);

      if(n_seen == 10)
        break;

      ++iter;
      n = n_orig*iter;
    }
    if(n_seen == 10){
      cout << "Case #" << i << ": " << n << endl;
      continue;
    } 
    else
      cout << "Case #" << i << ": INSOMNIA" << endl;
  }
}
