#include<bits/stdc++.h>
using namespace std;


int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t,k,c,s,i;
    IF >> t;

    for(int tc=1;tc<=t;tc++)
    {
        IF>>k>>c>>s;
         OF << "Case #" << tc << ": ";
         for(i=1;i<=k;i++)
         OF<<i<<" ";
         OF<<endl;

    }

    OF.close();
    IF.close();

}
