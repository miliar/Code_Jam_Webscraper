#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#define ll long long
using namespace std;

int main() {
    int t;
    bool num[9];
    cin >> t;
    ll answer[t];
    for (int i=0;i<t;i++) {
        for (int j=0;j<10;j++) {
            num[j] = false;
        }
        int n; ll n1;
        cin >> n;
        if (n==0) {
           answer[i]=0;
        } else {
            bool end;
            int j = 0; int abc = 0;
            end = false;
            while (end==false) {
                  j++;
                  n1 = j*n;
                  stringstream ss;
                  ss << n1;
                  string str = ss.str();
                  int len; len = str.length();
                  for (int k=0;k<len;k++) {
                      string str1=str.substr(k,1);
                      int n2 = atoi(str1.c_str());
                      switch (n2) {
                      case 0:
                           if (num[0]==false) {
                              num[0] = true;
                              abc++;
                           }
                           break;
                      case 1:
                           if (num[1]==false) {
                              num[1] = true;
                              abc++;
                           }
                           break;
                      case 2:
                           if (num[2]==false) {
                              num[2] = true;
                              abc++;
                           }
                           break;
                      case 3:
                           if (num[3]==false) {
                              num[3] = true;
                              abc++;
                           }
                           break;
                      case 4:
                           if (num[4]==false) {
                              num[4] = true;
                              abc++;
                           }
                           break;
                      case 5:
                           if (num[5]==false) {
                              num[5] = true;
                              abc++;
                           }
                           break;
                      case 6:
                           if (num[6]==false) {
                              num[6] = true;
                              abc++;
                           }
                           break;
                      case 7:
                           if (num[7]==false) {
                              num[7] = true;
                              abc++;
                           }
                           break;
                      case 8:
                           if (num[8]==false) {
                              num[8] = true;
                              abc++;
                           }
                           break;
                      case 9:
                           if (num[9]==false) {
                              num[9] = true;
                              abc++;
                           }
                           break;
                      }
                  }
                  if (abc==10) {
                     end = true;
                  }
            }
            answer[i]=n1;
        }   
    }
    for (int i=0;i<t;i++) {
        if (answer[i]==0) {
           cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        } else {
          cout << "Case #" << i+1 << ": " << answer[i] << endl;
        }
    }
    return 0;
}
