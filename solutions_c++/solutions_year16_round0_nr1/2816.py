#include <iostream>
using namespace std;

int main() {
	int t, n, k;
	cin >> t;
	int vt[100];
	int check[10];
    for(int i = 0; i < t; i++){
        cin >> vt[i];
    }
    for(int i = 0; i< t; i++){
        cout << "Case #" << (i+1) << ": ";
        if(vt[i] == 0){
            cout << "INSOMNIA"<<endl;
            continue;
        }
        n = vt[i];
        for(int i = 0; i < 10; i++){
            check[i] = 1;
        }
        long long sum = n;
        int countX = 0;
        while(true){
            long long temp = sum;
            while(temp != 0){
                countX += check[temp % 10];
                check[temp % 10] = 0;
                temp = temp / 10;
            }
            if(countX == 10){
                cout << sum << endl;
                break;
            }
            sum = sum + n;
        }
    }
    cin >> n;
	return 0;
}
