#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);


typedef long long LL;



vector<int> v;
int val;
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int T,cs,i,j,k,n,x;


    scanf("%d",&T);

    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);

        scanf("%d",&n);
        v.clear();


        for(i=0;i<n;i++)
        {
            scanf("%d",&val);
            v.push_back(val);
        }

        int ans=0;
        for(i=0;i<n;i++)
        {
            int mn=1000000010;
            int pos;
            for(j=0;j<v.size();j++)
            {
                if(v[j]<mn)
                {
                    mn=v[j];
                    pos=j;
                }
            }
            ans+=min(pos,(int)v.size()-1-pos);


            v.erase(v.begin()+pos);
        }
        printf("%d\n",ans);
    }



    return 0;
}
