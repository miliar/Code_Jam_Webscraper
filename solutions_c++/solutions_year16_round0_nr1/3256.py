#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,rem) memset(in,rem,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)

int main()
{
    int i;
     freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout); 
    int Tcases;
    scanf("%d", &Tcases);
    for(int tc=1;tc<= Tcases;tc++) {
        long int num1,num,rem=0;
        int j=2,ID=0;
        cin>>num;
        num1=num;
        bool check[10];
       for(i=0;i<10;i++)
       {
           check[i]=false;
       }
       if(num==0)
       {
          printf("Case #%d: INSOMNIA",tc);
          cout<<"\n";

       }
       else
       {
       while(ID<10)
       {

          while(num!=0)
          {
              rem=num%10;
              num=num/10;
              if(check[rem]==false)
              {
              check[rem]=true;
              ID++;
              }
          }
       long int b=num1;
       b=b*j;
       num=b;
       j++;
       }
       cout<<"Case #"<<tc<<": "<<num-num1<<"\n";
       }

    }
    return 0;
}

