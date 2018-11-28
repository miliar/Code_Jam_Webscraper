#include <fstream>

using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t,smax,sum,ris;
    string s;
    in >> t;
    for(int i=0; i<t; i++)
    {
        sum=ris=0;
        in >> smax;
        int ris = 0;
        in>>s;
        for(int j=0; j<=smax; j++)
        {

            if(j>0 && s[j]>'0')
            {
                ris+=max(j-sum,0);
                sum+=max(j-sum,0);
            }

            sum+=s[j]-'0';

        }
        out << "Case #" << i+1 << ": " << ris << endl;

    }
    return 0;
}
