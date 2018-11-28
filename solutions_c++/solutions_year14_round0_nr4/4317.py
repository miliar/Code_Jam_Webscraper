#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T,N,i,j,ptsa,ptsb;
    double temp;
    ifstream fin ("/Users/ezfxwhz/Downloads/D-large.in");
    ofstream fout ("/Users/ezfxwhz/Desktop/war.out");
    fin >> T;
    for (i=0;i<T;i++)
    {
        ptsa=0;
        ptsb=0;
        vector<double> naomi,ken;
        vector<double>::iterator nStart,nEnd,kStart,kEnd;
        
        fin >> N;
        for (j=0;j<N;j++)
        {
            fin >> temp;
            naomi.push_back(temp);
        }
        for (j=0;j<N;j++)
        {
            fin >> temp;
            ken.push_back(temp);
        }
        
        nStart=naomi.begin();
        nEnd=naomi.end();
        kStart=ken.begin();
        kEnd=ken.end();
        
        sort(nStart, nEnd);
        sort(kStart, kEnd);
        
        for (j=0;j<N;j++,nStart++)
        {
            if (*nStart>*kStart)
            {
                ptsb++;
                kStart++;
            }
        }
        
        nStart=naomi.begin();
        kStart=ken.begin();
        
        for (;nStart!=nEnd;nStart++)
        {
            for (kStart=ken.begin(),kEnd=ken.end();kStart!=kEnd&&*nStart>*kStart;kStart++);
            if (kStart==kEnd)
            {
                ptsa++;
            }
            else
            {
                ken.erase(kStart);
            }
        }
        
        fout << "Case #" << i+1 << ": " << ptsb << " " << ptsa;
        if (i<T-1)
        {
            fout << "\n";
        }
    }
    return 0;
}

