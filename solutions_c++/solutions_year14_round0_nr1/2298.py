#include <iostream>

using namespace std;

void testcase(int tc){
  int s[2][4];
	for (int j=0; j<2; ++j){
	  int r;
	  cin >> r;
	  for (int k=1; k<=4; ++k){
	    int n[4];
	    for (int l=0; l<4; ++l){
	      if (k == r)
	        cin >> s[j][l];
	      else
	        cin >> n[l];
	    }
	  }
	}
	int answer = 0;
	for (int i=0; i<4; ++i){
	  for (int j=0; j<4; ++j){
	    if (s[0][i] == s[1][j]){
	      if (answer != 0){
	        cout << "Case #" << tc << ": Bad magician!\n";
	        return;
	      }
	      answer = s[0][i];
	    }
	  }
	}
	if (answer == 0){
	  cout << "Case #" << tc << ": Volunteer cheated!\n";
	  return;
	}
	cout << "Case #" << tc << ": " << answer << endl;;
}

int main(){
	int ntc;
	cin >> ntc;
	for (int tc=1; tc<=ntc; ++tc){
	  testcase(tc);
	}
}
