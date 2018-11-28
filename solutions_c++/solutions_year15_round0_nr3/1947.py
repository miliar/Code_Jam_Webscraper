#include <bits/stdc++.h>

using namespace std;

ifstream f("c.in");

int evalMatrix[5][5];

int findCode(char x){
    if (x == 'i') return 2;
    if (x == 'j') return 3;
    if (x == 'k') return 4;
}


void scrie(int noTest, int tip){
    if (tip)
    printf("Case #%d: YES\n", noTest);
    else printf("Case #%d: NO\n", noTest);
}

int getSign(int x){
    if (x < 0) return -1;
    return 1;
}

int findEval(int currentEval, int toEval, int &numberOfMinus){

    currentEval = evalMatrix[abs(currentEval)][abs(toEval)] * getSign(currentEval) * getSign(toEval);
    return currentEval;
}

int main(){
    freopen("c.out", "w", stdout);

    int t; f >> t;
    for(int i=1; i<=4; ++i) evalMatrix[i][1] = i, evalMatrix[1][i] = i;
    for(int i=2; i<=4; ++i) evalMatrix[i][i] = -1;
    evalMatrix[1][1] = 1;

    evalMatrix[2][3] = 4;
    evalMatrix[2][4] = -3;

    evalMatrix[3][2] = -4;
    evalMatrix[3][4] = 2;

    evalMatrix[4][2] = 3;
    evalMatrix[4][3] = -2;


    for(int noTest=1; noTest<=t; ++noTest){
        int l, x;
        f >> l >> x;
        string s, sFinal;
        f >> s;
        for(int i=1; i<=x; ++i) sFinal += s;

        int currentI = 1;
        vector<int> prefix, sufix;
        int numberOfMinus = 0;
        for(int i=0; i<sFinal.size(); ++i){
            currentI = findEval(currentI, findCode(sFinal[i]), numberOfMinus);
            prefix.push_back( currentI );
        }
        currentI = 1;
        numberOfMinus = 0;/*
        for(int i=sFinal.size()-1; i>=0; --i){
            int rez = findEval( findCode(sFinal[i]), currentI, numberOfMinus );
            currentI = rez;
            if (numberOfMinus % 2 == 0 && rez < 0) rez = -rez;

            sufix.push_back(rez);
        }
        reverse(sufix.begin(), sufix.end());
        */
        for(int i=0; i<sFinal.size(); ++i){
            int currentEval = 1;
            numberOfMinus = 0;
            for(int j=i; j<sFinal.size(); ++j){
                currentEval = findEval(currentEval, findCode(sFinal[j]), numberOfMinus);
            }

            sufix.push_back(currentEval);
        }

        bool ok = 0;
        for(int i=1; i<sFinal.size(); ++i){
            int currentJ = 1;
            numberOfMinus = 0;
            //cout << i << "\n";
            for(int j=i; j+1<sFinal.size(); ++j){
                currentJ = findEval(currentJ, findCode(sFinal[j]), numberOfMinus );
                //int rez = currentJ;
                //if (numberOfMinus % 2 == 0) rez = -rez;
                //cout <<j << " " <<  prefix[i-1] << " " << rez << " " << sufix[j+1] << "\n";
                if (prefix[i-1] == 2 && currentJ == 3 && sufix[j+1] == 4){
                    //if (noTest == 51) cout << i << "  "<< i+1 << "  "<< j+2 << "\n";
                    scrie(noTest, 1);
                    ok = 1;
                    break;
                }
            }
            if (ok) break;
        }
        if (!ok) scrie(noTest, 0);
    }

    return 0;
}
