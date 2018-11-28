#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void doCase()
{
    int N, M;
    cin >> N >> M;
    vector<int> o, e, p;
    for(int i=0; i<M; i++)
    {
        int ot, et, pt;
        cin >> ot >> et >> pt;
        o.push_back(ot-1);
        e.push_back(et-1);
        p.push_back(pt);
    }

    long long bestcost = 0;
    vector<int> bestcards;
    for(int stop = 0; stop < N-1; stop++)
    {
        int flux = 0;
        for(int i=0; i<M; i++)
        {
            if(o[i] == stop)
                flux += p[i];
            if(e[i] == stop)
                flux -= p[i];
        }
        if(flux > 0)
        {
            for(int i=0; i<flux; i++)
            bestcards.push_back(N);
        }
        if(flux < 0)
        {
            bestcards.erase(bestcards.end() + flux, bestcards.end());
        }

        for(int i=0; i<bestcards.size(); i++)
        {
            bestcost += bestcards[i];
            bestcards[i]--;
        }
        bestcost %= 1000002013;
    }

    long long faircost = 0;
    for(int i=0; i<M; i++)
    {
        int diff = e[i] - o[i];
        if(diff > 0)
        {
            long long cost = diff*(-diff + 2*N + 1)/2;
            faircost += cost*p[i];
        }
        faircost %= 1000002013;
    }
    cout << (1000002013 + faircost - bestcost) % 1000002013 << endl;
}

int main()
{
    int cases;
    cin >> cases;
    for(int i=0; i<cases; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}

