#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

long long getInt(ifstream &instream)
{
    string s = "";
    instream >> s;
    return atoll(s.c_str());
}

int main()
{
    ifstream si;
    si.open("in.in", fstream::in);
    ofstream so;
    so.open("out.out", fstream::out);
    
    int t = getInt(si);
    cout << t << endl;

    for (int i = 0; i < t; ++i) {
        long long r = getInt(si);
        long long t = getInt(si);
        cout << r << " " << t << endl;
        int count = 0;
        while (t >= (2*r + 1)) {
            ++count;
            t -= 2*r + 1;
            r += 2;
        }
        cout << "Case #" << i+1 << ": " << count << endl;
        so << "Case #" << i+1 << ": " << count << endl;
    }

    si.close();
    so.close();

    return 0;
}

