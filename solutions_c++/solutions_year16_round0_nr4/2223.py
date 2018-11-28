#include <iostream>
using namespace std;
int vt[100];
int vK[100];
int vC[100];
int vS[100];

int main() {
	int t, n, k;
	cin >> t;
	int minX = 1;
    for(int i = 0; i< t; i++){
        cin >> vK[i] >> vC[i] >> vS[i];
    }
    for(int i = 0; i< t; i++){
        cout << "Case #" << (i+1) << ": ";
        int k = vK[i];int s = vS[i];int c = vC[i];
        if(c == 1 || k == 1){
            if(s < k){
                cout << "IMPOSSIBLE";
            }else{
                for(int j = 1; j <= k; j++)
                    cout << j << " ";
            }
        }else{
            if(s < k - 1){
                cout << "IMPOSSIBLE";
            }else{
                for(int j = 1; j <= k-1; j++)
                    cout << (j + 1 + k * (j - 1)) << " ";
            }
        }
        cout << endl;
    }
	return 0;
}
