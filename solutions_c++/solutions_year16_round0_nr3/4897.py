#include <bits/stdc++.h>

using namespace std;

long long convert(string j, long long b)
{
    long long ans = 0,i,k=1;
    for(i=j.size()-1;i>=0;i--)
    {
        ans += (j[i]=='1')*k;
        k*=b;
    }
    return ans;
}

long long ok(long long x)
{
    if(x%2==0)
    {
        if(x==2) return -1;
        return 2;
    }
    for(long long i=3;i*i<=x;i+=2)
    {
        if(x%i==0) return i;
    } return -1;
}

int main()
{

    long long jc=0;
    long long n = 32768;
    cout << "Case #1:\n";
    while(jc<50)
    {
        n++;
        string s = bitset<16>(n).to_string();
        if(s[0]!='1' || s[s.size()-1]!='1') continue;
        vector<int> divs;
        for(long long i=2;i<=10;++i)
        {
            long long x = convert(s,i);

            if(ok(x)==-1) break;
            divs.push_back(ok(x));


        }
        if(divs.size()==9)
        {
            jc++;
            cout << s;
            for(long long i=0;i<divs.size();++i) cout << " " << divs[i];
            cout << "\n";
        }
    }
    return 0;
}
