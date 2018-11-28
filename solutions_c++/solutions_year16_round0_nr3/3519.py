#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
#include <bitset>
#include <set>
#include <cmath>

using namespace std;
typedef long long ll;

vector <string> validos;

ll k[11][17];

ll divisor;

bool isPrime(ll n)
{
    if(n == 1 || n == 2)
        return true;
    if(n%2 == 0)
    {
        divisor = 2;
        return false;
    }
    ll lim = sqrt(n);
    for(ll i=3; i<=lim; i+=2)
        if(n%i == 0)
        {
            divisor = i;
            return 0;
        }
    return 1;
}

vector <ll> div;

ll calcDivisor (ll a)
{
    for(ll i=2; i<a; i++)
        if(a%i == 0)
            return i;
}

ll b[11];
bool esValido(string s)
{
    for(int i=0; i<s.size()/2; i++)
        swap(s[i], s[s.size()-i-1]);

    for(int i=0; i<11; i++)
        b[i] = 0;

    for(int i=2; i<=10; i++)
    {
        for(int j=0; j<s.size(); j++)
            if(s[j] == '1')
                b[i] += k[i][j];
        if(isPrime(b[i]))
        {
            div.clear();
            return false;
        }
        divisor = calcDivisor(b[i]);
        div.push_back(divisor);
    }
    /*
    for(int i=2; i<=10; i++)
        cout << b[i] << " = " << div[i-2] << endl;
    */
    return true;
}

ll l, z;

void generar(int largo)
{
    //ofstream out("out.txt");
    largo-=2;
    int maxP = 1;
    for(int i=0; i<largo; i++)
        maxP *= 2;

    cout << "Case #1:" << endl;
    int cantValidos = 0;
    for(int i=0; i<maxP && cantValidos < z; i++)
    {
        bitset<35>b(i);
        string s = "1" + b.to_string().substr(35-largo, largo) + "1";
        div.clear();
        if(esValido(s))
        {
            cantValidos++;
            cout <<  s;
            for(int i=0; i<9; i++)
                cout << " " << div[i];
            cout << endl;
        }
    }
    //out.close();
}

int main()
{
    for(int i=1; i<11; i++)
        k[i][0] = 1;

    for(int i=1; i<11; i++)
        for(int j=1; j<17; j++)
            k[i][j] = k[i][j-1]*i;

    ifstream in("in");

    in >> l;
    in >> l >> z;

    in.close();

    generar(l);
    return 0;
}
