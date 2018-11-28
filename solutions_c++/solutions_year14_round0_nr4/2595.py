#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
using namespace std;

int l;
double s[1005],t[1005];
set<double> st;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    for (int cnt=1;cnt<=amm;cnt++)
    {
        scanf("%d",&l);
        for (int i=0;i<l;i++)scanf("%lf",&s[i]);sort(s,s+l);
        for (int i=0;i<l;i++)scanf("%lf",&t[i]),st.insert(t[i]);sort(t,t+l);
        int a1=0,a2=0;
        int p1=0,p2=0;
        while (p1<l)
        {
            if (s[p1]>t[p2])p1++,p2++,a1++;
            else p1++;
        }
        for (int i=0;i<l;i++)
        {
            set<double>::iterator tmp=st.lower_bound(s[i]);
            if (tmp==st.end())a2++,st.erase(st.begin());
            else st.erase(tmp);
        }
        printf("Case #%d: %d %d\n",cnt,a1,a2);
    }
    return 0;
}
