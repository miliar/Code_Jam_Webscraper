#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n;
double a[10005];
double b[10005];
bool v[10005];

double p1(double x)
{
    int i,j;
    for(i=0; i<n; ++i)
        if(!v[i] && b[i]>x)
        {
            j = i;
            break;
        }
    if(i == n)
        for(i=0; i<n; ++i)
            if(!v[i])
            {
                j = i;
                break;
            }

    v[j] = true;
    return b[j];
}

double getMin()
{
    int i;
    for(i=0; i<n; ++i)
        if(!v[i])
            return b[i];
    return 0;
}

void removeMin()
{
    int i;
    for(i=0; i<n; ++i)
        if(!v[i])
        {
            v[i] = true;
            return;
        }
    return;
}

void removeMax()
{
    int i;
    for(i=n-1; i>=0; --i)
        if(!v[i])
        {
            v[i] = true;
            return;
        }
    return;
}

double p2(double x)
{
    int i,j;
    for(i=n-1; i>=0; --i)
        if(!v[i] && b[i]>x)
        {
            j = i;
            break;
        }

    if(i==-1)
        for(i=0; i<n; ++i)
            if(!v[i])
            {
                j = i;
                break;
            }

    v[j] = true;
    return b[j];
}

int main()
{
    int i,t,tt,k1=0,k2=0;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>n;
        for(i=0; i<n; ++i)
            fin>>a[i];
        for(i=0; i<n; ++i)
            fin>>b[i];
        
        sort(a, a+n);
        sort(b, b+n);

        k1 = k2 = 0;
        for(i=0; i<n; ++i)
            v[i] = 0;
        
        for(i=0; i<n; ++i)
            if(p1(a[i])<a[i])
                ++k1;            
        
        for(i=0; i<n; ++i)
            v[i] = 0;
        int n2 = n;

        for(i=0; i<n2; ++i)
        {
            if(getMin()<a[i])
            {
                removeMin();
                k2++;
            }
            else
                removeMax();
        }
        fout << "Case #" << t << ": "<< k2 << ' ' << k1 << endl;        
    }
    return 0;
}

