#include <iostream>
#include <cstdio>
using namespace std;

int hany,n;
int z[105][105];
int szum[105];


int strki(string s)
{
    for (int i = 0; i<s.length(); i++) printf("%c", s[i]); printf("\n"); return 0;
}



int main()
{
    FILE *out = fopen("ki.txt", "w");






    string s;
    scanf("%d", &hany);
    getline(cin, s);

    for (int ii = 1; ii<=hany; ii++)
    {
        scanf("%d", &n);
        getline(cin, s);
        string k = "";
        bool jo = true;
        int d = 0;
        for (int i = 1; i<=100; i++) szum[i] = 0;
        for (int i = 1; i<=n; i++) if (jo)
        {
            for (int j = 1; j<=100; j++) z[i][j] = 0;

            getline(cin, s);
            string marad;
            marad.push_back(s[0]);

            z[i][1] = 1;
            szum[1]++;

            for (int j = 1; j<s.length(); j++)
            {
                if (marad[marad.length()-1] != s[j]) marad.push_back(s[j]);
                z[i][marad.length()]++;
                szum[marad.length()]++;
            }

            //strki(marad);


            if (k == "") k = marad;
            else
            {
                if (k != marad) jo = false;
            }
        }

        if (jo)
        {
            for (int i = 1; i<=k.length(); i++)
            {
                int cel = szum[i]/n;
                if (szum[i] % n > n/2) cel++;

                for (int j = 1; j<=n; j++)
                {
                    int x = cel - z[j][i]; if (x < 0) x = 0 - x;
                    d+=x;
                }

            }

            printf("Case #%d: %d\n", ii, d);
            fprintf(out, "Case #%d: %d\n", ii, d);
        }
        else
        {
            printf("Case #%d: Fegla Won\n", ii);
            fprintf(out, "Case #%d: Fegla Won\n", ii);
        }



    }

    return 0;
}
