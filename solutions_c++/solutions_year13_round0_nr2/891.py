#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

typedef struct
{
    int height, row, col;
} lawnmap;

bool less_than(const lawnmap &a, const lawnmap &b) 
{
    return a.height < b.height;
}

int main()
{
    int t, count = 1;
    ifstream fin("B-large.in");
    ofstream fout("B.out");
    
    fin >> t;
    
    while (t--)
    {
        int n, m, i, j;
        fin >> n >> m;
        vector <lawnmap> mylawn(n * m);
        
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < m; j++)
            {
                int height, cur = i * m + j;
                fin >> height;
                
                mylawn[cur].height = height;
                mylawn[cur].row = i;
                mylawn[cur].col = j;
            }
        }
        
        vector <lawnmap> sortedlawn(mylawn);
        sort(sortedlawn.begin(), sortedlawn.end(), less_than);
        fout << "Case #" << count++ << ": "; 
        
        int curloc = 0;
        vector <int> flag(n * m, 0);
        
        while (curloc < n * m)
        {
            int r = sortedlawn[curloc].row, c = sortedlawn[curloc].col, height = sortedlawn[curloc].height;
            
            if (flag[r * m + c] == 0)
            {
                //cout << "111 " << r << " " << c << endl;
                //system("pause");
            
                for (i = 0; i < n; i++)
                    if (flag[i * m + c] == 0 && mylawn[i * m + c].height > height)
                        break;
                        
                if (i == n)
                {
                    for (i = 0; i < n; i++)
                        flag[i * m + c] = 1;
                        
                    //cout << "222 " << r << " " << c << endl;
                    //system("pause");
                }
                else
                {
                    for (j = 0; j < m; j++)
                        if (flag[r * m + j] == 0 && mylawn[r * m + j].height > height)
                            break;
                            
                    if (j == m)
                    {
                        for (j = 0; j < m; j++)
                            flag[r * m + j] = 1;
                            
                        //cout << "333 " << r << " " << c << endl;
                        //system("pause");
                    }
                    else
                    {
                        //cout << "444 " << r << " " << c << endl;
                        //system("pause");
                        
                        break;
                    }
                }
            }
            
            curloc++;
        }
        
        if (curloc == n * m) fout << "YES" << endl;
        else fout << "NO" << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
