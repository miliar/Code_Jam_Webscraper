#include<iostream>
#include<cstdlib>
#include<cstring>

using namespace std;

bool seen_all(int *seen) {
  for (int i=0; i<10; ++i) {
    if (seen[i]==0) return false;
  }
  return true;
}

int main() {
  int T;
  int N;
  cin >> T;

  for (int t=1; t<=T; ++t) {
    cin >> N;
    int sol=-1;
    int seen[10]={0,0,0,0,0,0,0,0,0,0};
    if (N==0) {
      cout << "Case #" << t << ": INSOMNIA" << endl;
      continue;
    }
    if (N==1)
      sol=10;
    if (N==2)
      sol=90;
    if (N>=3) {
      int K=1;
      while (!seen_all(seen)) {
	char s[128];
	sprintf(s, "%d", K*N);
	//cout << "cadena " << s << endl;
	for (char *c=s; (*c)!=0; ++c) {
	  seen[(*c)-'0']++;
	  //cout << "caracter " << *c << endl;
	}
	sol=N*K;
	K++;
      }
    }


    cout << "Case #" << t << ": ";
    cout << sol << endl;
  }


  return 0;
  
}
