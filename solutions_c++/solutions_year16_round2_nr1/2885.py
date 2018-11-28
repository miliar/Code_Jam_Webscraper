#include <bits/stdc++.h>
#define rep(a,b) for(int a = 0; a < b; a++)
#define fora(a,b,e) for(int a = b; a <= e; a++)
#define fore(a,b,e) for(int a= b; a >= e; a--)
#define SIZE(x) (int)x.size()
#define var(a,b) __typeof(b) a = b
#define foreach(a,b) for(var(a, (b).begin()); a != (b).end(); a++)
#define st first
#define nd second

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

//"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
int alf[27];
int main()
{
    ios_base::sync_with_stdio(0);
    int ty;
    cin >> ty;

    string str, odp;
    int whi = 1;
    while(ty--)
    {
        odp = "";
        cin >> str;
        cout << "Case #" << whi <<  ": ";
        for(int i = 0; i < 27; i++) alf[i] = 0;

        for(int i = 0; i < str.size(); i++)
        {
            alf[str[i]-'A']++;
        }

        //zero
        while(alf['Z'-'A'] > 0 && alf['E'-'A']  > 0 && alf['R'-'A']> 0 && alf['O'-'A'] > 0)
        {
           odp += '0';
           alf['Z'-'A']--;
           alf['E'-'A']--;
            alf['R'-'A']--;
            alf['O'-'A']--;
        }




        //two
        while(alf['T'-'A'] > 0 && alf['W'-'A']  > 0 && alf['O'-'A'] > 0)
        {
            odp += '2';
            alf['T'-'A']--;
            alf['W'-'A'] --;
            alf['O'-'A']--;
        }



        //four
        while(alf['F'-'A'] > 0 && alf['O'-'A']  > 0 &&alf['U'-'A']  > 0 && alf['R'-'A']> 0)
        {
            odp += '4';
            alf['F'-'A'] --;
            alf['O'-'A']--;
            alf['U'-'A'] --;
            alf['R'-'A']--;
        }


        //five
        while(alf['F'-'A']  > 0 && alf['I'-'A'] > 0 && alf['V'-'A'] > 0 && alf['E'-'A']> 0)
        {
            odp += '5';
            alf['F'-'A'] --;
            alf['I'-'A']--;
            alf['V'-'A'] --;
            alf['E'-'A']--;
        }

        //three
        while(alf['T'-'A'] > 0 && alf['H'-'A'] > 0 && alf['R'-'A']> 0 && alf['E'-'A'] > 1)
        {
            odp += '3';
            alf['T'-'A']--;
            alf['H'-'A'] --;
            alf['R'-'A']--;
            alf['E'-'A']-=2;
        }



        //eight
        while(alf['E'-'A'] > 0 && alf['I'-'A']> 0 && alf['G'-'A']  > 0 && alf['H'-'A']  > 0 && alf['T'-'A'] > 0)
        {
            odp += '8';
            alf['E'-'A']--;
           alf['I'-'A']--;
            alf['G'-'A'] --;
            alf['H'-'A'] --;
            alf['T'-'A']--;
        }

         //seven
        while(alf['S'-'A']  > 0 && alf['E'-'A']  > 1 && alf['V'-'A']  > 0 && alf['N'-'A'] > 0)
        {
            odp += '7';
            alf['S'-'A']--;
            alf['E'-'A'] -=2;
            alf['V'-'A'] --;
            alf['N'-'A']--;
        }
        //six
        while(alf['S'-'A']> 0 && alf['I'-'A']> 0 && alf['X'-'A']  > 0)
        {
            odp += '6';
            alf['S'-'A']--;
            alf['I'-'A']--;
            alf['X'-'A'] --;
        }
          //one
       while(alf['O'-'A'] > 0 && alf['N'-'A'] > 0 && alf['E'-'A'] > 0)
       {
           odp+= '1';
           alf['O'-'A']--;
          alf['N'-'A']--;
          --alf['E'-'A'];
       }
        //nine
        while(alf['N'-'A'] > 1 &&alf['I'-'A']> 0 && alf['E'-'A'] > 0)
        {
            odp += '9';
            alf['N'-'A'] -=2;
            alf['I'-'A']--;
            alf['E'-'A']--;
        }
        sort(odp.begin(), odp.end());
        cout << odp << "\n";
        whi++;
    }
}
