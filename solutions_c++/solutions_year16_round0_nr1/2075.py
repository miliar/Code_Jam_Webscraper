#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;
int mp[15];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    while (cin>>T)
    {
        for (int ca=1;ca<=T;ca++)
        {
         long long N,k,i,j,t;
         cin>>N;
         if (N==0) {printf("Case #%d: INSOMNIA\n",ca);continue;}
         k=2000;
         memset(mp,0,sizeof mp);
         for (i=1;i<=k;i++)
            {
                t=N*i;
                while (t>0) {mp[t%10]=1;t=t/10;}
                int flag=1;
                for (j=0;j<10&&flag;j++)
                  flag=mp[j];
                if (flag) {printf("Case #%d: %d\n",ca,i*N);break;}

            }
        if (i>k) printf("Case #%d: INSOMNIA\n",ca);

        }

    }



    fclose(stdin);
    fclose(stdout);
    return 0;

}
