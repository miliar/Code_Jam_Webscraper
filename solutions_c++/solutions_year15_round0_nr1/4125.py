#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);

    for(int it=1;it<=T;it++)
    {
        int Smax;
        scanf("%d",&Smax);
        char S[Smax+1];
        scanf("%s",&S);
        int people=0;
        int ans=0;
        for(int i=0;i<=Smax;i++)
        {
            if(people>=i)
            {
                people+=S[i]-'0';
            }
            else
            {
                int temp = i - people;
                ans+=temp;
                people+=temp;
                people+=S[i]-'0';
            }
        }
        printf("Case #%d: %d\n",it,ans);
    }


}
