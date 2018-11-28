#include<bits/stdc++.h>
#define LL long long int
using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef map<int, int> mii;

ll _sieve_size;
bitset<100000010> bs;   // 10^7 should be enough for most cases
vi primes;   // compact list of primes in form of vector<int>
void sieve(ll upperbound=100000010) {          // create list of primes in [0..upperbound]
  _sieve_size = upperbound + 1;                   // add 1 to include upperbound
  bs.set();                                                 // set all bits to 1
  bs[0] = bs[1] = 0;                                     // except index 0 and 1
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    // cross out multiples of i starting from i * i!
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back(i);  // also add this vector containing list of primes
}
 }                                           // call this method in main method
ll isprime(ll p)
{
    for(ll i=0;primes[i]*primes[i] <= p ;i++)
        if(p%primes[i] ==0)
        return primes[i];
    return -1;
}
 int A[20];
 ll B[20];
 ll Power[11][20];
 int J;
 void call(int i)
 {
             if(J>=50)
                return ;
     if(i==15)
     {
         LL p=0;
         int t=1;
         for(int j=2;j<=10 && t;j++)
         {
             p=0ll;
             for(int k=0;k<16;k++)
                p+= A[k]*Power[j][15-k];
            ll a=isprime(p);
            if(a==-1) t=0;
            B[j]=a;
         }
         if(t)
         {
             printf("%lld",p);
             for(int k=2;k<=10;k++)
                    printf(" %lld",B[k]);
             printf("\n");
             J++;
             if(J>=50)
                return ;
         }
         return;
     }
     A[i]=0;
     call(i+1);
             if(J>=50)
                return ;
     A[i]=1;
     call(i+1);
             if(J>=50)
                return ;
 }
int main()
{
   // freopen("C-small-attempt0.in","r",stdin);
  //  freopen("codejam.txt","w",stdout);
    int T,I=1;
    J=0;
    for(int i=1;i<=10;i++)
    {
        Power[i][0]=1;
        for(int j=1;j<17;j++)
            Power[i][j]=Power[i][j-1]*1ll*i;
    }
    scanf("%d",&T);
    printf("Case #1:\n");
    sieve();
    A[0]=1;
//    A[1]=0;
//    A[2]=0;
//    A[3]=0;
//    A[4]=1;
    A[15]=1;
    T=1;
    call(1);
    //LL p=0;
//         int t=1;
//         for(int j=2;j<=10 && t;j++)
//         {
//             p=0ll;
//             for(int k=0;k<6;k++)
//                p+= (A[k]*Power[j][5-k]);
//            //cout<<p<<" ";
//        if(isprime(p)) t=0;
//         }
//         cout<<t<<endl;
   // while(T--)
    //{
    //printf("Case #%d: ",I++);
   // scanf("%d",&n);
    //scanf("%s",str);
    //n=strlen(str);
//    int n;
//    memset(dp,-1,sizeof(dp));
//    int R=n;
//    for(int i=n-1;i>=0;i--)
//    {
//       Right[0][i]=R;
//        if(str[i]=='+')
//            R=i;
//    }
//    R=n;
//    for(int i=n-1;i>=0;i--)
//    {
//        Right[1][i]=R;
//        if(str[i]=='-')
//            R=i;
//    }
//    int t=(str[0]=='-')?1:0;
//    printf("%d\n",min(call(Right[1-t][0],t),1+call(Right[1-t][0],1-t)));
    //}
    return 0;
}
