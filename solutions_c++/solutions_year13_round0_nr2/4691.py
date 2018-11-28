#include <stdio.h>
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int array[100][100];
int compare[100][100];

int main(int argc, char *args[])
{
    int nr;
    cin >> nr;

    int n;
    int m;

    string adi;

    for (int caseNr=1;caseNr<=nr;++caseNr)
    {
        cin >> n;
        cin >> m;
        
        for (int i=0;i<n;++i)
        {
            for (int j=0;j<m;++j)
            {
                cin >> array[i][j];
                compare[i][j]=200;
            }
        }
        
        for (int i=0;i<n;++i)
        {
            int max=0;
            for (int j=0;j<m;++j) 
            {
                if (array[i][j] > max)
                {
                    max = array[i][j];
                }
            }

            //cout << "\nline: " << i << " max: " << max;
            for (int j=0;j<m;++j)
            {
                if (compare[i][j]>max)
                {
                    compare[i][j]=max;
                }
            }
        }

        for (int j=0;j<m;++j)
        {
            int max=0;
            for (int i=0;i<n;++i) 
            {
                if (array[i][j] > max)
                {
                    max = array[i][j];
                }
            }
            //cout << "\ncol: " << j << " max: " << max;

            for (int i=0;i<n;++i)
            {
                if (compare[i][j]>max)
                {
                    compare[i][j]=max;
                }
            }
        }

        bool equal = true;
        for (int i=0;(i<n)&&equal;++i)
        {
            for (int j=0;(j<m)&&equal;++j)
            {
                if (compare[i][j]!=array[i][j])
                {
                    equal = false;
                }
            }
        }
        
        if (!equal)
        {
            cout << "Case #" << caseNr << ": NO\n";
        }
        else
        {
            cout << "Case #" << caseNr << ": YES\n";
        }
    }
}

        
