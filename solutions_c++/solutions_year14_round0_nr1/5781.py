#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small.out");
    int t;
    fin >> t;
    for(int k = 0;k < t;k++)
    {
            int b1[4][4],b2[4][4];
            int a1,a2;
            vector<int> c;
            vector<int> d;
            fin >> a1;
            for(int i = 0;i < 4;i++)
                    for(int j = 0;j < 4;j++) fin >> b1[i][j];
            fin >> a2;
            a1--;
            a2--;
            for(int i = 0;i < 4;i++)
                    for(int j = 0;j < 4;j++) fin >> b2[i][j];
            for(int i = 0;i < 4;i++) c.push_back(b1[a1][i]);
            for(int i = 0;i < 4;i++) d.push_back(b2[a2][i]);
            int ans = 0;
            vector<int> an;
            for(int i = 0;i < 4;i++)
            {
                    for(int j = 0;j < 4;j++)
                    {
                            if(c.at(i) == d.at(j)){ ans++;an.push_back(c[i]);}
                    }
            }
            if(ans == 0) fout << "Case #" << k+1 << ": Volunteer cheated!" << endl;
            else if(ans == 1) fout << "Case #" << k+1 << ": " << an[0] << endl;
            else fout << "Case #" << k+1 << ": Bad magician!" << endl;
    }
    return 0;
}
