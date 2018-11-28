#include <fstream>
#include <queue>
#include <vector>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");
ifstream fin("nums.txt");

const int N = 32;
const int J = 500;

typedef unsigned long long tlong;

vector<tlong> v;
int CNT=0;
tlong dv[20];

tlong gcd(tlong a, tlong b)
{
    if (!b) return a;
    return gcd(b, a % b);
}

int cifl[16], cifr[16];

void desc(tlong x, int cif[16])
{
    int p = 0;
    while (x > 0)
    {
        cif[p++] = x % 10;
        x /= 10;
    }
    if (p != 16)
        g << "<<<<<<<<<<<WRONG!!!!!!!\n";
}

int main()
{
    g << "Case #1:\n";
    
    tlong x; 
    while (fin >> x)
        v.push_back(x);
    
    dv[3] = dv[5] = dv[7] = dv[9] = 2;
    for (tlong l : v)
        for (tlong r : v)
        {
            dv[10] = gcd(l, r);
            if (dv[10] <= 1)
                continue;
            desc(l, cifl);
            desc(r, cifr);
            
            bool ok = true;
            for (int p=2; p<=8; p+=2)
            {
                tlong pw = 1;
                tlong nl = 0, nr = 0;
                for (int i=0; i<16; i++)
                {
                    nl += 1LL * cifl[i] * pw;
                    nr += 1LL * cifr[i] * pw;
                    if (i+1 < 16)
                        pw *= p;
                }
                dv[p] = gcd(nl, nr);
                if (dv[p] <= 1)
                {
                    ok = false;
                    break;
                }
            }
            
            if (ok)
            {
                g << l << r << ' ';
                for (int p=2; p<=10; p++)
                    g << dv[p] << ' ';
                g << '\n';
                CNT++;
                if (CNT >= J)
                {
                    //g << "FINISHED\n";
                    return 0;
                }
            }
        }
    
    f.close();
    g.close();
    
    
    return 0;
}