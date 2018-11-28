#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("A-large.out");
    int nCases;
    in>>nCases;
    for(int x = 0; x<nCases; x++)
    {
        int smax, current,ans;
        ans = 0;
        current = 0;
        in>>smax;
        string line;
        in>>line;

        for(int i = 0; i<smax+1; i++)
        {
            while(current < i)
            {
                ans += i-current;
                current=i;
            }
            current += line[i] - '0';
        }
        out<<"Case #"<<x+1<<": "<<ans<<endl;
    }
    return 0;
}
