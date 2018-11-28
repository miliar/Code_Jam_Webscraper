#include<bits/stdc++.h>
using namespace std;
string str;
int ln;
bool chck()
{
    int i;
    for(i=0;i<ln;i++)
    {
        if(str[i]=='-')
            return false;
    }
    return true;
}
void ulta(int n)
{
    int i,j=n;
    for(i=0;i<=n;i++,n--)
    {
        swap(str[i],str[n]);
    }
    for(i=0;i<=j;i++)
    {
        if(str[i]=='-')
            str[i]='+';
        else str[i]='-';
    }

}
int main()
{
    int n,i,j,k,l,t;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>n;
    for(t=1;t<=n;t++)
    {
        cin>>str;
        ln=str.size();
        l=0;
        printf("Case #%d: ",t);
        if(chck()){
            cout<<0<<endl;
            continue;
        }
        while(1)
        {
            for(i=1;i<ln;i++)
            {
                if(str[i]!=str[0])
                    break;
            }
            ulta(i-1);

            l++;
            if(chck())
                break;
        }
        cout<<l<<endl;
    }
    return 0;
}
