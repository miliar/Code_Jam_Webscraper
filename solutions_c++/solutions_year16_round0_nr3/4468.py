#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

struct Struct
{
    string num;
    long long deviders[15];

    Struct(){}
    Struct(string num)
    {
        this->num = num;
    }
};

long long t, dels[15], n, l;
vector<Struct> jamcoins[20];

long long convert_to_integer(string s)
{
    long long ans = 0;

    for(int i = 0; i < s.size(); i++)
    {
        ans = ans * 10 + (s[i] - '0');
    }

    return ans;
}
string convert_to_bin(long long num)
{
    string bin;

    while(num > 0)
    {
        if(num % 2 == 0) bin += '0';
        else bin += '1';
        num /= 2;
    }

    reverse(bin.begin(), bin.end());
    return bin;
}
long long convert_from_p_to_dec(string num, int p)
{
    long long current_multi = 1, ans = 0;

    for(int i = num.size() - 1; i >= 0; i--)
    {
        ans += (num[i] - '0') * current_multi;
        current_multi *= p;
    }

    return ans;
}
long long find_del(long long number)
{
    if(number == 2) return -1;
    for(long long i = 2; i <= sqrt(number); i++)
    {
        if(number % i == 0 && number != i) return i;
    }

    return -1;
}
void pre_compute()
{
    for(int i = 16; i <= 16; i++)
    {
        for(long long j = 1; j < (1 << i); j++)
        {
            //cout<<i<<" "<<j<<endl;
            string number = convert_to_bin(j);
            if(number.size() != i || number[number.size() - 1] == '0') continue;

            memset(dels, 0, sizeof(dels));

            bool p1 = true;
            for(int p = 2; p <= 10; p++)
            {
                //cout<<p<<endl;
                long long current_number_dec = convert_from_p_to_dec(number, p);
                dels[p] = find_del(current_number_dec);
                if(dels[p] == -1) p1 = false;
            }

            if(p1 == true)
            {
                jamcoins[i].push_back(Struct(number));
                for(int p = 2; p <= 10; p++)
                {
                    jamcoins[i][jamcoins[i].size() - 1].deviders[p] = dels[p];
                }


                if(jamcoins[i].size() == 55) break;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    pre_compute();

    cin>>t;
    for(int cs = 1; cs <= t; cs++)
    {
        cout<<"Case #"<<cs<<":"<<endl;

        cin>>n>>l;

        //cout<<jamcoins[n].size()<<endl;
        for(int i = 0; i < l; i++)
        {
            cout<<jamcoins[n][i].num;
            for(int j = 2; j <= 10; j++)
            {
                cout<<" "<<jamcoins[n][i].deviders[j];
            }
            cout<<endl;
        }
    }
}
