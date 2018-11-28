#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void xchg(int &a, int &b)
{
    int c = b;
    b = a;
    a = c;
}

int max(int a, int b)
{
    if(a>b)
        return a;
    return b;
}

void captured(int d1, int d2, int w, int l1, int l2, int l3, int l4, int &s, int &c)
{
    s = 2*d1 + 2*d2 +2*w;
    if(d1 == 1)
        s -= 2;
    c = s + d1*(d2-1) + d2*(d1-1) + w*(d1+d2-2);
    for(int i = 1; i<=l1; i++)
    {
        s += 1;
        c += max(d1,2)-i;
    }
    for(int i = 1; i<=l2; i++)
    {
        s += 1;
        c += max(d1,2)-i;
    }
    for(int i = 1; i<=l3; i++)
    {
        s += 1;
        c += d2-i;
    }
    for(int i = 1; i<=l4; i++)
    {
        s += 1;
        c += d2-i;
    }
}

int main(int argc, char **argv)
{
    fstream input;
    int t;
    input.open(argv[1], fstream::in);
    input >> t;
    for(int i = 1; i<=t; i++)
    {   
        int k, m, n, s, c;
        input >> n >> m >> k;
        if(m>n)
            xchg(m,n);
        if (m<3 || k<4)
            s = k;
        else 
        {
            int min_s = m*n;
            for(int d1 = 1; d1<=m/2; d1++)
                for(int d2 = 2; d2+d1<=m; d2++)
                    for(int w = 0; d1+d2+w<=n; w++)
                        for(int l1 = 0; l1<max(d1,2); l1++)
                            for(int l2 = 0; l2<max(d1,2); l2++)
                                for(int l3 = 0; l3<d2; l3++)
                                    for(int l4 = 0; l4<d2; l4++)
                                    {
                                        //cout << "State d1: " << d1 <<" d2: " << d2  << " w: " << w << " l1: " << l1 << " l2: " << l2 << " l3: " << l3 << " l4: " << l4 << endl;
                                        captured(d1, d2, w, l1, l2, l3, l4, s, c);
                                        if(c>=k && s<min_s)
                                        {
                                            //cout << "State d1: " << d1 <<" d2: " << d2  << " w: " << w << " l1: " << l1 << " l2: " << l2 << " l3: " << l3 << " l4: " << l4 << endl;
                                            min_s = s;
                                        }
                                    }
             s = min_s;
        }
        cout << "Case #" << i << ": " << s << endl;

    }
}
