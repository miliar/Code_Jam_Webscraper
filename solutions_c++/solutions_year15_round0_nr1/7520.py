#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t, smax, stand = 0, invite = 0;
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    fin>>t;

    for(int i = 1; i<=t; i++)
    {
        stand = 0, invite = 0;
        fin>>smax;
        char people[smax+2];
        fin>>people;

/**.........................................................*/

        for(int j = 0; j<=smax; j++)
        {
            if(stand>=j)
            {
                stand += (people[j] - '0');
            }
            else
            {
                invite += (j - stand);
                stand += (j - stand + people[j] - '0');
            }
        }
        fout<<"Case #"<<i<<": "<<invite<<endl;
    }
}
