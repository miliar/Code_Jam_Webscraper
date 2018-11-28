#include<bits/stdc++.h>
#define ii long long int

using namespace std;

bool cnt[110];

int n;

bool check()
{
    for(int i=0;i<n;i++)
    {
        if(cnt[i]==0)
            return 0;
    }
    return 1;
}

void func(int ind)
{
    for(int i=0;i<ind;i++)
    {
        cnt[i]=!cnt[i];
    }
}

int main()
{
    //freopen("outlar.txt","w",stdout);
    int cas=1;
    int test;
    scanf("%d",&test);
    while(test--)
    {
        string x;
        cin>>x;
        n=x.length();
        //printf("n:%d\n",n);
        for(int i=0;i<n;i++)
        {
            if(x[i]=='-')
            {
                cnt[i]=0;
            }
            else
            {
                cnt[i]=1;
            }
        }
//        for(int i=0;i<n;i++)
//        {
//            printf("%d ",cnt[i]);
//        }
//        printf("\n");
        int moves=0;
        int ind=0;
        while(!check()&&ind<=n)
        {
            /// start of a move !!
            if(cnt[ind]==0)
            {
                while(cnt[ind]==0&&ind<n)
                {
                    ind++;
                }
                func(ind);
            }
            else
            {
                while(cnt[ind]==1&&ind<n)
                {
                    ind++;
                }
                func(ind);
            }
            //printf("ind:%d\n",ind);
            moves++;
            ind=0;
        }
        printf("Case #%d: %d\n",cas++,moves);
    }
    return 0;
}
// -+-+-+-+-+
// +-+-
