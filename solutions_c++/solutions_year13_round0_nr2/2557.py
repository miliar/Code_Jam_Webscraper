#include<iostream>
#include<algorithm>
#include<map>
#include<list>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    int cN;
    cin >> cN;
    for(int ci=0; ci<cN; ++ci)
    {
        map<int, list<pair<int, int>>> hlmap;
        int grass[101][101] = {0};
        int grassTest[101][101] = {100};
        int N, M;
        cin >> N;
        cin >> M;
        //ilarge = -1;
        for(int ni = 0; ni<N; ++ni)
        {
            for(int mi=0; mi<M; ++mi)
            {
                cin >> grass[ni][mi];
                pair<int, int> p(ni, mi);
                hlmap[grass[ni][mi]].push_back(p);
                grassTest[ni][mi] = -1;
            }
        }
        bool cando = true;
        map<int, list<pair<int, int>>>::reverse_iterator miter;
        for(miter = hlmap.rbegin(); miter!=hlmap.rend(); ++miter)
        {
            cando = true;
            //cout << miter->first << "," << miter->second.size() << endl;
            list<pair<int, int>>::iterator lpr;
            for(lpr = miter->second.begin(); lpr!=miter->second.end(); ++lpr)
            {
                pair<int, int> pr = *lpr;
                //cout << pr.first << "," << pr.second << endl;
                if(grassTest[pr.first][pr.second]==grass[pr.first][pr.second])
                {
                    continue;
                }
                int val = grass[pr.first][pr.second];
                //try to ->                
                for(int i=0; i<M; ++i)
                {

                    if( grassTest[pr.first][i] > val && grass[pr.first][i] > val)
                    {
                        cando = false;
                        break;
                    }
                }
                if(cando)
                {
                    for(int i=0; i<M; ++i)
                    {
                        grassTest[pr.first][i] = val;
                    }
                    continue;
                }
                bool pcando = true;
                for(int i=0; i<N; ++i)
                {
                    if( grassTest[i][pr.second] > val && grass[i][pr.second] > val)
                    {
                        pcando = false;
                        break;
                    }
                }
                if(pcando)
                {
                    cando = true;
                    for(int i=0; i<M; ++i)
                    {
                        grassTest[i][pr.second] = val;
                    }
                }
                if(!cando)
                {
                    break;
                }
            }
            if(!cando)
            {
                break;
            }
        }
        if(cando)
        {
            printf("Case #%d: YES\n", ci+1);
        }
        else
        {
            printf("Case #%d: NO\n", ci+1);
        }
    }
	return 0;
}

