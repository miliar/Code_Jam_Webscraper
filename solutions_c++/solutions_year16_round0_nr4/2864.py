#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        int k,c,s; IF >> k >> c >> s;
        OF << "Case #" << tt << ": ";
        for(int i=1;i<=k;i++)
            OF << i << " ";
        OF << endl;
    }
    OF.close(); IF.close();
}

