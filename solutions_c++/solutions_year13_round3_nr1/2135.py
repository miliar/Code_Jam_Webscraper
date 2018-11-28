#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

struct ConsecCons
{
        int _first;
        int _last;
};


int f(int first, int last, int iIdxConsF, int iIdxConsL, vector<ConsecCons> &iVec,map<int, map<int,int> > &iMemo)
{
    ConsecCons &aConsF = iVec[iIdxConsF];
    ConsecCons &aConsL = iVec[iIdxConsL];
    int newFirst = aConsF._first;
    int newLast = aConsL._last;
    
    auto itF =iMemo.find(iIdxConsF);
    if (itF != iMemo.end())
    {
        auto itL = itF->second.find(iIdxConsL);
        if(itL != itF -> second.end()) {
            return 0;//itL -> second;
        }
    }

    if (newFirst < first || last < newLast)
    {
        return 0;
    }

    int result = (newFirst - first +1)* (last - newLast +1);

    if(iIdxConsF < iIdxConsL)
    {
        result += f(aConsF._first+1, last,iIdxConsF+1,iIdxConsL,iVec,iMemo);
        result += f(first, aConsL._last-1,iIdxConsF,iIdxConsL - 1,iVec,iMemo);
    }
    iMemo[iIdxConsF][iIdxConsL]=result;
    return result;
}


int main() {
    unsigned int pb_size;
    cin >> pb_size;


    for (unsigned int pb_idx = 1;pb_idx <= pb_size;++pb_idx)
    {
        cerr << "Case #" << pb_idx << endl;
        string name;
        unsigned int n =0;
        cin >> name >> n;

        vector<ConsecCons> consecCons;
        int firstCons = -1;
        
        for (int i=0;i< name.size();i++)
        {
            if (!(name[i] == 'a' || name [i] == 'e' || name [i] == 'i'
                  || name [i] == 'o' || name [i] == 'u'))
            {
                if (firstCons == -1 )
                {
                    firstCons = i;
                }
                int first = firstCons;
                int last = i;
                
                if (last - first +1 >=n)
                {
                    consecCons.push_back(ConsecCons());
                    consecCons.back()._first = last - n+1;
                    consecCons.back()._last = last;
                }
            }
            else
            {
                firstCons = -1;
            }
        }


        int result = 0;
        if (!consecCons.empty())
        {
            map<int,map<int,int> > aMemo;
            result = f(0,name.size()-1,0,consecCons.size()-1,consecCons,aMemo);       
        }
        cout << "Case #" << pb_idx <<": " << result << endl;

    }
}
