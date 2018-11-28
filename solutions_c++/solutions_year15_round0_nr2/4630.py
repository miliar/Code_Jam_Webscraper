#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<queue>
using namespace std;

struct PlateState
{
    int round;
    vector<int> plates;
    PlateState() : round(0) {}

};
int main(void)
{
    int T;
    cin >> T;
    for(int Ti=0; Ti<T; ++Ti)
    {
        int D;
        cin >> D;
        vector<int> plates;
        for(int i=0; i<D; ++i)
        {
            int p;
            cin >> p;
            plates.push_back(p);
        }
        int round = 0;
        queue<PlateState> theQ;
        PlateState initP;
        initP.plates = plates;
        theQ.push(initP);
        while(!theQ.empty())
        {
            PlateState ps = theQ.front();
            vector<int> pp = ps.plates;
            vector<int> eat = pp;
            theQ.pop();
            int tot=0;
            int mostI=0;
            int mostP=pp[0];
            for(int i=0; i<eat.size(); ++i)
            {
                if(eat[i]>0)
                {
                    --eat[i];
                }
                tot+=eat[i];
                if(pp[i]>mostP)
                {
                    mostI=i;
                    mostP=pp[i];
                }
            }
            if(tot==0)
            {
                round = ps.round+1;
                break;
            }
            {
                PlateState newPS;
                newPS.plates = eat;
                newPS.round = ps.round+1;
                theQ.push(newPS);
            }
            for(int g=2; g<mostP/2+1; ++g)
            {
                vector<int> npp = pp;
                npp.push_back(g);
                npp[mostI]=npp[mostI]-g;
                PlateState newPS;
                newPS.plates = npp;
                newPS.round = ps.round+1;
                theQ.push(newPS);
            }
        }
        cout << "Case #" << (Ti+1) << ": " << round << endl;
    }

	return 1;
}