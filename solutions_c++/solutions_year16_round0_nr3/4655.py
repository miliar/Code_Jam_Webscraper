
#include <iostream>
#include <fstream>
#include <map>

using namespace std;
ofstream out("coinJam.out");
ifstream in("coinJam.in");

int x[100];
int v[100];
int nrSol;
int J;
int n;
int m;
map<string,bool> visited;

bool isPrim(unsigned long long x)
{
    if( x < 2 )
        return 0;
    if( x > 2 && x % 2 == 0)
        return 0;
    for(unsigned long long d = 3;  d*d <=x; d+=2)
        if(x % d == 0)
        return 0;
    return 1;
}

unsigned long long put(unsigned long long number, int put)
{
    unsigned long long prod = 1;
    for(int i = 1 ; i<=put; ++i)
        prod*= number;
    return prod;
}

unsigned long long computeNumber(int* v, int puterea)
{
    unsigned long long sum = 0;
    for(int j = 1 ; j<=m; ++j)
    {
        if(v[j] != 0)
        {
            sum = sum + put(puterea,j-1);
        }
    }

    return sum;
}

unsigned long long getDivizor(unsigned long long number)
{
    if(number % 2 == 0)
        return 2;
    unsigned long long d;
    for(d = 3 ; d*d <=number; d+=2)
        if(number % d == 0)
            return d;
}

void write()
{
    m = 16;
    string rezult = "1";
    v[1] = 1;
    v[m] = 1;
    int p = 1;
    for(int i = 1 ; i<=n;++i)
    {
        v[++p] = x[i];
        if(x[i] == 0)
        {
            rezult += "0";
        }
        else
        {
            rezult += "1";
        }
    }
    rezult += "1";
    if(visited[rezult] == 0)
    {
        visited[rezult] = 1;
    /*for(int i = 1 ; i<=m;++i)
        cout << v[i];
    cout << '\n';
    */
    bool ok = true;
    for(int i = 2 ; i<=10 && ok; ++i)
    {
        //i este puterea
        unsigned long long sum = 0;
        for(int j = 1 ; j<=m; ++j)
        {
            if(v[j] == 1)
                sum = sum + put(i,j-1);
        }

        if(isPrim(sum))
        {
            ok = false;
        }
    }

    if(ok)
    {
        ++nrSol;
        if(nrSol <= J)
        {
            for(int i = 1; i<=m;++i)
                out << v[i];
            out << " ";

            for(int i = 2 ; i<=10; ++i)
            {
                unsigned long long rezult = computeNumber(v,i);
                //out << rezult << " ";
                out << getDivizor(rezult);
                //cout << '\n';
                out << " ";
            }

            out << '\n';
        }

      }

    }

}



void back(int k)
{
    for(int i =0; i<=1; ++i){
        x[k] = i;
        if( k == n)
        {
            write();
        }
        else
            back(k+1);
    }
}
int main()
{
    int T;
    in >> T;
    for(;T;--T)
    {
        in >> n >> J;
        n-=2;
        out <<"Case #1:" << '\n';
        back(1);
    }

    return 0;
}
