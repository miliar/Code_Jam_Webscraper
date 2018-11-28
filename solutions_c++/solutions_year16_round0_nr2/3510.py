#include <stdio.h> 
#include <iostream>
#include <string>

using namespace std;

int main(){
    int T; 
    scanf("%d", &T);
    string buf;
    int aux [100];
    for (int i=0; i<T; ++i) {
        cin >> buf;
        printf("Case #%d: ", i+1); 
        int len = buf.length();
        for(int j=0; j<len; ++j)
            if (buf[j] == '-') aux[j] = 0;
            else aux[j] = 1;
        int cnt = 0;
        bool flip = false;
        int flipped = 0;
        for (int j=len-1; j>=0; --j) {
          if (aux[j] ^ flipped == 0)
              flip = true;
          else
              if (flip) {
                  cnt++;
                  flipped = flipped^1;
                  flip == true;
              }
              else flip = false;
        }
        if (flip) cnt++;
        cout << cnt << endl;
        cnt = 0;
    }
    return 0;
}
