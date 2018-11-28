#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    int t;
    fin >> t;
    ofstream fout("output.txt");
    for(int s=1; s<=t; ++s)
    {
        int a1,a2;
        int g1[4][4],g2[4][4];
        //vector <vector <int> > g1,g2(4);
        fin >> a1;
        a1-=1;
        for(int i=0; i<4; ++i)
            for(int j=0; j<4; ++j)
            {
                fin >> g1[i][j];
            }
        fin >> a2;
        a2-=1;
        for(int i=0; i<4; ++i)
            for(int j=0; j<4; ++j)
            {
                fin >> g2[i][j];
            }

        vector <int> sol;
        for(int j=0; j<4; ++j)
        {
            for(int h=0; h<4; ++h)
            if(g1[a1][j]==g2[a2][h])
            {
                sol.push_back(g1[a1][j]);
                break;
            }
        }
        /*printf("soluzioni: ");
        for(int i=0; i<sol.size(); ++i)
            printf("%d ",sol[i]);
        printf("\n");*/

        fout << "Case #" << s << ": ";
        if(sol.size()==1)
            fout << sol[0] << endl;
        else if(sol.size()==0)
            fout << "Volunteer cheated!" << endl;
        else if(sol.size()>1)
            fout << "Bad magician!" << endl;


    }
}
