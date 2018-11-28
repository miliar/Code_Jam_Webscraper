#include<iostream>
#include<fstream>
#include<cassert>

using namespace std;

ifstream inFile("A-large.in",ios::in);
ofstream oFile("A-large.out",ios::out);

int main()
{
    int t, sMax, countTotal, countInvites;
    string s;

    inFile>> t;

    for(int i=1; i<=t; i++)
    {
        countTotal = 0;
        countInvites = 0;

        inFile>> sMax>> s;

        countTotal += (s[0] - 48);

        for(int j=1; j<=sMax; j++)
        {
            if( j > countTotal )
            {
                countInvites+= (j-countTotal);
                countTotal+= (j-countTotal);
            }

            countTotal += (s[j] - 48);
        }

        oFile<< "Case #"<<i<<": "<< countInvites<<endl;
    }

    return 0;
}
