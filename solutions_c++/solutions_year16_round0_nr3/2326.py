#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<stack>
using namespace std;
int t,n,j;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%lld",&t);
    vector<long long> v;
    for(int o=1; o<=t; o++)
    {
        scanf("%lld%lld",&n,&j);
        printf("Case #%d:\n",o);
        for(long long i=0; i<=(1<<(n-1))-1; i++)
        {
            int e=0;
            v.clear();
            for(int s=2; s<=10; s++)
            {
                long long m=1;
                long long sum=1;
                for(int p=0; p<=n-3; p++)
                {
                    m*=s;
                    sum+=m*((i&(1<<p))?1:0);
                }
                m*=s;
                sum+=m;
                int f=0;
                for(long long d=2; d*d<=sum; d++)
                {
                    if(sum%d==0) {f=1; v.push_back(d); break;}
                }
                if(f==0) {e=1; break;}
            }
            if(e==1) continue;
            int k=i;
            stack<int> st;
            while(k>0) {st.push(k%2); k/=2;}
            printf("1");
            for(int g=1; g<=n-2-st.size(); g++) printf("0");
            while(!st.empty()) {printf("%d",st.top()); st.pop();}
            printf("1");
            for(int g=0; g<=8; g++)
                printf(" %lld",v[g]);
            printf("\n");
            j--;
            if(j==0) break;
        }
    }
    return 0;
}
