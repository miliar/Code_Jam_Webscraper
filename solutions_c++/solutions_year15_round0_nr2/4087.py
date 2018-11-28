#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int find_max (vector<int> v)
{
    int ret = 0;
    for (int i=0; i<v.size(); i++)
    {
        if (v[i] > ret)
            ret = v[i];
    }
    return ret;
}
int reduce(vector<int>&v, int dst, int max)
{
    vector<int> v2;
    int flag = 0;
    for (int i=0; i<v.size(); i++)
    {
        if (flag == 0 && v[i] == max)
        {
            flag = 1;
            continue;
        }
        v2.push_back(v[i]);
    }
   
    int ans = 0;
    int tmp = max;
    while (1)
    {
        ans++;
        tmp = tmp - dst;
        if (tmp > dst)
            v2.push_back(dst);
        else if (tmp <= dst)
        {
            v2.push_back(dst); 
            v2.push_back(tmp); 
            break;
        }
    }
/*
    for (int i=0; i<v2.size(); i++)
    {
        cout << v2[i] << ' ';  
    }
    cout << "===> " << ans << endl;
*/

    v.clear();
    v = v2;
    return ans;
}
int split_to_dst(vector<int>v, int dst)
{
    int end = 0;
    int ans = 0;
//    cout << "\t";
    while (end == 0)
    {
        int max = find_max (v);
        ans += reduce(v, dst, max);
//        cout << ans << "\t";
        for (int i=0; i<v.size(); i++)
        {
            if (v[i] > dst)
                break;
            else if (i==v.size()-1)
                end = 1;
            
        }
    }
//    cout << endl;
    return ans;
}

int main()
{
    int round;
    cin >> round;
    for (int idx=1; idx<=round; idx++)
    {
        int plate;
        vector<int> cake;
        cin >> plate;
        for (int i=0; i<plate; i++)
        {
            int tmp;
            cin >> tmp;
            cake.push_back(tmp);
        }

        int max = find_max(cake);
        int ans = max;         
        for (int dst=1; dst<=max; dst++)
        {
//            cout << '#' << dst <<endl;;
            int tmp = 0;
            tmp += split_to_dst(cake, dst);
            tmp += dst;
            if (tmp < ans)
            {
                ans = tmp;
            }
        }
        cout << "Case #" << idx << ": " << ans << endl;
    }
}
