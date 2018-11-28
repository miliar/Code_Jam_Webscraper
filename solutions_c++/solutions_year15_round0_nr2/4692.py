#include <bits/stdc++.h>
using namespace std;

int mini2;

int dp(vector<int>& arr, int t)
{
    int lnt = arr.size();

    if(arr[lnt-1] == 0 || t >= mini2)
    {
        return t;
    }
    if(arr[lnt-1] == 1)
    {
        return t+1;
    }
    if(arr[lnt-1] == 2)
    {
        return t+2;
    }

    vector<int> temp2 = arr;
    int time_with_decreament =2147483647;
    vector<int> time_with_division(4,2147483647);


    time_with_decreament = arr[lnt-1] + t;

    int m = (int)(temp2[lnt - 1]/2);
    temp2[lnt-1]-=m;
    temp2.push_back(m);
    sort(temp2.begin(), temp2.end());
    time_with_division[0] = dp(temp2, t+1);

    int maxx = arr[lnt-1];

    if(maxx > 3)
    {
        vector<int> temp3 = arr;
        int mm = (int)(temp3[lnt - 1]/3);
        temp3[lnt-1]-=mm;
        temp3.push_back(mm);
        sort(temp3.begin(), temp3.end());
        time_with_division[1] = dp(temp3, t+1);
    }
    if(maxx > 4)
    {
        vector<int> temp4 = arr;
        int mm = (int)(temp4[lnt - 1]/4);
        temp4[lnt-1]-=mm;
        temp4.push_back(mm);
        sort(temp4.begin(), temp4.end());
        time_with_division[2] = dp(temp4, t+1);
    }
    if(maxx > 5)
    {
        vector<int> temp5 = arr;
        int mm = (int)(temp5[lnt - 1]/5);
        temp5[lnt-1]-=mm;
        temp5.push_back(mm);
        sort(temp5.begin(), temp5.end());
        time_with_division[3] = dp(temp5, t+1);
    }

    sort(time_with_division.begin(), time_with_division.end());

    return min(time_with_division[0], time_with_decreament);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tcase;
    scanf("%d", &tcase);

    for(int tc = 1; tc <= tcase; tc++)
    {
        int d;
        scanf("%d", &d);
        vector <int> arra;
        int temporary;
        for(int i = 0; i < d; i++)
        {
            scanf("%d", &temporary);
            arra.push_back(temporary);
        }
        sort(arra.begin(), arra.end());

        int mini = arra[arra.size()-1];
        mini2= mini;
        int time = dp(arra, 0);
        mini = min(mini, time);
        printf("Case #%d: %d\n", tc, mini);
    }
    return 0;
}
