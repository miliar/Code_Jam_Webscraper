#include <iostream>
using namespace std;

int main(){
	FILE* fp;
	freopen_s(&fp, "out.txt", "w", stdout);
	int c;
	cin >> c;
	for (int i = 0; i < c; i++){
		int smax;
		cin >> smax;
		int need = 0;
		int already = 0;
		for (int j = 0; j <= smax; j++)
		{
			char t;
			do{
				cin >> t;
			} while (t == ' ' || t == '\n' || t == '\t' || t == '\r');
			t -= '0';

			if (t != 0 && j>already + need)need = j - already;
			already += t;
		}
		cout << "Case #" << (i + 1) << ": " << need << endl;
	}
}