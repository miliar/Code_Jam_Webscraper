#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
          int a[4],b[4];
          int t, k, x, l = 1;
          cin >> t;
          while (l <= t)
          {
                    cin >> k;
                    for (int i = 0; i < 4;i ++) {
                              for (int j = 0; j < 4; j++) {
                                        cin >> x;
                                        if (k-1 == i) {
                                                  a[j] = x;
                                        }
                              }
                    }
                    cin >> k;
                    for (int i = 0; i < 4;i ++) {
                              for (int j = 0; j < 4; j++) {
                                        cin >> x;
                                        if (k-1 == i) {
                                                  b[j] = x;
                                        }
                              }
                    }
                    int f= 0, tm;
                    for (int i = 0; i < 4; i++) {
                              for (int j = 0 ; j < 4; j++) {
                                        if (a[i] == b[j]) {
                                                  f++;
                                                  tm  = a[i];
                                                  break;
                                        }
                              }

                    }

                    if (f == 1) {
                              cout <<"Case #"<<l<<": " << tm << endl;
                    } else if (f > 1) {
                              cout <<"Case #"<<l<<": " << "Bad magician!" << endl;
                     }else {
                              cout << "Case #"<<l<<": " << "Volunteer cheated!" << endl;
                    }
                    l++;
          }
          return 0;
}
