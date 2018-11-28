#include <iostream>

using namespace std;

signed char mult[256][256];

int
main() {
  int T;

  cin >> T;

  for(int i = 0; i < 26; i++) {
    for(int j = 0; j < 26; j++) {
      mult[i][j] = 0;
    }
  }
  mult['1']['1'] = '1';
  mult['1']['i'] = 'i';
  mult['1']['j'] = 'j';
  mult['1']['k'] = 'k';

  mult['i']['1'] = 'i';
  mult['i']['i'] = -'1';
  mult['i']['j'] = 'k';
  mult['i']['k'] = -'j';

  mult['j']['1'] = 'j';
  mult['j']['i'] = -'k';
  mult['j']['j'] = -'1';
  mult['j']['k'] = 'i';

  mult['k']['1'] = 'k';
  mult['k']['i'] = 'j';
  mult['k']['j'] = -'i';
  mult['k']['k'] = -'1';

  for(int c = 1; c <= T; c++) {
    int l, x;
    string s;

    cin >> l >> x >> s;

    int N = x*l;
    int i = 0;

    char I = '1';
    bool result = false;

    while(!result && (i < N)) {
      if(I < 0) {
	I = -mult[-I][s[i%l]];
      } else {
	I = mult[I][s[i%l]];
      }
      i++;

      if(I == 'i') {
	int j = i;
	char J = '1';

	while(!result && (j < N)) {
	  if(J < 0) {
	    J = -mult[-J][s[j%l]];
	  } else {
	    J = mult[J][s[j%l]];
	  }
	  j++;

	  if(J == 'j') {
	    int k = j;
	    char K = '1';

	    while(k < N) {
	      if(K < 0) {
		K = -mult[-K][s[k%l]];
	      } else {
		K = mult[K][s[k%l]];
	      }
	      k++;
	    }

	    result = K == 'k';
	  }
	}
	if(j == N) break;
      }
    }

out:
    //cout << C << " (" << (int)'1' << ", " << (int)'i' << ", " << (int)'j' << ", " << (int)'k' << ")" << endl;
    cout << "Case #" << c << ": " << (result ? "YES" : "NO") << endl;
  }

  return 0;
}
