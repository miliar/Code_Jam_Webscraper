#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  // get rid of \n after T
  string s;
  getline(cin,s);

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {

    string letters, sorted;
    getline(cin, letters);

    int todel;
    vector<int> counts(10);

    // 0
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'Z')
	++counts[0];
    }
    todel = counts[0];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'Z' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[0];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[0];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'R' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[0];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'O' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 2
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'W')
	++counts[2];
    }
    todel = counts[2];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'T' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[2];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'W' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[2];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'O' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 4
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'U')
	++counts[4];
    }
    todel = counts[4];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'F' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[4];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'O' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[4];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'U' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[4];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'R' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    
    // 6
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'X')
	++counts[6];
    }
    todel = counts[6];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'S' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[6];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'I' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[6];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'X' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 8
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'G')
	++counts[8];
    }
    todel = counts[8];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[8];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'I' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[8];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'G' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[8];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'H' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[8];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'T' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    
    // 3
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'H')
	++counts[3];
    }
    todel = counts[3];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'T' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[3];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'H' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[3];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'R' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[3];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[3];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 5
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'F')
	++counts[5];
    }
    todel = counts[5];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'F' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[5];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'I' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[5];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'V' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[5];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 7
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'V')
	++counts[7];
    }
    todel = counts[7];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'S' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[7];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[7];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'V' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[7];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[7];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'N' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    // 1
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'O')
	++counts[1];
    }
    todel = counts[1];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'N' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }
    todel = counts[1];
    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'E' && todel > 0) {
	letters[j] = '0';
	--todel;
      }
    }

    for (int j = 0; j< letters.length();  ++j) {
      if (letters[j] == 'I') {
	++counts[9];
	letters[j] = '0';
      }
    }
      
    cout << "case #" << i << ": ";
    for (int j = 0; j< counts.size();  ++j) {
      while (counts[j] > 0) {
	cout << j;
	--counts[j];
      }
    }
    cout << endl;
  }
  return 0;
}
