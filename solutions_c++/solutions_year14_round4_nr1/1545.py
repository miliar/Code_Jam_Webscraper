#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t)
    {
        int numberOfFiles, sizeOfDisks;
        
        cin >> numberOfFiles >> sizeOfDisks;
        
        int mimimum = 0;
        
        vector<int> files(numberOfFiles);
        
        for (int i = 0; i < numberOfFiles; ++i)
        {
            cin >> files[i];
        }
        
        vector<bool> picked(numberOfFiles, false);
        
        for (int f1 = 0; f1 < numberOfFiles; ++f1)
        {
            if (!picked[f1])
            {
                ++mimimum;
                
                picked[f1] = true;
                // Try to find match
                
                int maxSize = 0;
                int pos = -1;
                for (int f2 = 0; f2 < numberOfFiles; ++f2)
                {
                    if (!picked[f2] && files[f1] + files[f2] <= sizeOfDisks && files[f2] > maxSize)
                    {
                        pos = f2;
                        maxSize = files[f2];
                    }
                }
                
                if (pos != -1)
                {
                    picked[pos] = true;
                }
            }
        
        }
        
        
        cout << "Case #" << t << ": " << mimimum << '\n';
    }
}