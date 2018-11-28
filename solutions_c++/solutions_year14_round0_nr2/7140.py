#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;

int A1[20][20],A2[20][20];
int a1[20], a2[20];
int main()
{
    ofstream ofile;
    ifstream ifile;
    ofile.open("output.txt");
    ifile.open("input.txt");
    int T;
    ifile>>T;
    
    for(int zz = 0; zz<T; zz++)
    {
        double C, F, X;
        ifile>>C>>F>>X;
        int flag = 0;
        int i = 0;
        double tottime = 0.0;
        
        while(flag == 0)
        {
            double rate = 2 + i*F;
            double newrate = 2 + (i+1)*F;
            double curtime = (X/rate);
            double nexttime = (C/rate + X/newrate);
            
            if(curtime<=nexttime)
            {
                flag = 1;
                tottime += curtime;
            }
            else tottime += C/rate;
            i++;
        }
        ofile<<"Case #"<<(zz+1)<<": "<<setprecision(18)<<tottime<<endl;
    }
    return 0;
}
            
            
            
