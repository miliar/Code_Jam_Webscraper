#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    int T;
    int i,j,k,f,s;
    int a[4];
    int b[4];
    int t[4];
    
    cin >> T;
    for (i=0;i<T;i++)
    {
        cin >> f;
        
        for (j=0;j<4;j++)
        for (k=0;k<4;k++)
        {
            if (j+1==f)
               cin >> a[k];
            else
               cin >> t[k];
        }

        cin >> s;

        for (j=0;j<4;j++)
        for (k=0;k<4;k++)
        {
            if (j+1==s)
               cin >> b[k];
            else
               cin >> t[k];
        }

        // find intersection of a and b
        
        int c = 0;
        int answer = 0;
        for (j=0;j<4;j++)
        for (k=0;k<4;k++)
        {
            if (a[j]==b[k])
            {
               c++;
               answer = a[j];
            }
        }
        
        if (c==0) 
           cout << "Case #" << (i+1) << ": Volunteer cheated!\n";
        else if (c>1)
           cout << "Case #" << (i+1) << ": Bad magician!\n";
        else
           cout << "Case #" << (i+1) << ": " << answer << "\n";
    }
}
