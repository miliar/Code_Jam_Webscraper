#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int t;
long long l, r;
long long a, b;
char tmp[20];
long long list[100];
int tail;
int count;

bool judge(long long x);//
long long pal(int x, int insert);

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int i, j;

    list[1]=1; list[2] = 4; list[3]=9;
    tail = 4;
    for (i=1; i<=999999; i++)
    {
        a = pal(i, -1);
        b = a*a;
        if (b>100000000000000) break;
        if (judge(b))
        {
            list[tail] = b;
            tail++;
        }
        for (j=0; j<=9; j++)
        {
            a = pal(i, j);
            b = a*a;
            if (b>100000000000000) break;
            if (judge(b))
            {
                list[tail] = b;
                tail++;
            }
        }
    }
    cin>>t;
    for (i=1; i<=t; i++)
    {
        cin>>l>>r;
        count = 0;
        for (j=1; j<tail; j++)
            if (list[j]>=l && list[j]<=r)
                count++;
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}

bool judge(long long x)
{
    int i, len;
    sprintf(tmp, "%lld", x);
    len = strlen(tmp);
    for (i=0; i<=len/2; i++)
        if (tmp[i]!=tmp[len-i-1])
            return false;
    return true;
}

long long pal(int x, int insert)
{
    long long result = x;
    int i, len;
    if (insert>-1)
        result = result*10+insert;
    sprintf(tmp, "%d", x);
    len = strlen(tmp);
    for (i=len-1; i>=0; i--)
        result = result*10+tmp[i]-'0';
    return result;
}