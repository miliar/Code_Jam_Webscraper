#include<bits/stdc++.h>
#define ii long long int
#define MAXSIZE 2001

using namespace std;

map<int,int> mp;
map<int,int> ::iterator it;

int main()
{
    //freopen("outttttlar.txt","w",stdout);
    int test;
    scanf("%d",&test);
    int cas=1;
    while(test--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                int x;
                scanf("%d",&x);
                if(mp.find(x)==mp.end())
                {
                    mp[x]=1;
                }
                else
                {
                    mp[x]++;
                }
            }
        }
        vector<int> res;
        for(it=mp.begin();it!=mp.end();it++)
        {
            if(it->second%2)
            {
                res.push_back(it->first);
            }
        }
        int l=res.size();
        printf("Case #%d: ",cas++);
        for(int i=0;i<l;i++)
        {
            printf("%d",res[i]);
            if(i!=l-1)
                printf(" ");
        }
        printf("\n");
        mp.clear();
    }
    return 0;
}

//50
//c 1 30
//q 3 1
