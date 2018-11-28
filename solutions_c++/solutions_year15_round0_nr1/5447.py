#include <iostream>

using namespace std;
int* stringToInt(string& s);

int main(){
    int t;
    cin >> t;
    for(int j = 1; j <= t; j++){
        int sm;
        cin >> sm;
        string shys;
        cin >> shys;

        int* a = stringToInt(shys);

        int added = 0;
        int total = a[0];

        for(int i = 1; i <= sm; i++){
            if(i > total && a[i] != 0){
                added += i - total;
                total += added;
            }
            total += a[i];
        }

        cout << "Case #" << j << ": " << added << endl;
        delete[] a;
    }

    return 0;
}

int* stringToInt(string& s){
    int* a = new int[s.size()];
    for(int i = 0; i < s.size(); i++){
        a[i] = (int) (s[i] - '0');
    }
    return a;
}
