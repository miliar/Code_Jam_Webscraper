#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
bool chk(long long a)
{
    int i,j;
    char num[100];
    sprintf(num,"%d",a);
    i=0;
    j=strlen(num)-1;
    while(i<j)
    {
        if(num[i]!=num[j])return 0;
        i++;
        j--;
    }
    return 1;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,ii;
    long long i,a,b;
    vector<long long> v;
    for(i=1;i<10000000;i++)
    {
        if(chk(i)&&chk(i*i))v.push_back(i*i);
    }
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%I64d %I64d",&a,&b);
        printf("Case #%d: %d\n",ii,upper_bound(v.begin(),v.end(),b)-1-lower_bound(v.begin(),v.end(),a)+1);
    }
}
