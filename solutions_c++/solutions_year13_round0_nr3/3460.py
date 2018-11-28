#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
vector <LL> v;
bool ispa(LL t)
{
    if(t == 0)return true;
    int cnt = 0;
    int num[20];
    while(t)
    {
        num[cnt++] = t%10;
        t/=10;
    }
    for(int i=0;i<cnt/2;i++)
        if(num[i] != num[cnt-1-i])return false;
    return true;
}
int main()
{
    //freopen("C-small-attempt2.in","r",stdin);
    //freopen("output.txt","w",stdout);
    v.push_back(0);
    v.push_back(4);
    v.push_back(1);
    v.push_back(9);
    for(int i=1;i<1000;i++)
    {
        if(i%10 == 0)continue;
        char num[20];
        sprintf(num,"%d",i);
        int len = strlen(num);
        LL t1 = 0,t[20];
        for(int j=0;j<10;j++)
            t[j] = 0;
        for(int j=0;j<len;j++)
        {
            t1 *= 10;
            t1 += num[j]-'0';
        }
        for(int j=0;j<10;j++)
            t[j] = j+t1*10;
        for(int j=len-1;j>=0;j--)
        {
            t1 *= 10;
            t1 += num[j]-'0';
            for(int k=0;k<10;k++)
            {
                t[k] *= 10;
                t[k] += num[j]-'0';
            }
        }
        LL q = (LL)t1*t1;
        if(ispa(q))v.push_back(q);
        for(int j=0;j<10;j++)
        {
            q = (LL)t[j]*t[j];
            if(ispa(q))v.push_back(q);
        }
    }
    sort(v.begin(),v.end());
    /*int len = v.size();
    for(int i=0;i<len;i++)
        cout << v[i] << endl;*/
    int T;
    scanf("%d",&T);
    int cas = 1;
    while(T--)
    {
        printf("Case #%d: ",cas++);
        LL a,b;
        cin >> a >> b;
        int nn = v.size();
        LL ans = 0;
        for(int i=0;i<nn;i++)
            if(v[i]>=a && v[i]<=b)ans++;
        cout << ans << endl;

    }
    return 0;
}
