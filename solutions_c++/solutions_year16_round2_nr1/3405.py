#include <iostream>
#include <vector>
#include <string>

using namespace std;

string numer;
vector<string> tr = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<string> lic = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

bool CzyPasuje(int x, vector<int> lit)
{
    string s = tr[x];
    for(int i = 0; i < s.length(); ++i)
    {
        if (lit[s[i]-65] - 1 < 0)
        {
            //cout << x << " - " << tr[x] << " " << s[i] << " "<< s[i]-65 << " " << lit[s[i]-65] << endl;
            return false;
        }
    }
    return true;
    //cout << "A";
}

void Szukaj(string s, vector<int> lit, int ile, string nr)
{
    if (ile == 0)
    {
        numer = nr;
        return;
    }
    if (numer != "p")
        return;

    int ost = 0;
    if (nr.length() > 0)
        ost = nr[nr.length()-1] - '0';

    string pnr, p;
    vector<int> plit;
    int pile;
    //cout << " & " << ost << endl;
    for (int i = ost; i <= 9; ++i)
    {
        if (CzyPasuje(i, lit))
        {
            pnr = nr + lic[i];
            string p = tr[i];
            plit = lit;
            for(int j = 0; j < p.length(); ++j)
            {
                plit[p[j]-65]--;
            }
            pile = ile - p.length();
            Szukaj(s, plit, pile, pnr);
        }
    }

}



int main()
{
    int T;

    cin >> T;
    string s;
    string p;

    vector<int> litery;
    int ile;

    for(int t = 1; t <= T; ++t)
    {

        litery.clear();
        litery.resize(26, 0);
        ile = 0;
        cin >> s;
        ile = s.length();
        for (int i = 0; i < s.length(); ++i)
        {
            litery[s[i]-65]++;
        }
        p = "";
        numer = "p";
        Szukaj(s, litery, ile, p);

        cout << "Case #" << t << ": " << numer << endl;

    }

    return 0;
}
