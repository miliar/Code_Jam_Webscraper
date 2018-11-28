
#include "Util.cpp"
#include "IOTemplate.cpp"
//alias
using XX::GT; //(x,y) update x if x > y
using XX::LS; //(x,y) update x if x < y
using XX::UP; //(x,y) comp
using RG = XX::Range;
using XX::MAKEV;
//RD[L],RDV[L],WT[L],WTV[L] for i/o
//template
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <functional>
using namespace std;


char buf[1024];

int main()
{
    int T;
    RD(T);

    for(int tn: RG(1, T + 1))
    {
        printf("Case #%d: ", tn);

        RD(buf);
        string ret;

        for(int i = 0; buf[i]; i++)
            if(ret + buf[i] > buf[i] + ret)
                ret += buf[i];
            else
                ret = buf[i] + ret;

        printf("%s\n", ret.c_str());
    }

}


