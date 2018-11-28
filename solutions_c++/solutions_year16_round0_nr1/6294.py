#include <iostream>
#include <vector>
using namespace std;

bool hasFalse (vector <bool> &vec) {
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] == false) return true;
        //cout << vec[i] << " ";
    }
    return false;
}

void check (vector<bool> &vec, int num) {
    while (num > 0) {
        vec[num%10] = true;
        //cout << num << endl;
        //cout << "ANT: "<< num << endl;
        num = num / 10;
        //cout << "DESP: "<< num << endl;
    }
}

int main () {
    int t = 0;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        vector <bool> vec (10,false);
        int n = 0;
        cin >> n;
        bool flag;
        if (n == 0) flag = false;
        else flag = true;
        int cont = 1;
        int temp = 0;
        while (hasFalse(vec) && flag) {
            temp = n*cont;
            //cout << "NEW: "<<temp;
            check(vec, temp);

            cont++;
        }
        if (flag)
            cout << "Case #" << i << ": " << temp << endl;
        else
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;

    }


}
