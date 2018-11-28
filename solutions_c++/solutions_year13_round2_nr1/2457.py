#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    
    // insert code here...
    int T;
    ifstream infile;
    infile.open("/Users/Raven/Desktop/data.in");
    if (!infile.is_open())
    {
        cout<<"error read data!"<<endl;
        return 1;
    }
    
    ofstream outfile;
    outfile.open("/Users/Raven/Desktop/data.out");
    if (!outfile.is_open())
    {
        cout<<"error open outfile"<<endl;
        return 1;
    }
    
    
    infile>>T;
    
    long long int f[101][21];
    
    for (int caseIndex = 1; caseIndex <= T; caseIndex++)
    {
        int currentSize;
        int n;
        infile>>currentSize>>n;
        
        vector<int> target;
        for (int i = 0; i < n; i++)
        {
            int temp;
            infile>>temp;
            target.push_back(temp);
        }
        
        sort(target.begin(), target.end());
        
        f[0][0] = currentSize;
        for (int k = 1; k <= 20; k++)
        {
            f[0][k] = 2 * f[0][k-1] - 1;
        }
        
        for (int i = 1; i <= n; i++)
        {
            if (f[i-1][0] > target[i-1])
                f[i][0] = f[i-1][0]+target[i-1];
            else
                f[i][0] = -1;
            
            for (int k = 1; k <= 20; k++)
            {
                bool find = false;
                for (int j = 0; j <= k; j++)
                {
                    int diff = k-j;
                    if (f[i-1][j] > target[i-1])
                    {
                        long long int res = f[i-1][j] + target[i-1];
                        for (int l = 1; l <= diff; l++)
                        {
                            res = res * 2 - 1;
                        }
                        f[i][k] = res;
                        find = true;
                        break;
                    }
                }
                
                if (!find)
                {
                    f[i][k] = f[i-1][k-1];
                }
            }
        
        }
        
        int answer = 0;
        for (int i = 0; i <= 20; i++)
        {
            if (f[n][i] >= currentSize)
            {
                answer = i;
                break;
            }
        }
        outfile<<"Case #"<<caseIndex<<": "<<answer<<endl;
    }
    
    infile.close();
    outfile.close();
    return 0;
    
}

