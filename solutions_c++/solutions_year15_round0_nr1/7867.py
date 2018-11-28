#include <iostream>
using namespace std;

int main()
{
      int n;
      cin >> n;

      for(int i=0; i<n; ++i)
      {
            int m;
            cin >> m;

            int s=0, r=0;
            for(int j=0; j<(m+1); ++j)
            {
                  char c;
                  cin >> c;
                  int d = (int)(c-'0');

                  if(s < j)
                  {
                        r++, s++;
                  }

                  s+=d;
            }

            cout << "Case #" << (i+1) << ": " << r << endl;
      }

      return 0;
}
