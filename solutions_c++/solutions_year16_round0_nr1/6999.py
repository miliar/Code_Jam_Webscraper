#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int main() {
    ifstream cin("/Users/mayurpawar/Desktop/cpp/codejam/A-large.in");
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        int N, sum=0;
        bool num[10]={false, false, false, false, false, false, false, false, false, false};
        cin >> N;
        if (N==0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        for (int j=1; j<100000; j++) {
            int currentN=N*j;
            int digits = (int)log10(currentN)+1;
            int x=currentN;
            for (int k=0; k<digits; k++) {
                int reminder=x%10;
                x=x/10;
                if (num[reminder]==false) {
                    num[reminder]=true;
                    sum++;
                }
                if (sum==10) {
                    cout << currentN << endl;
                    break;
                }
            }
            if (sum==10) break;
        }
    }
}