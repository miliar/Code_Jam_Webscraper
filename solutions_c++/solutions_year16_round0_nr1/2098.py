#include <bits/stdc++.h>
#define IMPOSIBLE "INSOMNIA"
using namespace std;

const int MAXITERACIONES = 1000;

int tengo[10 + 2];
int color;
int faltan;
int N, aumento;

void agrega(int val){
    if(val == 0){
        tengo[0] = color;
        return;
    }
    int d;
    while(val > 0){
        d = val % 10;
        if(tengo[d] != color){
            tengo[d] = color;
            faltan--;
        }
        val -= d;
        val /= 10;
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    int c;
    for(int caso = 1; caso <= T; caso++){
        cout << "Case #" << caso << ": ";
        color++;
        cin >> aumento;
        N = 0;
        faltan = 10;
        for(c = 0; faltan > 0 && c <= MAXITERACIONES; c++){
            N += aumento;
            agrega(N);
        }
        if(faltan == 0){
            cout << N << "\n";
        }else{
            cout << IMPOSIBLE << "\n";
        }
    }
    return 0;
}
