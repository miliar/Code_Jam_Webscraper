#include <stdio.h>
#include <vector>
#include <algorithm>

int solve4_sub(std::vector<int> P, int current_minutes, int max_minutes)
{
    while(true)
    {
        if(P.size() == 0)
            return std::min(max_minutes, current_minutes);
        max_minutes = std::min(max_minutes, current_minutes+P[P.size()-1]);
        if(current_minutes >= max_minutes-1)
            return max_minutes;
        int max = P[P.size()-1];
        std::vector<int> tmp;
        if(max/2 > 0)
            tmp.push_back(max/2);
        tmp.push_back(max-max/2);
        std::vector<int> P2(P.size()-1+tmp.size());
        std::merge (P.begin(),P.begin()+(P.size()-1),tmp.begin(),tmp.end(),P2.begin());
        P = P2;
        current_minutes++;
    }
}

int solve4(std::vector<int> P)
{
    int count = 0;
    std::sort(P.begin(), P.end());
    count = solve4_sub(P, 0, P[P.size()-1]);
    return count;
}

int solve3_rec(const std::vector<int>& P, int current_minutes, int max_minutes)
{
    if(P.size() == 0)
        return current_minutes;
    if(current_minutes >= max_minutes-1)
        return max_minutes;
    std::vector<int> P2;
    for(int i = 0; i < P.size(); i++)
        if(P[i] > 1)
            P2.push_back(P[i]-1);
    max_minutes = std::min(max_minutes, solve3_rec(P2, current_minutes+1, max_minutes));
    int max = P[P.size()-1];
    for(int i = 2; i <= max/2; i++)
    {
        P2 = P;
        P2[P2.size()-1] = max-i;
        P2.push_back(i);
        std::sort(P2.begin(), P2.end());
        max_minutes = std::min(max_minutes, solve3_rec(P2, current_minutes+1, max_minutes));
    }
    return max_minutes;
}

int solve3(std::vector<int> P)
{
    int count = 0;
    std::sort(P.begin(), P.end());
    count = solve3_rec(P, 0, P[P.size()-1]);
    return count;
}

int main()
{
    int num;
    scanf("%d\n", &num);
    for(int i = 0; i < num; i++)
    {
        int d;
        scanf("%d\n", &d);
        std::vector<int> P(d);
        for(int j = 0; j < d; j++)
            scanf("%d", &P[j]);
        printf("Case #%d: %d\n", i+1, solve3(P));//, solve4(P));
    }
    return 0;
}
