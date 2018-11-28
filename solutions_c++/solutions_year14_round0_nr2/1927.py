#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    int count, i, round, j;
    double C, F, X, k, time;
    
    cin >> count;
    for(i = 1; i <= count; i++){
        cin >> C >> F >> X;
	time = 0;
        k = (F * X - 2.0 * C) / (F * C);
        round = (int) k;
        if(round < 0){
            round = 0;
        }
        for(j = 0; j < round; j++){
            time = time + C / (2.0 + j * F);
        }
        time = time + X / (2.0 + round * F);
        cout << setprecision(7) << fixed;
	cout << "Case #" << i << ": " << time << endl;
    }
    return 0;
}
