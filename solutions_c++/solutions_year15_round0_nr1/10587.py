#include <bits/stdtr1c++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("Mekkawy.in","r",stdin);
    freopen("Mekkawy.out","w",stdout);
    int T;
    cin>>T;
    int cnt=0;
    while(T--)
    {
        cnt++;
        int N;
        cin>>N;
        string x;cin>>x;
        for(int i=0;i<=1000;i++)
        {
            int b=i;
            int clapping=i;
            int j;
            for(j=0;j<=N;j++)
            {
                if(clapping>=j)
                    clapping+=x[j]-'0';
                else
                    break;
            }
            if(j>N)
            {
                cout<<"Case #"<<cnt<<": "<<i<<"\n";
                break;
            }
        }
    }


    return 0;
}
