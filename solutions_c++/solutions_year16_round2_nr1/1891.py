#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll hh,t,i,j;
    string str;
    freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
    cin>>t;
    ll arr[30],num[11];
    for(hh=1;hh<=t;hh++)
    {
        printf("Case #%d: ",hh);
        cin>>str;
        memset(arr,0,sizeof(ll)*27);
        for(i=0;i<str.length();i++)
        {
            arr[str[i]-'A']++;
        }

        num[6]=arr['X'-'A'];
        num[8]=arr['G'-'A'];
        num[2]=arr['W'-'A'];
        num[0]=arr['Z'-'A'];
        num[4]=arr['U'-'A'];
        num[5]=arr['F'-'A']-num[4];
        num[7]=arr['V'-'A']-num[5];
        num[3]=arr['R'-'A']-num[0]-num[4];
        num[1]=arr['O'-'A']-num[0]-num[4]-num[2];
        num[9]=arr['I'-'A']-num[5]-num[6]-num[8];

        for(i=0;i<10;i++)
        {
            for(j=1;j<=num[i];j++)
                printf("%lld",i);
        }

        cout<<endl;
    }
    return 0;
}
