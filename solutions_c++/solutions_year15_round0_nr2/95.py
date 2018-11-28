#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

int main(){
    //freopen("b.in", "r", stdin);
    //freopen("b.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        int D;
        cin >> D;
        int P[1000];
        int ans = 1000;
        for(int j = 0; j < D; j++)
            cin >> P[j];
        for(int k = 1; k <= 1000; k++){
            int temp = k;
            for(int l = 0; l < D; l++)
                temp += ((P[l] - 1) / k);
            if(temp < ans)
                ans = temp;
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}



/*int main(int argc, char *argv[]){
    //freopen("d.in", "r", stdin);
    //freopen("d.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        int X, R, C;
        cin >> X >> R >> C;
        bool possible = true;
        if(X > max(R, C) || X > 2 * min(R, C) - 1)
            possible = false;
        if(X == 2)
            possible = true;
        if(X == 4){
            if(R == 2 || C == 2)
                possible = false;
        }
        if((R * C) % X != 0)
            possible = false;
        if(possible)
            cout << "Case #" << i+1 << ": " << "GABRIEL" << endl;
        else
            cout << "Case #" << i+1 << ": " << "RICHARD" << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}*/
