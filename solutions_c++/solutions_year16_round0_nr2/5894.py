#include <iostream>
#include <cstdio>
#include <bitset>

using namespace std;


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("bLarge.out", "w", stdout);
    int N;
    string S;
    cin>>N;

    for(int i=0; i<N; i++)
    {
        cin>>S;
        char current = S[0];

        int numchanges = 0;
        for (char c: S)
        {
            if (c!=current)
            {
                numchanges++;
                current=c;
            }
        }
        if (S[S.length()-1] == '-')
        {
            numchanges++;
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<numchanges<<endl;
    }

    return 0;
}
