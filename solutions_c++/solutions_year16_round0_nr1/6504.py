#include <bits/stdc++.h>

using namespace std;

set<int> cntVc;

long long get(long long num)
{
    long long curCnt = 0;
    while(cntVc.size() < 10)
    {
        curCnt++;
        long long curNum = num * curCnt;
        while(curNum)
        {
            cntVc.insert(curNum%10);
            curNum /= 10;
        }
    }
    return num * curCnt;
}

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
        cntVc.clear();
        long long num;
        cin >> num;
        cout << "Case #"<<cnt+1<<": ";
        if(num == 0)
            cout << "INSOMNIA" << endl;
        else
            cout << get(num) << endl;
    }
}
