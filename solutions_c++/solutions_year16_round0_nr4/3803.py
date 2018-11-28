#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;

int main (void)
{
    ifstream in("Din.txt");
    cin.rdbuf(in.rdbuf());
    ofstream out("Dout.txt");
    cout.rdbuf(out.rdbuf()); 

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        
        int K, C, S;

        cin >> K >> C >> S;

        for (int i = 1; i < K; i++)
            cout << i << " ";
        cout << K << endl;     

    }
    return 0;
}
