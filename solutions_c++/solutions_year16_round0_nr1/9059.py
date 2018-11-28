//rubal9 pes college
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll t,x =1;
    cin>>t;
    while(t--)
    {
        ll a;
        cin>>a;
        ll arr[10],i;
            ll count =0,temp;
            memset(arr,0,sizeof arr);
            for(i =1; i <= 100; i++)
            {
                ll c = a*i;
                while(c > 0)
                {
                    temp = c%10;
                    if(arr[temp] == 0)
                    {
                        arr[temp] = 1;
                        count++;
                    }
                    c = c/10;
                }
                if(count == 10)
                {
                    cout<<"Case #" << x <<  ": " <<  a*i<<endl;
                    x++;
                    break;
                }
            }
            if(count !=10)
            {
                cout<<"Case #" << x <<  ": " <<"INSOMNIA"<<endl;
                x++;
            }
    }
    return 0;
}




