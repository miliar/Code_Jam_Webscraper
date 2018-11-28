#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> chars {'_', 'E', 'F', 'G', 'H', 'I', 'N', 'O', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z'};

void countChar(int pos, string s, vector<size_t> &charscount) {
  size_t n = std::count(s.begin(), s.end(), chars[pos]);
  // cout<<"Counting "<<chars[pos]<<" "<<pos<<" found "<<n<<endl;
  charscount[pos] = n;
}

int main() {
  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {
    // 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    // _ E F G H I N O R S T  U  V  W  X  Z
    vector<size_t> charscount {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    vector<size_t> founddigits {0,0,0,0,0,0,0,0,0,0,0};
    string input;

    cin >> input;

    for (int i = 1; i <= 15; i++) {
      countChar(i, input, charscount);
    }
    // for (int i = 1; i <= 15; i++) {
    //   cout<<charscount[i]<<",";
    // }
    // cout<<endl;

    // Cool stuff begins here
    // Counting Zeros
    founddigits[0] = charscount[15]; // Z
    // charscount[1] -= founddigits[0];
    charscount[7] -= founddigits[0];
    // charscount[8] -= founddigits[0]; // UNUSED
    // Counting 2
    founddigits[2] = charscount[13]; // W
    charscount[7] -= founddigits[2];
    // charscount[10] -= founddigits[2];

    // Counting 4
    founddigits[4] = charscount[11];
    charscount[2] -= founddigits[4];
    charscount[7] -= founddigits[4];

    // Counting 6
    founddigits[6] = charscount[14];

    // Counting 1
    founddigits[1] = charscount[7];
    charscount[6] -= founddigits[1];

    // Counting 5
    founddigits[5] = charscount[2];
    charscount[12] -= founddigits[5];

    // Counting 7
    founddigits[7] = charscount[12];
    charscount[6] -= founddigits[7];
    charscount[9] -= founddigits[7];

    // Counting 8
    founddigits[8] = charscount[3];
    charscount[4] -= founddigits[8];

    // Counting 9
    founddigits[9] = charscount[6] / 2;

    // Counting 3
    founddigits[3] = charscount[4];

    // And finally
    // for (int i = 0; i < 10; i++) {
    //   cout<<founddigits[i]<<",";
    // }
    // cout<<endl;
    // cout<<"Almost there..."<<endl;

    string outputs = "";
    for (int i = 0; i < 10; i++) {
      for (size_t j = 0; j < founddigits[i]; j++) {
        outputs += to_string(i);
      }
    }

    cout<<"Case #"<<(i+1)<<": "<<outputs<<endl;
  }
  return 0;
}
