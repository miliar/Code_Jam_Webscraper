#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int tests;
    int a;
    int b;
    int c;
    int d;
    int aa;
    int bb;
    int cc;
    int dd;
    int row_one;
    int row_two;
    vector <int> wynik;
    int lol;
    cin >> tests;
    for(int i =0; i<tests; i++)
    {
        wynik.clear();
     cin >> row_one;
     for(int j=0; j<4*(row_one-1);j++)
     {
         cin >> lol;
     }
     cin >> a; cin >> b; cin >> c; cin >> d;
       for(int j=0; j<(4-row_one)*4;j++)
     {
         cin >> lol;
     }
     cin >> row_two;
       for(int j=0; j<4*(row_two-1);j++)
     {
         cin >> lol;
     }
     cin >> aa; cin >> bb; cin >> cc; cin >> dd;
        for(int j=0; j<(4-row_two)*4;j++)
     {
         cin >> lol;
     }
    if (aa==a || aa == b || aa == c || aa==d)
    {
        wynik.push_back(aa);
       // cout << aa << ":::::a:::::";
    }
    if (bb==a || bb == b || bb == c || bb==d)
    {
        wynik.push_back(bb);
       // cout << bb << ":::::b:::::";
    }
    if (cc==a || cc == b || cc == c || cc==d)
    {
        wynik.push_back(cc);
       // cout << cc << "::::c::::::";
    }
    if (dd==a || dd == b || dd == c || dd==d)
    {
        wynik.push_back(dd);
        //cout << dd << ":::::d:::::";
    }
    if(wynik.size()<1)
    {
        cout << "Case #" << i+1 <<": Volunteer cheated!" << endl;
    }
    else if (wynik.size()>1)
    {
        cout << "Case #" << i+1 <<": Bad magician!" << endl;
    }
    else

    {
        cout << "Case #" << i+1 <<": "<< wynik[0] <<endl;
    }


    }

}
