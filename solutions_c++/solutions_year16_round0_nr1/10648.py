#include<bits/stdc++.h>
#define loop(i,a,b) for(i=a;i<b;i++)
#define M 1000000007
#define ull unsigned long long
#define ll long long
#define pb push_back
#define popb pop_back
#define pf push_front
#define mp make_pair
#define sz(x) ((int)x.size())
#define si(n) scanf("%d",&n)
#define gi(n) printf("%d\n",n)
#define sl(n) scanf("%I64d",&n)
#define gl(n) printf("%I64d\n",n)
#define nl() printf("\n")
#define limit 1000009

using namespace std;


int main()
{
freopen("ABC.in","r",stdin);
freopen("out3.txt","w",stdout);
   int t;
   cin>>t;
  int j;


   loop(j,1,t+1)
   {
         ll n,i,val;
         cin>>n;
         set <int> s;

         i=1;
         val=n;

         if(n==0)
         cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
         else{

            while(1)
            {
             n= val*i;
             ll num=n;
             while(num>0)
             {
                    int r = num%10;

                    s.insert(r);

                    num /=10;
             }
             //cout<<n<<" here ";

             if(s.size()==10)
             break;

             i++;

            }

            cout<<"Case #"<<j<<": "<<n<<endl;


         }





   }


  return 0;

}


