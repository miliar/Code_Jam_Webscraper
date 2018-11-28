#include<iostream>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<climits>
using namespace std;
#define mx 100001
#define read(x) scanf("%d",&x)
#define MOD 1000000007
typedef pair<int,int> pr;
typedef long long int ull;



  int main()
  {
    int t,i,j,tt;
    read(t);
    ull k,c,s;
    for(tt=1;tt<=t;tt++)
    {
      cin>>k>>c>>s;
      printf("Case #%d:",tt);
      ull base=(ull)pow(k,c-1);
      //cout<<base;
      ull pos=1;
      for(i=0;i<s;i++)
      {
        printf(" %lld",pos);
        pos+=base;
      }
      cout<<endl;
    }

  }