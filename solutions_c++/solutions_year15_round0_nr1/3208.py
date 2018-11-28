# include<cstdio>
# include<algorithm>
# include<iostream>
# include<cstring>
# include<string>
# include<cmath>

# define N 1010
# define M 100010

typedef long long ll;

using namespace std;

int n;
char s[N];


int main()
{
    //freopen("C:\\Users\\DELL\\Desktop\\A\\A-large.in","r",stdin);
    //freopen("out.out","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%s",&n,s);
        int res = 0,cnt = 0;
        //if(n+1 != strlen(s))
        //printf("error!\n");break;
        for(int i=0;i<=n;i++)
        {
            if(cnt >= i)    cnt+=s[i]-'0';
            else
            {
                res+=i-cnt;
                cnt = i+s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",t,res);
    }
    return 0;
}

