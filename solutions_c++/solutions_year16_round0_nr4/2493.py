// #CodeLikeTheMartian
#include <bits/stdc++.h>

#define     MOD       1000000007
#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     lb        lower_bound
#define     ub        upper_bound
#define     SIZE      1000001
#define     MAX       INT_MAX
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;
int main()
{
    int T;
    FILE *fp=fopen("A_smallOutput.t xt","w");
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        ll K,C,S;
        cin>>K>>C>>S;

      //  fprintf(fp,"Case #%d: ",t);
        cout<<"Case #"<<t<<": ";
        if(S>=K)
        {
        for(int i=1;i<=K;++i)
           {
    //         fprintf(fp,"%d ",i);
             cout<<i<<" ";
           }

        }
        else
        {
  //          fprintf(fp,"IMPOSSIBLE");
            cout<<"IMPOSIIBLE";
        }
        cout<<endl;
//        fprintf(fp,"\n");
    }
	return 0;
}

