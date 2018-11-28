#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, const char *argv[])
{
	string inputFileName = "B-small-attempt0.in";
	string outputFileName = "B-small-attempt0.out";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    int i, j, k, a, b, t, l, count;

    cin>>t;

    for(l=1; l<=t; l++)
    {
        cin>>a>>b>>k;

        count = 0;

        for(i=0; i<a; i++)
        {
            for(j=0; j<b; j++)
            {
                if((i&j)<k)
                    count++;
            }
        }

        cout<<"Case #"<<l<<": "<<count<<endl;
    }

    return 0;
}
