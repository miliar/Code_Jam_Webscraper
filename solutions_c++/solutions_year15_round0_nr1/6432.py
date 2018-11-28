#include <iostream>
using namespace std;

main ()
{
int powtorzenia;
cin >> powtorzenia;
for (int i=1; i<=powtorzenia; i++)
    {
    int n, wynik=0, suma=0;
    cin >> n;

    string a;
    cin >> a;

    for (int k=0; k<a.size(); k++)
        {
        if (suma<k)
            {
            wynik+=k-suma;
            suma=k;
            }

        suma+=a[k]-'0';
        }

    cout << "Case #" << i << ": " <<  wynik << endl;
    }


}
