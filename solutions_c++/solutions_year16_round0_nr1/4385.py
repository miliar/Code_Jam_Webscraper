#include <iostream>
#include <vector>

using namespace std;

int main ()
  {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
      {
        long long N;
        cin >> N;
        if (N == 0)
          {
            cout << "Case #" << i+1 << ": INSOMNIA\n";
            continue;
          }
        long long mult = 1;
        vector<int> res;
        for (unsigned a = 0; a < 10; ++a) res.push_back(0);
        while ((mult-1) * N < mult * N)
          {
            long long x = mult * N;
            while (x > 0)
              {
                if (res[x%10] == 0) res[x%10] = 1;
                x /= 10;
              }
            bool done = true;
            for (unsigned a = 0; a < 10; ++a)
              {
                if (res[a] == 0)
                  {
                    done = false;
                    mult++;
                    break;
                  }
              }
            if (done) break;
          }
        if ((mult-1) * N > mult * N) cout << "Case #" << i+1 << ": INSOMNIA\n";
        else cout << "Case #" << i+1 << ": " << mult * N << "\n";
      }
    return 0;
  }
            

        
