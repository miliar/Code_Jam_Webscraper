#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<utility>
using namespace std;

inline int cakes2bits(string& cakes)
{
    int bits = 0;
    int bit = 1;
    for(int i=0;i<cakes.length();++i)
    {
        if(cakes[i]=='+')
            bits |= bit;
        bit <<=1;
    }
    return bits;
}

void showBits(int bits, int sz)
{
    int pow = 1;
    for(int i=0;i<sz;++i)
    {
        if(pow & bits)
            cout << "1";
        else
            cout << "0";
        pow <<= 1;
    }
    cout << endl;
}

inline int convert(int cakeBits, int index)
{
    int power = (1<<(index+1));
    int intern = cakeBits%power;
    for(int i=0;i<index+1;++i)
    {
        power = (1<<i);
        //if(cakeBits & power)
        cakeBits ^=power;        
    }
    int revertPower = 0;
    int answer = cakeBits;
    
    for(int i=0;i<index + 1;++i)
    {
        power = (1<<i);
        revertPower = (1<<(index - i));
        if(cakeBits & power)
            answer |= revertPower;
        else
            answer &= (~revertPower);
    }
    
    return answer;
}

int bfs(int cakesBits, int sz, int target)
{
    if(cakesBits == target)
        return 0;
    int ans = 0;
    vector<int> stk;
    set<int> uniq;
    stk.push_back(cakesBits);
    uniq.insert(cakesBits);
    int st = 0, ed = 1;
    int cur = 0;
    int newStat = 0;
    while(st < ed)
    {
        for(int i=st;i<ed;++i)
        {
            cur = stk[i];
            for(int j=1;j<=sz;j=(j<<1))
            {
                newStat = convert(cur, j-1);
                // cout << "newStat: ";
                // showBits(newStat, sz);
                if(uniq.find(newStat)!=uniq.end()) continue;                               
                if(newStat==target)
                {                    
                    ++ans;
                    break;
                }                
                uniq.insert(newStat);
                stk.push_back(newStat);
            }
            if(newStat==target)
                break;
        }
        if(newStat==target)
            break;
        st = ed;
        ed = stk.size();
        ++ans;
    }
    
    return ans;
}

int main()
{
    int T;
    string cakes;
    cin >> T;
    //cin >> cakes;
    for(int i=1;i<T+1;++i)
    {
        cin >> cakes;        
        //cout << cakes << endl;
        int cBits = cakes2bits(cakes);
        int target = (1<<(cakes.length())) - 1;
        //showBits(cBits, cakes.length());
        //showBits(convert(cBits, cakes.length()-1), cakes.length());
        int ans = bfs(cBits, cakes.length(), target);
        cout << "Case #" << i << ": " <<  ans << endl;
    }
    return 0;
}
