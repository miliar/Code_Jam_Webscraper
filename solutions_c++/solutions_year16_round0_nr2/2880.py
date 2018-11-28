#include <iostream>
using namespace std;
string vt[100];

int main() {
	int t, n, k;
	cin >> t;
	getline(cin, vt[0]);
    for(int i = 0; i < t; i++){
        getline(cin, vt[i]);
    }
    for(int i = 0; i< t; i++){
        cout << "Case #" << (i+1) << ": ";
        char find = '-';
        string s = vt[i];
        int countX = 0;
        for(int j = s.length() - 1; j >=0; j--){
            if(s.at(j) == find){
                countX++;
                if(find == '-')
                    find = '+';
                else
                    find = '-';
            }
        }
        cout << countX << endl;
    }
    cin >> n;
	return 0;
}
