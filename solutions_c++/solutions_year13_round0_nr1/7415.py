#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;
const ll A=(1LL<<4)-1;
const ll B=(1LL<<8)-1-A;
const ll C=(1LL<<12)-1-B-A;
const ll D=(1LL<<16)-1-C-B-A;
const ll E=(1LL)|(1LL<<5)|(1LL<<10)|(1LL<<15);
const ll F=(1LL<<3)|(1LL<<6)|(1LL<<9)|(1LL<<12);
const ll G=(1LL)|(1LL<<4)|(1LL<<8)|(1LL<<12);
const ll H=(1LL<<1)|(1LL<<5)|(1LL<<9)|(1LL<<13);
const ll I=(1LL<<2)|(1LL<<6)|(1LL<<10)|(1LL<<14);
const ll J=(1LL<<3)|(1LL<<7)|(1LL<<11)|(1LL<<15);
int main()
{
    int T,i,cas=0;
    ll s1,s2;
    char c;
    ifstream fin("A-large.in");
    ofstream fout("gcj1.out");
//    cin>>T;
    fin>>T;
    while(T--)
    {
        cas++;
        s1=0,s2=0;
        for(i=0;i<16;++i)
        {
//            cin>>c;
            fin>>c;
            if(c=='X')
                s1|=(1LL<<i);
            else if(c=='O')
                s2|=(1LL<<i);
            else if(c=='T')
                s1|=(1LL<<i),s2|=(1LL<<i);
        }
        if((s1&A)==A||(s1&B)==B||(s1&C)==C||(s1&D)==D||(s1&E)==E||(s1&F)==F||(s1&G)==G||(s1&H)==H||(s1&I)==I||(s1&J)==J)
            fout<<"Case #"<<cas<<": X won"<<endl;
        else if((s2&A)==A||(s2&B)==B||(s2&C)==C||(s2&D)==D||(s2&E)==E||(s2&F)==F||(s2&G)==G||(s2&H)==H||(s2&I)==I||(s2&J)==J)
            fout<<"Case #"<<cas<<": O won"<<endl;
        else if((s1|s2)==((1LL<<16)-1))
            fout<<"Case #"<<cas<<": Draw"<<endl;
        else
            fout<<"Case #"<<cas<<": Game has not completed"<<endl;
    }
    return 0;
}