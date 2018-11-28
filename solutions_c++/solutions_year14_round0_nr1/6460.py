#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>

using namespace std;

int main()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T, ind1, c, count=0, ans;
    int A[17];

    cin>>T;

    for(int t=0; t<T; t++)
    {
        count = 0;
        memset(A,0,17*sizeof(int));
        for(int k=0; k<2; k++)
        {
            cin >> ind1;
            for(int j=1; j<5; j++)
            {
                for(int i=1; i<5; i++)
                {
                    cin >> c;
                    if(j==ind1)
                        A[c]++;
                }
            }
        }
        for(int k=0; k<17; k++)
        {
            if(A[k]==2)
            {
                count++;
                ans=k;
            }
        }
        cout << "Case #" << t+1 << ": ";
        if(count==0) cout << "Volunteer cheated!";
        else if(count==1) cout << ans;
        else cout << "Bad magician!";


        cout << "\n";
    }

    return 0;
}

