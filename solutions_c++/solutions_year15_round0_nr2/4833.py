#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#include<utility>
#include<algorithm>

using namespace std;

int split(vector<int> &panck, int maxpk, int result, int resultref)
{
    int res = result + maxpk;
    resultref = min(resultref, res);
    if(maxpk == 1)
        return resultref;
    else
    {
        if(result >= resultref)
            return resultref;
        else
        {
            for(int k = 1; k <= maxpk/2; k++)
            {
                int stockp = panck[maxpk];
                int stockmaxpk = maxpk;
                int stockresult = result;
                result = result + panck[maxpk];
                int splita = k;
                int splitb = maxpk - splita;
                panck[splita] += panck[maxpk];
                panck[splitb] += panck[maxpk];
                panck[maxpk] = 0;
                while(panck[maxpk] == 0)
                    maxpk--;
                result = split(panck, maxpk, result, resultref);
                if(result < resultref)
                    resultref = result;
                panck[splita] -= stockp;
                panck[splitb] -= stockp;
                panck[stockmaxpk] = stockp;
                maxpk = stockmaxpk;
                result = stockresult;
            }
            return resultref;
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        vector<int> panck(1001,0);
        int D;
        cin >> D;
        int maxpk = 0;
        for(int j = 0; j < D; j++)
        {
           int Pi;
           cin >> Pi;
           panck[Pi]++;
           if(Pi > maxpk)
               maxpk = Pi;
        }
        int result = split(panck, maxpk, 0, maxpk);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
}
