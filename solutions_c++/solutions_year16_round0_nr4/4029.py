#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    int i,j,t,k,c,s;
    ofstream output("output small.txt");
    ifstream input("D-small-attempt0.in");
    input >> t;
    for(j=1;j<=t;j++)
    {
        input >> k >> c >> s;
        output << "Case #" << j << ": ";
        for(i=1;i<=k;i++)
            output << i << " ";
        output << endl;
    }
}
