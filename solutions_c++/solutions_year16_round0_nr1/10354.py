#include <bits/stdc++.h>
#define vi vector<int>
#define vl vector<long>

typedef unsigned long long llu;
typedef long long ll;

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int tt;
    cin>>tt;
    for (int qq = 1; qq <=tt ; ++qq)
    {
        cout<<"Case #"<<qq<<": ";
        int n;
        cin>>n;
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int num,temp,mul=1;
        set<int> sheep;
        while(1)
        {
            num = mul*n;
            while(num)
            {
                temp = num%10;
                sheep.insert(temp);
                num/=10;
            }
            if(sheep.size() == 10)
                break;
            mul++;
        }
        num = mul*n;
        cout<<num<<endl;
    }
}