#include "bits/stdc++.h"

using namespace std;

int main()
{
    ifstream in ("A-large.in");
    ofstream out ("output.txt");

    int t;

    in>>t;

    for(int cn = 1;cn<=t;++cn)
    {
        int present = 0,standing = 0,invited = 0;
        string people;
        int s_max;
        in>>s_max>>people;
        for(present = 0;present<=s_max;++present)
        {
            if(standing >= present)
            {
                standing += people[present] - '0';
            }
            else if(people[present] > '0')
            {
                invited += present - standing;
                standing = present + people[present] - '0';
            }
        }
        out<<"Case #"<<cn<<": "<<invited<<"\n";
    }
    return 0;
}
