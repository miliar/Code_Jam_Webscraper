#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int p;
    in >> p;
    for (int k = 1; k <= p; ++k)
    {
       string S;
       in >> S;
       map <char, int> A;
       A.insert({'Z', 0});
       A.insert({'G', 0});
       A.insert({'H', 0});
       A.insert({'T', 0});
       A.insert({'X', 0});
       A.insert({'S', 0});
       A.insert({'N', 0});
       A.insert({'I', 0});
       A.insert({'F', 0});
       A.insert({'O', 0});
       for (int i = 0; i < S.size(); ++i)
       {
          auto it = A.find(S[i]);
          if (it == A.end())
          {
               A.insert({S[i], 1});
          }
          else
          {
               ++it->second;
          }
    }
    vector <int> B;
    while (A['Z'] > 0)
    {
        B.push_back(0);
        --A['Z'];
        --A['E'];
        --A['R'];
        --A['O'];
    }
    while (A['G'] > 0)
    {
        B.push_back(8);
        --A['E'];
        --A['I'];
        --A['G'];
        --A['H'];
        --A['T'];
    }
    while (A['H'] > 0)
    {
        B.push_back(3);
        --A['T'];
        --A['H'];
        --A['R'];
        A['E'] -= 2;
    }
    while (A['T'] > 0)
    {
        B.push_back(2);
        --A['T'];
        --A['W'];
        --A['O'];
    }
    while (A['X'] > 0)
    {
        B.push_back(6);
        --A['S'];
        --A['I'];
        --A['X'];
    }
    while (A['S'] > 0)
    {
        B.push_back(7);
        --A['S'];
        --A['E'];
        --A['V'];
        --A['E'];
        --A['N'];
    }
    while (A['V'] > 0)
    {
        B.push_back(5);
        --A['F'];
        --A['I'];
        --A['V'];
        --A['E'];
    }
    while (A['F'] > 0)
    {
        B.push_back(4);
        --A['F'];
        --A['O'];
        --A['U'];
        --A['R'];
    }
    while (A['O'] > 0)
    {
        B.push_back(1);
        --A['O'];
        --A['N'];
        --A['E'];
    }
    while (A['N'] > 0)
    {
        B.push_back(9);
        --A['N'];
        --A['I'];
        --A['N'];
        --A['E'];
    }
    sort(B.begin(), B.end());
    out << "Case #" << k << ": ";
    for (int i = 0; i < B.size(); ++i)
    {
        out << B[i];
    }
    out << endl;
    }
    in.close();
    out.close();
    return 0;
}
