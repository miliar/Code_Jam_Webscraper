#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;

    scanf("%d", &T);
    int L = T;
    while(T--){
        string s;
        cin >> s;
        vector<int> fone;
        map<char, int> mapa;
        int t = s.size();
        for(int i = 0; i < s.size(); i++)
        {
            mapa[s[i]]++;
        }
        while(t)
        {
            int x = t;
            int k = mapa['Z'];
            t -= 4*k;
            mapa['Z'] -= k;
            mapa['E'] -= k;
            mapa['R'] -= k;
            mapa['O'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(0);

            k = mapa['W'];
            t -= 3*k;
            mapa['W'] -= k;
            mapa['T'] -= k;
            mapa['O'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(2);

            k = mapa['X'];
            t -= 3*k;
            mapa['X'] -= k;
            mapa['S'] -= k;
            mapa['I'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(6);

            k = mapa['G'];
            t -= 5*k;
            mapa['G'] -= k;
            mapa['E'] -= k;
            mapa['I'] -= k;
            mapa['H'] -= k;
            mapa['T'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(8);

            k = mapa['U'];
            t -= 4*k;
            mapa['F'] -= k;
            mapa['O'] -= k;
            mapa['U'] -= k;
            mapa['R'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(4);

            k = mapa['T'];
            t -= 5*k;
            mapa['T'] -= k;
            mapa['H'] -= k;
            mapa['R'] -= k;
            mapa['E'] -= 2*k;
            for(int i = 0; i < k; i++)
                fone.push_back(3);

            k = mapa['O'];
            t -= 3*k;
            mapa['O'] -= k;
            mapa['N'] -= k;
            mapa['E'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(1);

            k = mapa['S'];
            t -= 5*k;
            mapa['S'] -= k;
            mapa['E'] -= 2*k;
            mapa['V'] -= k;
            mapa['N'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(7);

            k = mapa['N']/2;
            t -= 4*k;
            mapa['N'] -= k;
            mapa['I'] -= k;
            mapa['E'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(9);

            k = mapa['F'];
            t -= 4*k;
            mapa['F'] -= k;
            mapa['I'] -= k;
            mapa['V'] -= k;
            mapa['E'] -= k;
            for(int i = 0; i < k; i++)
                fone.push_back(5);
        }
        cout << "Case #" << L-T << ": ";
        sort(fone.begin(), fone.end());
        for(int i = 0; i < fone.size(); i++)
            printf("%d", fone[i]);
        cout << endl;


    }
}
