#include<algorithm>
#include<iostream>
#include<vector>
#include<string>

using namespace std;

int good(vector<int> stacks, int cut)
{
    int large = stacks[0];
    int newLarge = large - cut;
    int count = 0;
    for(int i = 1; i < stacks.size(); i++)
    {
        if(stacks[i] > newLarge)
        {
            count++;
        }
    }
    return count < cut;
}

int cut(vector<int> stacks)
{
    sort(stacks.rbegin(), stacks.rend());
    int large = stacks[0];

    if(stacks[0] == 1)
    {
        return 1;
    }
    
    int small = large;
    for(int i = 2; i <= large/2; i++)
    {
        if(good(stacks, i))
        {
            vector<int> temp = stacks;
            int remain = large - i;
            temp[0] = i;
            temp.push_back(remain);
            small = min(small, 1+cut(temp));
        }
    }

    return small;
}

int main(void)
{
    int test;
    cin >> test;
    for(int z = 1; z <= test; z++)
    {
        int len;
        vector<int> stacks;
        cin >> len;
        for(int i = 0; i < len; i++)
        {
            int num;
            cin >> num;
            stacks.push_back(num);
        }


        int ans = cut(stacks);

        cout << "Case #" << z << ": " << ans << endl;

    }

    return 0;
}
