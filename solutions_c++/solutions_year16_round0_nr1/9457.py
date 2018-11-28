#include <iostream>
#include <vector>
using namespace std;

void mark(long long int n, vector<bool> &v, int& marked) {
    while(n > 0) {
        int aux = n%10;
        if(!v[aux]) {
            v[aux] = true;
            marked++;
        }
        n = n/10;
    }
}

int main() {
    int n;
    cin >> n;
    int i = 1;
    while(i <= n) {
        int num;
        cin >> num;
        cout << "CASE #" << i << ": ";
        if(num == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            vector<bool> v = vector<bool>(10, false);
            int marked = 0;
            long long int act = 0;
            while(marked < 10) {
                act += num;
                mark(act, v, marked);
            }
            cout << act << endl;
        }
        ++i;
    }
}