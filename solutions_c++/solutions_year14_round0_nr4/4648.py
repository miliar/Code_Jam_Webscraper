#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

int war(vector<double> &naomi, vector<double> &ken)
{
    int score = 0;
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());
    vector<bool> used(ken.size(),false);

    for(int i=0;i<naomi.size();i++)
    {
        int j;
        for(j=0;j<ken.size();j++)
        {
            if(ken[j]>naomi[i] && used[j]==false)
            {
                used[j] = true;
                break;
            }
        }
        if(j>=ken.size())
        {
            score++;
        }
    }
    return score;
}

int helper(int N, vector<double> &v1, int p, vector<double> &v2, int q)
{
    int score = 0;
    for(int i=0;i<N;i++)
    {
        if(v1[p+i]>v2[q+i])
            score++;
    }
    return score;
}

int deceitWar(vector<double> &naomi, vector<double> &ken)
{
    int score = 0;
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());
    vector<bool> used(ken.size(),false);

    int N = naomi.size();
    score = helper(N,naomi,0,ken,0);
    N--;
    while(N>0)
    {
        int tmp_score = helper(N,naomi,naomi.size()-N, ken,0);
        if(tmp_score>score)
            score = tmp_score;
        N--;
    }
    return score;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        int N;
        cin>>N;
        vector<double> naomi;
        vector<double> ken;
        for(int i=0;i<N;i++)
        {
            double tmp;
            cin>>tmp;
            naomi.push_back(tmp);
        }
        for(int i=0;i<N;i++)
        {
            double tmp;
            cin>>tmp;
            ken.push_back(tmp);
        }

        cout<<deceitWar(naomi,ken)<<" "<<war(naomi,ken)<<endl;
    }
    return 0;
}



