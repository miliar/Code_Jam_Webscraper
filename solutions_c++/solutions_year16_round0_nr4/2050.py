#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main()
{
    int T,ca;
    freopen("D-large (1).in","r",stdin);
   freopen("d.out","w",stdout);
    cin>>T;
    for (ca=1;ca<=T;ca++)
    {
        int K,C,S;
        cin>>K>>C>>S;
        if (K>C*S) {printf("Case #%d: IMPOSSIBLE\n",ca);continue;}
        int i,j;
        int p[200];
        for (i=1;i<=200;i++) p[i]=0;
        for (i=1;i<=K;i++) p[i]=i-1;
        printf("Case #%d: ",ca);
        long long t,t2,t3;
        t2=1;
        for (i=1;i<C;i++)
        t2=t2*K;
       // cout<<t2<<endl;
        t3=0;
        for (i=1;i<=K;)
          {
              t=0;
              for (j=i;j<i+C;j++)
              {
                  t=t*K+p[j];
                //  cout<<"!"<<endl;
              }
              cout<<t+1<<' ';
              //t3+=t2;
              i=j;
          }
          cout<<endl;
    }
    fclose(stdout);
  //  fclose(stdin);


    return 0;
}
