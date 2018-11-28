
#include <iostream>
#include <algorithm>
#define ROW_ELEMENTS 4

using namespace std;

int main() {
    int T;
    int n1, n2;
    int m1[16], m2[16];
    int r1[4], r2[4];
    int x;
    
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        
        cin >> n1;
        
        for (int i = 0; i < ROW_ELEMENTS; i++)
            for (int j = 0; j < ROW_ELEMENTS; j++)
            {
                cin >> m1[i*ROW_ELEMENTS+j];
                      }
        
   
        cin >> n2;
        
        for (int i = 0; i < ROW_ELEMENTS; i++)
            for (int j = 0; j < ROW_ELEMENTS; j++)
                cin >> m2[i*ROW_ELEMENTS+j];

        for (int i = 0; i < ROW_ELEMENTS; i++)
        {
            r1[i]=m1[(n1-1)*ROW_ELEMENTS+i];
            r2[i]=m2[(n2-1)*ROW_ELEMENTS+i];
        }
        
        int n_results=0;
        for (int i = 0; i < ROW_ELEMENTS; i++)
            for (int j = 0; j < ROW_ELEMENTS; j++)
            {
                int a=r1[i];
                int b=r2[j];
                if (a==b)
                {
                    n_results++;
                    x=a;
                }
            }
       if (n_results==0)
        {
            cout << "Case #" << t << ": " << "Volunteer cheated!" << endl;
        }
        else if (n_results==1)
        {
            cout << "Case #" << t << ": " << x << endl;
        }
        else if (n_results>1)
        {
            cout << "Case #" << t << ": " << "Bad magician!" << endl;
        }

        
    }
    return 0;
}