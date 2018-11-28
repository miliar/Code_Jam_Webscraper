#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>> t;

    for (int i = 1; i<=t; i++)
    {
        priority_queue<pair<int, char> > pq;
        int n;
        cin>>n;
        for(int k  = 0; k<n; k++)
        {
            int p;
            cin>>p;
            pair<int, char> pp;
            pp.first = p;
            pp.second = 'A'+ k;
            pq.push(pp);
        }

        cout<<"Case #"<<i<<": ";
        while(pq.size() > 2)
        {
            pair<int, char> p = pq.top();
            pq.pop();

            cout <<p.second<<" ";

            if (p.first > 1)
            {
                pair <int, char> pp;

                pp.first = p.first-1;
                pp.second = p.second;

                pq.push(pp);
            }
        }

        pair<int, char> one = pq.top();
        pq.pop();
        char fs = one.second;
        int fn = one.first;

        pair<int, char> sec = pq.top();
        char ss = sec.second;
        int  sn = sec.first;
        pq.pop();

        while(fn > sn)
        {
            cout<<fs<<" ";
            fn --;
        }

        for (int h  = 0; h < fn; h++)
        {
            cout<<fs<<ss<<" ";
        }
        cout<<endl;
    }
    return 0;
}
