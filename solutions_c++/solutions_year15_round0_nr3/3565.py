#include <iostream>
#include <cmath>
#include <cassert>
#define DEBUG 0
#define I 2
#define J 3
#define K 4

using namespace std;

void printQ(int a){
    int aa = abs(a);
    if(aa != a){
        cout << '-';
    }
    else{
        cout << ' ';
    }
    char mat[4] = {'1', 'I', 'J', 'K'};
    cout << mat[aa-1];
}

int divQ(int b, int a){
    int aa = abs(a);
    bool aneg = a < 0;

    static int matrix[4][4] = {{1,  I,  J,  K},
                         {I, -1,  K, -J},
                         {J, -K, -1,  I},
                         {K,  J, -I, -1}};
    int v = 0;
    if(DEBUG){
        cout << "dividing ";
        printQ(b);
        cout << " by ";
        printQ(a);
        cout << " rb ";
        printQ(b);

        cout << " row: " << aa-1 <<endl;
    }
    for(int i = 1; i <= K; i++){
        if(matrix[aa-1][i - 1] == b){
            v = i;
            break;
        }
    }

    bool bneg = false;
    // if we didn't find b in expected row, b must be negative
    if(v == 0){
        bneg = true;
        b = -b;
        for(int i = 1; i <= K; i++){
            if(matrix[aa-1][i - 1] == b){
                v = i;
                break;
            }
        }
    }

    if(v == 0){
        cout << "RET 0" << endl;
        return 0;
    }

    if(aneg != bneg){
        v *= -1;
    }

    if(DEBUG){
        cout << "RESULT: ";
        printQ(v);
        cout << endl;
    }

    return v;

}

int mulQ(int a, int b){
    int aa = abs(a);
    int ab = abs(b);

    /*
    if(aa == 1 || ab == 1){
        return a * b;
    }
    */

    static int matrix[4][4] = {{1,  I,  J,  K},
                         {I, -1,  K, -J},
                         {J, -K, -1,  I},
                         {K,  J, -I, -1}};
    int v = matrix[aa-1][ab-1];
    if((a < 0 && b > 0) || (a > 0 && b < 0)){
        v *= -1;
    }

    return v;

}

int c2i(char c){
    return (int) (c - 'i' + 2);
}

int main(){

    /*
    static int matrix[4][4] = {{1,  I,  J,  K},
                         {I, -1,  K, -J},
                         {J, -K, -1,  I},
                         {K,  J, -I, -1}};
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            int d = matrix[i][j];
            assert(divQ(d, i+1) == j + 1);
        }
    }
    cout << "1" << endl;

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            int d = matrix[i][j];
            assert(divQ(-d, i+1) == -(j + 1));
        }
    }
    cout << "2" << endl;

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            int d = matrix[i][j];
            assert(divQ(d, -(i+1)) == -(j + 1));
        }
    }
    cout << "3" << endl;

    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            int d = matrix[i][j];
            assert(divQ(-d, -(i+1)) == (j + 1));
        }
    }
    cout << c2i('i') << endl;
    cout << c2i('j') << endl;
    cout << c2i('k') << endl;

    for(int i = 1; i <= K; i++){
        for(int j = 1; j <= K; j++){
            printQ(mulQ(i, j));
            cout << " ";
        }
        cout << endl;
    }

    cout << endl;
    printQ(divQ(-1, I));
    cout << endl;
    cout << endl;
    printQ(divQ(1, -I));
    cout << endl;

    cout << endl;
    */
    int t;
    cin >> t;
    for(int u = 1; u <= t; u++){
        int l;
        int x;
        cin >> l >> x;

        string s;
        cin >> s;

        if(DEBUG){
            cout << "l: " << l << endl;
            cout << "x: " << x << endl;
            cout << "s: " << s << endl;
        }

        if(l * x < 3){
            cout << "Case #" << u << ": NO" << endl;
        }
        else{
            int lim = l * x;
            int* a = new int[lim];
            for(int i = 0; i < lim; i++){
                a[i] = c2i(s[i % l]);
            }
            int* dp = new int[lim];
            dp[0] = a[0];

            for(int i = 1; i < lim; i++){
                dp[i] = mulQ(dp[i-1], a[i]);
            }

            if(DEBUG){
                cout << "a: ";
                for(int i = 0; i < l; i++){
                    printQ(a[i]);
                }
                cout << endl;
                cout << "d: ";
                for(int i = 0; i < l; i++){
                    printQ(dp[i]);
                }
                cout << endl;
            }

            bool yes = false;

            for(int i = 0; i < lim - 2 && !yes; i++){
                if(dp[i] == I){
                    for(int j = i + 1; j < lim - 1 && !yes; j++){
                        int second = divQ(dp[j], dp[i]);
                        if(second == 0){
                            cout << "second zero at: ";
                            printQ(dp[j]);
                            cout << "/";
                            printQ(dp[i]);
                            cout << endl;
                            cout << "i: " << i << " j: " << j << endl;
                            assert(false);
                        }
                        if(second == J){
                            int third = divQ(dp[lim-1], dp[j]);
                            if(third == 0){
                                cout << "third zero at: ";
                                printQ(dp[lim - 1]);
                                cout << "/";
                                printQ(dp[j]);
                                cout << endl;
                                cout << "i: " << i << " j: " << j << endl;
                                assert(false);
                            }
                            if(third == K){
                                yes = true;
                            }
                        }
                    }
                }
            }

            if(yes){
                cout << "Case #" << u << ": " << "YES" << endl;
            }
            else{
                cout << "Case #" << u << ": " << "NO" << endl;
            }
        }
    }

    return 0;
}
