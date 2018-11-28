#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;

int main (void)
{
    ifstream in("Bin.txt");
    cin.rdbuf(in.rdbuf());
    ofstream out("Bout.txt");
    cout.rdbuf(out.rdbuf()); 

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        string S;
        cin >> S;

        int num_moves = 0;

        for (int i = 1; i < S.size(); i++)
        {
            if (S[i] != S[i-1])
            {
                num_moves++;
                S[i-1] = S[i];
            }
        }        

        if (S[S.size()-1] == '-')
            num_moves++;

        cout << num_moves << endl;
    }
    return 0;
}
