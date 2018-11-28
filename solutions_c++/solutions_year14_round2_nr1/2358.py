#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
    int t,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        int i,n,j;
        scanf("%d",&n);
        string a[n];
        for(i=0;i<n;i++)
            cin>>a[i];
        vector <char> v[n];
        vector <int> c[n];
        for(i=0;i<n;i++)
        {
            int l=a[i].size();
            v[i].push_back(a[i][0]);
            c[i].push_back(1);
            for(j=1;j<l;j++)
            {
                if(a[i][j]!=v[i][v[i].size()-1])
                {
                    v[i].push_back(a[i][j]);
                    c[i].push_back(1);
                }
                else
                    c[i][c[i].size()-1]++;
            }
        }
        int l=v[0].size();
        for(i=1;i<n;i++)
            if(v[i].size()!=l)
                break;
        if(i<n)
            printf("Fegla Won\n");
        else
        {
            for(i=0;i<l;i++)
            {
                for(j=1;j<n;j++)
                    if(v[j][i]!=v[j-1][i])
                        break;
                if(j<n)
                    break;
            }
            if(i<l)
                printf("Fegla Won\n");
            else
            {
                int ans=0;
                for(i=0;i<l;i++)
                {
                    int sum=0;
                    for(j=0;j<n;j++)
                        sum+=c[j][i];
                    int x1=ceil(double(sum)/n),x2=floor(double(sum)/n),temp1=0,temp2=0;
                    for(j=0;j<n;j++)
                        temp1+=fabs(x1-c[j][i]);
                    for(j=0;j<n;j++)
                        temp2+=fabs(x2-c[j][i]);
                    ans+=temp1<temp2?temp1:temp2;
                }
                printf("%d\n",ans);
            }
        }
    }

    return 0;
}
