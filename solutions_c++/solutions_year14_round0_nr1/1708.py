#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int a, b;
vector<int> num,ans;

int main()
{
    int T, ii;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    cin>>T;
    for(ii = 1; ii <= T; ++ii)
    {
        int r1, r2;
        num.clear();
        ans.clear();
        cin>>r1;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            {
                cin>>a;
                if(i+1==r1)
                    num.push_back(a);
            }
        cin>>r2;
        //cout<<num[0]<<num[1]<<num[2]<<num[3]<<endl;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            {
                cin>>a;
                if(i+1 == r2)
                {
                    vector<int>::iterator it = find(num.begin(), num.end(), a);
                    if(it !=num.end())
                    {
                        //num.erase(it);
                        ans.push_back(a);
                    }
                }
            }
        if(ans.size() > 1)
        {
            printf("Case #%d: Bad magician!\n", ii);
        }
        else if(ans.size() == 1)
        {
            printf("Case #%d: %d\n", ii, ans[0]);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", ii);
        }
    }
    return 0;
}
