#include <bits/stdc++.h>

using namespace std;

int t;
int n;
int usado[11];
void preenche(int aux)
{
    int a = aux;

    while (a > 0)
    {
        usado[a % 10] = 1;
        a /= 10;
    }
}
bool verifica()
{
    for (int i = 0; i < 10; i++)
        if (!usado[i]) return false;
    return true;
}
int main()
{
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        memset(usado, 0, sizeof(usado));
        cin >> n;
        cout << "Case #" << i + 1 << ": ";

        if (n == 0)
            cout << "INSOMNIA" << endl;
        else
        {
            int aux = 0;
            while (!verifica())
            {
                aux += n;
                preenche(aux);
            }
            cout << aux << endl;
        }
    }

}
