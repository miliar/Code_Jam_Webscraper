#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x,y,i,j;
    int a[20],b,k;
    int temp = 1;
    cin>>t;
    while(t--)
    {
        memset(a,0,sizeof(a));
        int ans = 0;
        k = 0;
        cin>>x;
        for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
        {
            cin>>b;
            if(i==x-1)
            a[b] = 1;
        }
        cin>>y;
        for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
        {
            cin>>b;
            if(i==y-1)
            {
                if(a[b]==1)
                {
                    k = b;
                    ans++;
                }
            }
        }
        cout<<"Case #"<<temp++<<": ";
        if(ans==1)cout<<k<<endl;
        else if(ans==0)cout<<"Volunteer cheated!"<<endl;
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}
