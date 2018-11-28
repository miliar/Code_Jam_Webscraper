#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N;
int ans;
int oA;
void test(int A, int ci, int times, const vector<int>& motes)
{
    bool allclear = true;
    for(int i=ci; i<motes.size(); ++i)
    {
        if(A>motes[i])
        {
            A+=motes[i];
        }
        else
        {
            allclear = false;
            test(A, i+1, times+1, motes);
            if(times<N)
            {
                vector<int> newMotes=motes;
                newMotes.push_back(A-1);
                sort(newMotes.begin(), newMotes.end());
                test(oA, 0, times+1, newMotes);
                break;
            }
        }
    }
    if(allclear && (times<ans || ans ==-1))
    {
        ans = times;
    }
}
void main()
{
    int T;
    cin >> T;
    for(int TC=0; TC<T; ++TC)
    {
        ans = -1;
        oA = 0;
        cin >> oA;
        N = 0;
        cin >> N;
        vector<int> motes;
        for(int NC=0; NC<N; ++NC)
        {
            int tmp;
            cin >> tmp;
            motes.push_back(tmp);
        }
        sort(motes.begin(), motes.end());
        test(oA, 0, 0, motes);
        printf("Case #%d: %d\n", (TC+1), ans);
    }    
}