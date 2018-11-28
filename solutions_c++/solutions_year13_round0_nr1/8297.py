#include <iostream>
#include <cstdio>
#include <set>
#include <string>

using namespace std;
//typedef vector <string> v_s;

string mapa [4];
string O_ = "OOOO", O_T = "OOOT", X_ = "XXXX", X_T = "XXXT", O_t = "TOOO", X_t = "TXXX";

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int n; cin >> n;
    for(int i = 0; i < n; i ++)
    {
        short A = 0;
        for(int j = 0; j < 4; j ++)
        {
            cin >> mapa[j];
            if(O_ == mapa[j] || O_T == mapa[j] || O_t == mapa[j]) A = 1;
            if(X_ == mapa[j] || X_T == mapa[j] || X_t == mapa[j]) A = 2;
        }
        int cont_puntos = 0;
        if(A == 0)
        {
            string diagonal = "";
            for(int j = 0; j < 4; j ++)
            {
                string cad = "";
                for(int s = 0; s < 4; s ++)
                {
                    if(s == j) diagonal.push_back(mapa[s][j]);
                    if(mapa[s][j] == '.') cont_puntos ++;
                    cad.push_back(mapa[s][j]);
                }
                if(O_ == cad || O_T == cad || O_t == cad) A = 1;
                if(X_ == cad || X_T == cad || X_t == cad) A = 2;
            }
            if(O_ == diagonal || O_T == diagonal || O_t == diagonal) A = 1;
            if(X_ == diagonal || X_T == diagonal || X_t == diagonal) A = 2;
            diagonal = "";
            diagonal.push_back(mapa[0][3]);
            diagonal.push_back(mapa[1][2]);
            diagonal.push_back(mapa[2][1]);
            diagonal.push_back(mapa[3][0]);
            if(O_ == diagonal || O_T == diagonal || O_t == diagonal) A = 1;
            if(X_ == diagonal || X_T == diagonal || X_t == diagonal) A = 2;
        }
        if(A == 1)
        {
            cout << "Case #" << i + 1 << ": O won" << endl;
            continue;
        }
        if(A == 2)
        {
            cout << "Case #" << i + 1 << ": X won" << endl;
            continue;
        }
         if(A == 0 && cont_puntos == 0)
        {
            cout << "Case #" << i + 1 << ": Draw" << endl;
            continue;
        }
         if(A == 0 && cont_puntos > 0)
        {
            cout << "Case #" << i + 1 << ": Game has not completed" << endl;
            continue;
        }
    }
    return 0;
}
