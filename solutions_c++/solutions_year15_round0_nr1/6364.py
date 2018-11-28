#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;


int main ()
{
    ofstream output("outputfile.txt");
    ifstream input("A-large.in");
    int T,i,j,S;
    char ch;
    int ara[1001];
    input>>T;
    for(i=1;i<=T;i++)
    {
        input>>S;
        ch=input.get();
        for(j=0;j<=S;j++) {
            ch=input.get();
            ara[j]=ch-'0';
        }
        int sum = 0;
        int countppl = 0;
        if(ara[0]==0)
        {
            countppl = countppl + 1;
            sum = sum + 1;
        }
        else {
            sum = sum + ara[0];
        }
        for(j=1;j<=S;j++)
        {

         /* if(ara[j]==0)
            {
                continue;
            } */
                if(j>sum) {
                    //countppl = j - sum;
                    countppl++;
                    sum = sum + ara[j] + 1;
                }
                else {
                    sum = sum + ara[j];
                }
            }

        output<<"Case #"<<i<<": "<<countppl<<endl;
    }

    return 0;
}

