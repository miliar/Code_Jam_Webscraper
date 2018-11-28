#include <bits/stdc++.h>

typedef long long LL;
typedef unsigned long long ULL;
typedef long double ld;
typedef __float128 bfl;

const int MOD = 1000000007;

#define f first
#define s second
#define pll pair<LL, LL> 
#define pii pair<int, int> 
#define mp make_pair
#define pb push_back
#define SC static_cast

using namespace std;
const int len = 32;
string 
coin = "10000000000000000000000000000001";
int i;

string next_coin()
{
    string res = coin;
    for(int pos = len-2; pos>0; pos--)
        if (coin[pos] == '1')
        {
            for(int pos1 = pos-1; pos1>0; pos1-=2)
                if (pos1>2 && coin[pos1] == '1')
                {
                    coin[pos1] = '0';
                    coin[pos1-2] = '1';
                    return res;
                }
                else if (coin[pos1] == '1') coin[pos1] = '0';

            coin[pos]='0';
            coin[pos-1] = '1';
            coin[pos-2] = '1';
            return res;
        }
    return '\0';
}

string next_coin1()
{
    string res = coin;
    for(int pos = len-4; pos>0; pos--)
        if (coin[pos] == '1')
        {
            for(int pos1 = pos-1; pos1>0; pos1-=2)
                if (pos1>2 && coin[pos1] == '1')
                {
                    coin[pos1] = '0';
                    coin[pos1-2] = '1';
                    return res;
                }
                else if (coin[pos1] == '1') coin[pos1] = '0';

            coin[pos]='0';
            coin[pos-1] = '1';
            coin[pos-2] = '1';
            return res;
        }
    return '\0';
}

string next_coin2()
{
    string res = coin;
    for(int pos = len-6; pos>0; pos--)
        if (coin[pos] == '1')
        {
            for(int pos1 = pos-1; pos1>0; pos1-=2)
                if (pos1>2 && coin[pos1] == '1')
                {
                    coin[pos1] = '0';
                    coin[pos1-2] = '1';
                    return res;
                }
                else if (coin[pos1] == '1') coin[pos1] = '0';

            coin[pos]='0';
            coin[pos-1] = '1';
            coin[pos-2] = '1';
            return res;
        }
    return '\0';
}

int main()
{
    cout<<"Case #1:"<<endl;
    
    cout<<coin<<" 3 4 5 6 7 8 9 10 11"<<endl;        

coin = "10000000000000000000000000000111";
    for (i = 1; i<220; i++)
        cout<<next_coin()<<" 3 4 5 6 7 8 9 10 11"<<endl;        
coin = "10000000000000000000000000011111";

    for (i = 220; i<415; i++)
        cout<<next_coin1()<<" 3 4 5 6 7 8 9 10 11"<<endl;        
coin = "10000000000000000000000001111111";
    for (i = 415; i<500; i++)
        cout<<next_coin2()<<" 3 4 5 6 7 8 9 10 11"<<endl;        
    return 0;
}
