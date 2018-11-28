#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;

string to_string(long long N)
{
    string result;
    ostringstream convert;
    convert << N;
    result = convert.str();
    return result;
}

long long find_digs(long long N)
{
    vector<bool> digs_found = vector<bool>(10, false);
    int num_to_go = 10;

    long long newN = 0;

    while(num_to_go)
    {
        newN += N;
        string strN = to_string(newN);
                
        for (int i = 0; i < strN.size(); i++)
        {
            if (!digs_found[strN[i] - '0'])
            {
                digs_found[strN[i] - '0'] = true;
                num_to_go--;
            }
        }
    }
    return newN;
}

int main (void)
{
    ifstream in("Ain.txt");
    cin.rdbuf(in.rdbuf());
    ofstream out("Aout.txt");
    cout.rdbuf(out.rdbuf()); 

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        long long N;
        cin >> N;

        if (N == 0)
            cout << "INSOMNIA";
        
        else
        {
            cout << find_digs(N);
        }
        
        cout << endl;
    }
    return 0;
}
