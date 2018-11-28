#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int T;
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream fin("ovation.in");
    ofstream fout("ovation.out");

    fin>>T;
    for(int t=0; t<T; ++t)
    {
        int Smax;
        fin>>Smax;
        string audience;
        int guest=0;
        int additional=0;
        fin>>audience;
        for(int i=0; i<=Smax; ++i)
        {
            if(audience[i]-'0')
            {
                if(guest + additional < i)
                    additional = i -guest;
                guest+=audience[i]-'0';
            }
        }
        fout<<"Case #"<<t+1<<": "<<additional<<"\n";
    }
    return 0;
}
