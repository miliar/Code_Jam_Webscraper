#include <iostream>

using namespace std;

int calculate(long long int n){
    int a[11] = {0};
    long long int i = 1, res= -1;
    for(int j = 0; j < 10; j++){
        if (a[j] == 0){
            long long int q = n * i;
            i++;
            res = q;
            while (q != 0){
                a[q % 10]++;
                q = q/10;
            }
            if (i <= 1000000)
                j = -1;
            else {res = -1;break;}
        }
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++){
        long long int N;
        cin >> N;
        if (N == 0)
            cout << "Case #" << i << ": INSOMNIA\n";
        else{
            int res = calculate(N);
            if (res == -1){
                cout << "Case #" << i << ": INSOMNIA\n";
            }
            else
                cout << "Case #" << i << ": " << res << "\n";
        }
    }
    return 0;
}
