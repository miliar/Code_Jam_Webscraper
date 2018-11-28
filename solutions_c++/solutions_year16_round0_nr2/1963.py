#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("res.txt");
    int t;
    fin >> t;
    for(int tc = 0; tc < t; tc ++)
    {
        fout << "Case #" << (tc + 1) << ": ";
        string s;
        fin >> s;
        int pos = -1;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i] == '-') pos = i;
        }
        if(pos == -1)
        {
            cout << 0 << endl;
            fout << 0 << endl;
            continue;
        }
        int cnt = 1;
        while(pos > 0)
        {
            if(s[pos-1] != s[pos]) cnt ++ ;
            pos --;
        }
        cout << cnt << endl;
        fout << cnt << endl;
    }
    return 0;
}
