#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<utility>
#include<iostream>
#include<string>
using namespace std;

string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int cnt[26];

bool isExist(int num)
{
    string &target = nums[num];
    int idx = 0;
    for(int i=0;i<target.size();++i)
    {
        idx = target[i] - 'A';
        if(cnt[idx] < 1)
        {
            for(int j=0;j<i;++j)
            {
                idx = target[j] - 'A';
                cnt[idx]++;                
            }
            return false;
        }
        cnt[idx]--;
    }
    return true;
}

bool findAnswer(int num, string answer)
{    
    bool usedAll = true;
    for(int i=0;i<26;++i)
        if(cnt[i]!=0)
        {
            usedAll=false;
            break;
        }
    if(usedAll==true)
    {
        cout << answer << endl;
        return true;
    }

    if(num > 9)
        return false;

    if(isExist(num))
    {
        bool rtn = findAnswer(num, answer + (char)(num+'0'));
        if(rtn==true)
            return true;
        rtn = findAnswer(num+1, answer + (char)(num+'0'));
        if(rtn==true)
            return true;
        int idx = 0;
        for(int i=0;i<nums[num].size();++i)
        {
            idx = nums[num][i] - 'A';
            cnt[idx]++;
        }
    }
    bool rtn = findAnswer(num+1, answer);
    if(rtn==true)
        return true;
    return false;
}

void findAll(const string& s)
{
    memset(cnt,0,sizeof(cnt));
    int idx = 0;
    for(int i=0;i<s.size();++i)
    {
        idx = s[i] - 'A';
        cnt[idx]++;
    }

    findAnswer(0, "");
}

int main()
{
    int T;
    cin >> T;
    for(int i=1;i<T+1;++i)
    {
        string s;
        cin >> s;
        cout << "Case #" << i << ": ";
        findAll(s);        
    }
    return 0;
}
