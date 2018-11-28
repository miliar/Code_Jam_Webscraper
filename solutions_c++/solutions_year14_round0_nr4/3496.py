#include<iostream>
#include<vector>
#include<climits>
#include<set>

using namespace std;

int computeScoreWar( set<float> blocksNaomi, set<float> blocksKen )
{
    int scoreWar=0;

    for(float blockNaomi : blocksNaomi)
    {
        auto blockKenP=blocksKen.upper_bound(blockNaomi);
        if(blockKenP==blocksKen.end())
        {
            blockKenP=blocksKen.upper_bound(-1);
            ++scoreWar;
        }
        blocksKen.erase(blockKenP);
    }

    return scoreWar;
}

int computeScoreDeceitfulWar( set<float> blocksNaomi, set<float> blocksKen )
{
    int scoreDeceitfulWar=0;

    for(auto blockKenP=blocksKen.rbegin();blockKenP!=blocksKen.rend();blockKenP++)
    {
        float blockKen= *blockKenP;
        auto blockNaomiP=blocksNaomi.upper_bound( blockKen );
        if(blockNaomiP!=blocksNaomi.end())
        {
            ++scoreDeceitfulWar;
        }
        else if(blockNaomiP==blocksNaomi.end())
        {
            blockNaomiP=blocksNaomi.upper_bound(-1);
        }
        blocksNaomi.erase(blockNaomiP);
    }

    return scoreDeceitfulWar;
}

int main()
{
    int t;
    cin >> t;

    for(int i=1;i<=t;i++)
    {
        int n;
        cin >> n;

        set<float> blocksNaomi;
        set<float> blocksKen;
        for(int j = 0;j<n;j++)
        {
            float temp;
            cin >> temp;
            blocksNaomi.insert(temp);
        }
        for(int j=0;j<n;j++)
        {
            float temp;
            cin>>temp;
            blocksKen.insert(temp);
        }

        cout<<"Case #"<<i<<": "<<computeScoreDeceitfulWar(blocksNaomi, blocksKen )<<" "<<computeScoreWar(blocksNaomi,blocksKen)<<endl;
    }

    return 0;
}
