#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

FILE * oFile=fopen("kits.out", "w");
FILE * iFile=fopen("kits.in", "r");
vector<unsigned long long> fas;
char ksend[50];
unsigned long long b, e, inis[25];
int totes, cases;
bool palin(string kit)
{
    for(int i=0; i<=kit.length()/2; i++)
    {
        if(kit[i]!=kit[kit.length()-1-i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    /*for(unsigned long long i=1; i<=10000000; i++)
    {
        ltoa(i, ksend, 10);
        if(palin(ksend))
        {
            ltoa(i*i, ksend, 10);
            if(palin(ksend))
            {
                fas.push_back(i*i);
            }
        }
    }
    for(int i=0; i<fas.size(); i++)
    {
        fprintf(oFile, "inis[%d]=%d;\n", i, fas[i]);
    }*/
    inis[0]=1;
inis[1]=4;
inis[2]=9;
inis[3]=121;
inis[4]=484;
inis[5]=10201;
inis[6]=12321;
inis[7]=14641;
inis[8]=40804;
inis[9]=44944;
inis[10]=1002001;
inis[11]=1234321;
inis[12]=4008004;
inis[13]=100020001;
inis[14]=102030201;
inis[15]=104060401;
inis[16]=121242121;
inis[17]=123454321;
inis[18]=125686521;
inis[19]=400080004;
inis[20]=404090404;
    fscanf(iFile, "%d", &cases);
    for(int q=1; q<=cases; q++)
    {
        totes=0;
        fscanf(iFile, "%lld%lld", &b, &e);
        for(int i=0; i<=20; i++)
        {
            if(inis[i]<=e && inis[i]>=b)
            {
                totes++;
            }
        }
        fprintf(oFile, "Case #%d: %d\n", q, totes);
    }
    return 0;
}
