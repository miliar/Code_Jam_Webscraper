#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T,ii;
    freopen("D-large.in", "r", stdin);
    freopen("d.txt", "w", stdout);
    cin>>T;
    for(ii = 1; ii <= T; ++ii)
    {
        int n;
        double a;
        vector<double> c, k;
        cin>>n;
        //cout<<n<<endl;
        for(int i = 0; i < n; ++i)
        {
            cin>>a;
            c.push_back(a);
        }
        for(int i = 0; i < n; ++i)
        {
            cin>>a;
            k.push_back(a);
        }
        sort(c.begin(),c.end());
        sort(k.begin(),k.end());
        int score1 = 0, score2 = 0;

        for(int i = 0, j = 0; i < n; ++i)
        {
            if(c[i] > k[j])
            {
                score1 ++;
                ++j;
            }
        }
        //cout<<"dd";
        for(int i = 0, j; i < c.size(); ++i)
        {

            for(j = 0; j < k.size(); ++j)
            {
                if(c[i] < k[j])
                    break;
            }
            vector<double>::iterator it;
            if(j == k.size()) // not find
            {
                it = k.begin();
                score2 ++;
            }
            else
                it = k.begin()+j;
            k.erase(it);
        }
        printf("Case #%d: %d %d\n", ii, score1, score2);
    }
    return 0;
}
