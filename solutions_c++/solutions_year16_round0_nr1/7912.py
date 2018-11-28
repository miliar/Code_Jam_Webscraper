#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bitset<10> nums;
int t;
ll n, tmp, pos, tn;

bool isFound()
{
    /*for(int i=0;i<10;i++)
    {
        cout<<nums[i]<<" ";
    }
    cout<<endl;*/
    for(int i=0;i<10;i++)
        if(!nums[i])
            return false;
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin>>t;
    for(int ca=1; ca<=t; ca++)
    {
        nums.reset();
        pos = 1;
        cin>>n;   
        tn=n;   
        if(n!=0)
        {
            do
            {
                n = pos*tn;
                tmp=n;
                //cout<<tmp<<endl;
                while(tmp)
                {
                    nums[tmp%10]=1;
                    tmp/=10;
                }   
                pos++;
            }while(!isFound());
            cout<<"Case #"<<ca<<": "<<n<<endl;
        }
        else
            cout<<"Case #"<<ca<<": INSOMNIA"<<endl;
    }
    return 0;
}
