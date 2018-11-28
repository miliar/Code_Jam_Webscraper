#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>

using namespace std;

int abs(int a)
{
    if(a<0) return a*-1;
    return a;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int tt = 1;tt<=t;tt++)
    {
        int n;
        scanf("%d",&n);
        string tab[200];
        for(int i=0;i<n;i++)
        {
            cin >> tab[i];
        }
        string lt = "";
        int count[200][200]={0};
        lt += tab[0][0];
        int p = 0;
        for(int i=1;i<tab[0].length();i++)
        {
            if(tab[0][i]!=tab[0][i-1])
            {
                lt+= tab[0][i];
            }
        }
        bool chk = false;
        //cout << lt << "\n";
        for(int i=0;i<n;i++)
        {
            int pp = 0;
            if(tab[i][0]!=tab[0][0])
            {
                chk = true;
                break;
            }
            count[i][0]++;
            for(int j=1;j<tab[i].length();j++)
            {
                if(tab[i][j]!=lt[pp])
                {
                    pp++;
                    if(pp>=lt.length())
                    {
                        chk = true;
                        break;
                    }
                    if(tab[i][j]!=lt[pp])
                    {
                        chk = true;
                        break;
                    }
                }
                count[i][pp]++;
            }
            if(pp!=lt.length()-1)
                chk = true;
            if(chk) break;
        }
        printf("Case #%d: ",tt);
        if(chk)
        {
            printf("Fegla Won\n");
            continue;
        }
        int ans = 0;
        for(int i=0;i<lt.length();i++)
        {
            //printf("%d %d\n",count[0][i],count[1][i]);
            int sum = 0;
            for(int j=0;j<n;j++)
            {
                sum += count[j][i];
            }
            //cout << sum << "\n";
            for(int j=0;j<n;j++)
            {
                ans+=fabs((int)round((double)sum/n)-count[j][i]);
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
