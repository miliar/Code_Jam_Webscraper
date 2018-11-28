#include <cstdlib>
#include <vector>
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	int T;
	cin >> T;
	for (int n=0;n<T;n++) {
		int Sm;
		cin >> Sm;
		vector <int> s (Sm+1,0);
		string ss;
		cin >> ss;
		//cout << ss << "\n\n";
		for (int i=0;i<Sm+1;i++) {
			s[i] = int(ss[i])-48;
		}
		/*for (int i=0;i<Sm+1;i++) {
			cout << s[i]*2 << endl;
		}*/
		int i=0;
		int q=0;
		while (i<=Sm) {
			if (s[i]==0) {
				q++;
				i++;
			} else {
				int ppl=s[i];
				for (int j=1;j<ppl && i+ppl<=Sm;j++) {
					ppl+=s[i+j];
				}
				i+=ppl;

				//i+=s[i];
			}
		}
		printf("Case #%d: %d\n",n+1,q);
	}

	return 0;
}

