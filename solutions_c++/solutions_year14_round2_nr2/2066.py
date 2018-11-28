#include <iostream>
using namespace std;
#include <fstream>

int main(){
    ifstream cin ("B.in");
    ofstream cout("B.out");

    int n;
    cin >> n;
    for (int kk = 1; kk <= n; kk++){
        int a, b, k;
        cin >> a >> b >> k;

        int result = 0;
        for (int i = 0; i < k; i++){
            for (int j = 0; j < a; j++){
                for (int l = 0; l < b; l++){
                    if ((j&l) == i){
                        result++;
                    }
                }
            }
        }
        cout << "Case #" << kk << ": " << result << endl;
    }


    return 0;
}
