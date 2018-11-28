#include <bits/stdc++.h>
using namespace std;

int t;
long long int n;
set<int>s_temp;
long long int temp=1;
void another_magic_box(long long int temp_n)
{
    //cout<<temp_n<<endl;
    while(temp_n!=0)
    {
        s_temp.insert(temp_n%10);
        temp_n=temp_n/10;
    }
}
void magic_box()
{
    while(s_temp.size()!=10)
    {
        another_magic_box(n*temp);
        temp++;
    }
}
int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {

        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
        }
        else
        {
            temp=1;
            magic_box();
            printf("Case #%d: %lld\n",i,n*(temp-1));
        }
        s_temp.clear();
    }
}
