#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
    int T;
    cin >> T;
    for (int i=1;i<=T;i++)
    {
        int smax;
        int cur=0,need=0;
        string audience;
        cin >> smax;
        cin >> audience;
        for(int j=0;j<smax;j++)
        {
            cur=cur+(audience[j]-48);
            if (cur<j+1)
            {
                need=need+j+1-cur;
                cur=j+1;
            }
        }
        cout << "Case #" << i << ": " << need <<endl;
    }
    return 0;
}
