#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int cant, hay;
bool masDeLaMitad;

int maxV(vector <int> a, int n)
{
    int m=0, p = -1;
    cant = 0;
    masDeLaMitad = false;
    for(int i=0; i<n; i++)
    {
        cant += a[i];
        if(m < a[i])
        {
            m = a[i];
            p = i;
        }
    }

    ///Saco a[p]
    int saco = a[p]-1;
    int otro = cant-a[p];

    //cout << saco << " " << otro << endl;

    if(saco >= otro)
        masDeLaMitad = true;

    return p;
}

int main()
{
    ifstream in("in.in");
    ofstream out("out.txt");
    int tc;
    in >> tc;
    for(int w=1; w<=tc; w++)
    {
        int n;
        in >> n;

        vector <int> a(n);

        for(int i=0; i<n; i++)
            in >> a[i];

        ///Los saco de a 1

        out << "Case #" << w << ":";
        int init = 0;
        int k = maxV(a, n);
        while(k != -1)
        {
            if(cant > 1 && (!masDeLaMitad || init%2 == 0))
                out << " ";
            out << (char)(k+'A');
            a[k]--;
            k = maxV(a, n);
            init++;
        }
        out << endl;
    }
    return 0;
}
