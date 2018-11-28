#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

vector<bool> v(10, false);

int summ(vector<bool> a){
    int res = 0;
    for(int i = 0; i < 10; i++){
        res += int(a[i]);
    }
    return res;
}

int sets(long long a){
    while(a > 0){
        int b = a % 10;
        v[b] = true;
        a /= 10;
    }
    return 0;
}

int main(){
    //ifstream in("input.in");
    //ofstream out("output.txt");
    int n;
    long long t, t1;
    cin >> n;
    for(int i= 0; i < n; i++){
        for(int j = 0; j < 10; j++){
            v[j] = 0;
        }
        cin >> t;
        t1 = t;
        if(t == 0){
            cout <<"Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        }
        else{
            sets(t1);
            while(summ(v) < 10){
                t1 += t;
                sets(t1);
            }

            cout << "Case #" << i + 1 << ": " << t1 << endl;
        }
    }
    return 0;
}
