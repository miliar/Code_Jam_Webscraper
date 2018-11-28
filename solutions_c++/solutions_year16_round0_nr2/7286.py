#include<bits/stdc++.h>
using namespace std;
#define ll long long
char s[105];
ll l;

void pancakeflip(ll index) //flips the group from 0...index with all their faces reversed
{
    ll i,newpos;
    char temp[105];
    for(i=0;i<=index;i++)
    {
        newpos=index-i;

        if(s[i]=='+')
            temp[newpos]='-';
        else
            temp[newpos]='+';

    }
    for(i=0;i<=index;i++)
    s[i]=temp[i];
}

int main()
{

freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
    ll t,i,j,k,ans;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>s;
        l=strlen(s);
        ans=0;
        i=l-1;

        while(1)
        {
            while(i>=0&&s[i]=='+')
                i--;

            if(i==-1)
                break;
            //Now s[i]='-' and we need to change it into '+';
            if(s[0]=='+')
            {
                j=1;
                while(s[j]=='+')
                    j++;
                j--;
                pancakeflip(j);
                ans++;
            }
            pancakeflip(i);
            ans++;
            --i;
        }
        cout<<"Case #"<<k<<": "<<ans<<"\n";
    }
return 0;
}
