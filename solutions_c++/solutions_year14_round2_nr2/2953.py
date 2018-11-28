#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("B-small-attempt0.in");
    ofstream output("output.txt");
    long long testCases;
    input>>testCases;
    for(long long tc=1;tc<=testCases;tc++)
    {
        long long a,b,k;
        input>>a>>b>>k;
        long long answer=0;
        for(long long ai=0;ai<a;ai++)
        {
            for(long long bi=0;bi<b;bi++)
            {
                if((ai&bi)<k)
                {
                    answer++;
                }
            }
        }
        output<<"Case #"<<tc<<": "<<answer<<endl;
    }
    return 0;
}
