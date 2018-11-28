#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

#include <fstream>
int main()
{
    //ifstream cin("in.txt");
    //ofstream cout("out.txt");

    int T;
    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        string  S;
        cin >> S;
        cout << "Case #" << i<<": ";
            
        int m = 0;
        int k = S.length()-1;

        for (int i = 0; i < k; i++)
        {
            if (S[i] != S[i+1]) m++;
        }    
        
        if (S[k] == '-') m++;
        cout << m << endl;

    }
    return 0;
}