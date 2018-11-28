#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

bool isFair(long long num)
{
    bool fair = true;
    char p[200];
    memset(p,0,200);
    lltoa(num,p,10);
    //cout<<p<<endl;
    string str(p);
    int strLen = str.length();
    for(int jsp=0; jsp<=(strLen-1)/2; jsp++)
    {
        if(str[jsp]!=str[strLen-jsp-1])
        {
            fair = false;
            break;
        }
    }
    return fair;
}

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream out("C-small-attempt0.out");
    int T;
    fin>>T;
    int i;
    for(i=0; i<T; i++)
    {
        long long A, B;
        fin>>A>>B;
        long long numOfFaSq = 0;
        long long lbound = floor(sqrt(A));
        long long ubound = ceil(sqrt(B));
        for(long long num=lbound; num<=ubound; num++)
        {
            long long sqNum = num*num;
            if(sqNum<A || sqNum>B)
                continue;
            if(isFair(num)&&isFair(sqNum))
            {
                //cout<<"Case #"<<i+1<<": "<<sqNum<<endl;
                numOfFaSq++;
            }
        }
        out<<"Case #"<<i+1<<": "<<numOfFaSq<<endl;

    }

    fin.close();
    out.close();
    return 0;
}
