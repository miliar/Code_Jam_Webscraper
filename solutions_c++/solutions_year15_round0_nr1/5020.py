#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;


int main ()
{
    ifstream in("INPUT.TXT ");
    ofstream out("OUTPUT.TXT");
    int T = 0; // number of tests
    int Smax;
    char Sall[1002];
    int k[1002];
    int stands = 0;
    int friends = 0;
    in >> T;
    for (int iT=0;iT<T;iT++)
    {
        //cout<<"iT "<<iT<<endl;

        in >> Smax;
        in >> Sall;
        //cout<<"Smax "<<Smax<<endl;
        //cout<<"Sall "<<Sall<<endl;
        for (int ik = 0;ik<=Smax;ik++)
        {
            k[ik] = Sall[ik] - '0';
            //cout<<"k "<<k[ik]<<endl;
        }
        stands = k[0];
        for (int shy_level=1;shy_level<=Smax;shy_level++)
        {
            //cout<<"stands "<<stands<<"  shy_level "<<shy_level<<endl;
            if (stands >= shy_level) stands+=k[shy_level];
            else
            {
                friends+=shy_level - stands;
                stands+= shy_level - stands + k[shy_level];
                //cout<<"friends  "<<friends<<endl;
            }
        }
        out<<"Case #"<<iT+1<<": "<<friends<<endl;
        stands = 0;
        friends = 0;

    }








    return 0;
}
