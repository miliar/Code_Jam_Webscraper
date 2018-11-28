#include <bits/stdc++.h>
using namespace std;


int t,siz;
string s;
long long int ans;
void magic_box()
{
    int last_index;
    int index=siz;
    while(index>=0&&s[index]=='+')
    {
        index--;
    }
    while(index>=0)
    {
        ans++;
        for(int i=0;i<=index;i++)
        {
            if(s[i]=='-')
            {
                s[i]='+';
            }
            else
            {
                s[i]='-';
            }
        }
        index=siz;
        while(index>=0&&s[index]=='+')
        {
            index--;
        }
    }
}
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        ans=0;
        cin>>s;
        siz=s.size()-1;
        magic_box();
        printf("Case #%d: %lld\n",i,ans);
    }
}
