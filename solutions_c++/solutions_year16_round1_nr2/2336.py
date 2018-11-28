#include <bits/stdc++.h>
using namespace std;
map<int,int>m;
vector<int>v;
int main()
{
    int a,b,c,d,i,j,k,p,q,r,s,T;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&b);
         m.clear();
         v.clear();
        for(j=1;j<=2*b-1;j++)
        {
            for(k=1;k<=b;k++)
            {
                scanf("%d",&p);
                m[p]++;
            }



        }
        for(j=1;j<=2500;j++)
        {
            if(v.size()<b)
            {
                if(m[j]%2!=0)
                    v.push_back(j);
            }
        }
        printf("Case #%d: ",i);

        for(j=0;j<v.size();j++)
        {
            printf("%d ",v[j]);
        }
        printf("\n");


    }
    return 0;
}
