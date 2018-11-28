#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int itr = 1; itr <= t; itr++)
    {
        int i, n, a;
        int minop = 101, runop = 0;
        vector<int> motes;
        cin >> a >> n;
        for(i= 0; i < n; i++){
            int temp;
            cin >> temp;
            motes.push_back(temp);
        }
        sort(motes.begin(), motes.end());

        // the idea is to find no of operations to add each element
        // into the mote
        int motesize = a;
        for(i=0; i< n; i++)
            if(motes[i] < motesize)
                motesize += motes[i];
            else break;
        minop = min(minop, n - i);

        if(a == 1){
            printf("Case #%d: %d\n", itr, minop);
            continue;
        }

        for(; i< n; i++)
        {
            bool f = false;
            while(motesize <= motes[i])
            {
                motesize += (motesize - 1);
                runop ++;
                // cout << motesize << ';' << motes[i] << endl;
            }
            while(motes[i] < motesize && i < n){
                motesize += motes[i];
                i++;
                f = true;
                // cout << motesize << ' ' << motes[i] << endl;
            }

            minop = min(minop, runop + n - i);
            if(f) i--;
        }
        printf("Case #%d: %d\n", itr, minop);
    }
    return 0;
}

