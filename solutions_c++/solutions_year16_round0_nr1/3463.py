#include<bits/stdc++.h>
#include<string>
using namespace std;
#define ll long long int
vector<bool> is_present(10);
bool fill_digits(ll num)
{
    while(num>0)
    {
        is_present[num%10]=true;
        num=num/10;
    }
    for(ll i=0;i<10;i++)
    {
        if(is_present[i]==false)
            return false;
    }
    return true;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    ll m,ans,test,i,j,num,index,temp;
    bool flag;
    scanf("%lld",&test);
    for(i=1;i<=test;i++)
    {
        index=1;
        flag=false;
        fill(is_present.begin(),is_present.end(),false);
        scanf("%lld",&num);
        if(num==0)
            printf("Case #%lld: INSOMNIA\n",i);
        else
        {
            while(1)
            {
                temp=num*index;
                flag=fill_digits(temp);
                if(flag==true)
                    break;
                index++;
            }
            num=temp;
            printf("Case #%lld: %lld\n" ,i,num);
        }
    }
    return 0;
}
