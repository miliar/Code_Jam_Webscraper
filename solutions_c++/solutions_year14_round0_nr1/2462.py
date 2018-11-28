#include <iostream>

using namespace std;

int testy;
int tab[5][5];
int rzad;
int powtorzenia[20];
int licznik;
int ktora;

int main()
{
    ios_base::sync_with_stdio(0);

    cin >> testy;

    for(int i=1;i<=testy;i++)
    {
        cin >> rzad;

        for(int j=1;j<=16;j++)
        {
            powtorzenia[j]=0;
        }
        licznik=0;

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin >> tab[j][k];
                if(j==rzad-1)
                {
                    powtorzenia[tab[j][k]]++;
                }
            }
        }

        cin >> rzad;

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin >> tab[j][k];
                if(j==rzad-1)
                {
                    powtorzenia[tab[j][k]]++;
                }
            }
        }

        for(int j=1;j<=16;j++)
        {
            if(powtorzenia[j]==2)
            {
                licznik++;
                ktora=j;
            }
        }

        cout << "Case #" << i << ": ";

        if(licznik==0)
        {
            cout << "Volunteer cheated!" << endl;
        }
        else if(licznik==1)
        {
            cout << ktora << endl;
        }
        else
        {
            cout << "Bad magician!" << endl;
        }
    }

    return 0;
}
