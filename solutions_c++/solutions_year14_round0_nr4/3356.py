#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int war(vector<double> a,vector<double> b)
{
    int ret=0;
    vector<bool> used(b.size(),false);
    for(int i=0;i<a.size();i++)
    {
        bool found=false;
        for(int j=b.size()-1;j>=0&&!found;j--)
        {
            if(b[j]>a[i]&&!used[j])
            {
                found=true;
                used[j]=true;
                ret++;
            }
        }
    }
    return a.size()-ret;

}

int dwar(vector<double> a ,vector<double> b)
{
    int ret=0;
    int as=0,bs=0;
    for(int i=0,size=a.size();i<size;i++)
    {
        if(a.back()>b.back())
        {
            a.pop_back();
            b.pop_back();
            ret++;
        }
        else{
            a.pop_back();

        }
    }
    return ret;
}
bool comp(double a,double b)
{
    return a>b;
}
int main()
{
    freopen("d_large.in","r",stdin);
    freopen("d_large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=0;test<t;test++)
    {
        int n;
        scanf("%d",&n);
        vector<double> in[2];
        for(int i=0;i<2;i++)
        for(int j=0;j<n;j++)
        {
            double tm;
            scanf("%lf",&tm);
            in[i].push_back(tm);
        }
        sort(in[0].begin(),in[0].end(),comp);
        sort(in[1].begin(),in[1].end(),comp);
/*
         for(int i=0;i<2;i++)
         {
             for(int j=0;j<n;j++)
            {
                printf("%lf ",in[i][j]);
            }
            printf("\n");
         }
*/

        printf("Case #%d: %d %d\n",test+1,dwar(in[0],in[1]),war(in[0],in[1]));
     //   printf("djfsj\n");

    }
    return 0;
}
