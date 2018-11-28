#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>
#include<math.h>


using namespace std;


typedef long long int ll;
#define For(i, a, b) for(int i=a; i<b; i++)
//100,000,000 operations


int main() {
	ifstream cin ("test.in");
	ofstream cout ("test.out");
	
	int T;
	bool used[10];
	cin >> T;
	For (t, 1, T+1) {
		int N;
		cin >> N;
		
		For (i, 0, 10) {
			used[i] = false;
		}
		int out = -1;
		For (i, 1, 100001) {
			int use = N*i;
			//Set all digits to true;
			bool add = false;
			for (int divide = 1000000; divide >= 1; divide = divide/10) {
				int a = use/divide;
				if (add == false && a > 0) {
					add = true;
				}
				
				if (add) {
					used[a] = true;
					//cout << use << " " << a << " " << used[a] << endl;
					use -= a*divide;
				}
			}
			
			
			//Check if all digits are true;
			bool exit = true;
			For (j, 0, 10) {
				//cout << used[j] << " ";
				if (used[j] == false) {
					exit = false;
				}
			}
			//cout << endl;
			if (exit) {
				out = N*i;
				break;
			}
		}
		if (out == -1) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << t << ": " << out << endl;
		}
	}
	
	
	
	return 0;
}

