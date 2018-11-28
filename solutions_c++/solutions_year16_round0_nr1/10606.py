#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> digit;

bool isAllPresent()
{
    for(int i =0;i<10;i++)
    {
        if(digit[i]==0)
            return false;
    }
    return true;
}

void addCount(ll num)
{
    while(num)
    {
        digit[num%10]+=1;
        num/=10;
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;
    cin>>cases;
    int t = 0;
    while(cases--)
    {
        ++t;
        ll num;
        cin>>num;
        digit.assign(10,0);
        ll i ;
        for(i = 1;i<100;i++)
        {
            ll lastNum = i*num;
            addCount(lastNum);
            if(isAllPresent())
            {
                cout<<"Case #"<<t<<": "<<lastNum<<endl;
                break;
            }
        }
        if(i==100)
        {
            cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
        }
    }


    return 0;
}
