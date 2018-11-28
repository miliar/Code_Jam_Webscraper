#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

int T;

string digits[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int n_digits = 10;

string udigits[] = { "ZERO", "TWO", "FOUR", "SIX", "EIGHT" };
int n_udigits = 5;

char ul[] = { 'Z', 'E', 'R', 'O', 'N', 'T', 'W', 'H', 'U', 'F', 'I', 'V', 'S', 'X', 'G' };
int n_ul = 15;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        string str;
        in >> str;

        vector<int> d;

        map<char, int> m;

        for (int i = 0; i < str.length(); ++i)
        {
            auto it = m.find(str[i]);
            if (it != m.end()) it->second++;
            else
            {
                m.insert(pair<char, int>(str[i], 1));
            }
        }

        //zero
        if (m.find('Z') != m.end() && m.find('Z')->second > 0)
        {
            int nz = m.at('Z');
            m.at('Z') = 0; m.at('E') -= nz; m.at('R') -= nz; m.at('O') -= nz; for (int i = 0; i < nz; ++i) d.push_back(0);
        }

        //two
        if (m.find('W') != m.end() && m.find('W')->second > 0)
        {
            int nw = m.at('W');
            m.at('T') -= nw; m.at('W') -= nw; m.at('O') -= nw; for (int i = 0; i < nw; ++i) d.push_back(2);
        }

        //four
        if (m.find('U') != m.end() && m.find('U')->second > 0)
        {
            int nu = m.at('U');
            m.at('F') -= nu; m.at('O') -= nu; m.at('U') -= nu; m.at('R') -= nu; for (int i = 0; i < nu; ++i) d.push_back(4);
        }

        //six
        if (m.find('X') != m.end() && m.find('X')->second > 0)
        {
            int nx = m.at('X');
            m.at('S') -= nx; m.at('I') -= nx; m.at('X') -= nx; for (int i = 0; i < nx; ++i) d.push_back(6);
        }

        //eight
        if (m.find('G') != m.end() && m.find('G')->second > 0)
        {
            int ng = m.at('G');
            m.at('E') -= ng; m.at('I') -= ng; m.at('G') -= ng; m.at('H') -= ng; m.at('T') -= ng; for (int i = 0; i < ng; ++i) d.push_back(8);
        }

        //one
        if (m.find('O') != m.end() && m.find('O')->second > 0)
        {
            int no = m.at('O');
            m.at('O') -= no; m.at('N') -= no; m.at('E') -= no; for (int i = 0; i < no; ++i) d.push_back(1);
        }

        //three
        if (m.find('H') != m.end() && m.find('H')->second > 0)
        {
            int nh = m.at('H');
            m.at('T') -= nh; m.at('H') -= nh; m.at('R') -= nh; m.at('E') -= nh; m.at('E') -= nh; for (int i = 0; i < nh; ++i) d.push_back(3);
        }

        //five
        if (m.find('F') != m.end() && m.find('F')->second > 0)
        {
            int nf = m.at('F');
            m.at('F') -= nf; m.at('I') -= nf; m.at('V') -= nf; m.at('E') -= nf; for (int i = 0; i < nf; ++i) d.push_back(5);
        }

        //seven
        if (m.find('V') != m.end() && m.find('V')->second > 0)
        {
            int nv = m.at('V');
            m.at('S') -= nv; m.at('E') -= nv; m.at('V') -= nv; m.at('E') -= nv; m.at('N') -= nv; for (int i = 0; i < nv; ++i) d.push_back(7);
        }

        //nine
        if (m.find('I') != m.end() && m.find('I')->second > 0)
        {
            int ni = m.at('I');
            m.at('N') -= ni; m.at('I') -= ni; m.at('N') -= ni; m.at('E') -= ni; for (int i = 0; i < ni; ++i) d.push_back(9);

        }

        sort(d.begin(), d.end());

        out << "Case #" << t + 1 << ": ";
        for (int i = 0; i < d.size(); ++i)
        {
            out << d[i];
        }
        out << endl;
    }

    in.close();
    out.close();
}