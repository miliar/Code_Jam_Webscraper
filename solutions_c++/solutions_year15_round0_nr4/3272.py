#include <iostream>
using namespace std;

main ()
{
int powtorzenia;
cin >> powtorzenia;
for (int i=1; i<=powtorzenia; i++)
{
    int a, b, c;
    bool odpowiedz;
    cin >> a >> b >> c;

    if (a==1) odpowiedz=true;
    else if (a==4 && ((b==4 && c==2) || (b==2 && c==4)) ) odpowiedz=false;
    else if (a==6 && ((b==6 && c==3) || (b==3 && c==6)) ) odpowiedz=false;

    else if (a>=2 && a<7)
        {
        if (max(b, c)<a) odpowiedz=false;
        else if (min(b, c)<((a+1)/2)) odpowiedz=false;
        else if ((c*b)%a!=0) odpowiedz=false;
        else odpowiedz=true;
        }

    else if (a>=7) odpowiedz=false;

    cout << "Case #" << i << ": ";
    if (odpowiedz==true) cout << "GABRIEL" << endl;
    if (odpowiedz==false) cout << "RICHARD" << endl;
}
}
