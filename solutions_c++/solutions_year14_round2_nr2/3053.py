//Md. Khairullah Gaurab
//SUST, CSE
//20th Batch
//gaurab.cse.sust@gmail.com

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <numeric>
#include <utility>

#define sf scanf
#define pf printf

using namespace std;

int main(int argc, const char *argv[])
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_small.txt","w",stdout);
    int test, ways, A, B, K;
    cin>>test;
    for(int i=1; i<=test; i++)
    {
        cin>>A>>B>>K;
        ways = 0;
        for(int i=0; i<min(A,B); i++)
        {
            for(int j=0; j<max(A,B); j++)
            {
                if((i&j)<K) ways++;
            }
        }

        cout<<"Case #"<<i<<": "<<ways<<"\n";

    }
	return 0;
}
