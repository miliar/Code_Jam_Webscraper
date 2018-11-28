#include <iostream>
#include <cstring>
#include <bits/stdc++.h>
#include <cstdlib>
#define ll long long
using namespace std;
vector<ll>vc1;
 long long divis(long long a){
     long long c=sqrt(a);
     //cout<<c<<endl;
   for(long long b=0;b<vc1.size();b++){
    if(a%vc1[b]==0){
          //  cout<<"boobs "<<vc1[b];
            return vc1[b];
    }
   }
     return -1;
 }
int N = 100000100, status[100000100];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out2.o","w",stdout);
     int i, j, sqrtN;
     vc1.push_back(2);
    for( i = 2; i <= N >> 1; i++ ) status[i] = 0;
    sqrtN = int( sqrt((double)N) ); // have to check primes up to (sqrt(N))
    for( i = 3; i <= sqrtN; i += 2 ) {
        if( status[i>>1] == 0 ) {
                vc1.push_back(i);
            // so, i is a prime, so, discard all the multiples
            // j = i * i, because it’s the first number to be colored
            for( j = i * i; j <= N; j += i + i )
                status[j>>1] = 1; // status of the multiple is 1
        }
    }
     long long arr[15][20],mul,k,l;
    for(i=2; i<=10; i++)
    {
        mul=1;
        arr[i][0]=1;
        for(j=1; j<=16; j++)
        {
            mul*=i;
            arr[i][j]=mul;
         //   cout << arr[i][j]<<endl;
        }
    }

     queue<long long>q;
    vector<long long>vc;
    long long ma=999999999999999,ma2=1111111111111112;
    long long a,b,v,d,e,f,c;
    q.push(1);
    while(!q.empty()){
    a=q.front();
   // cout<<a<<endl;
    q.pop();
    if(a>ma){
            if(a%10!=0)
            vc.push_back(a);
    }
        b=a*10+0;
       if(b<ma2)q.push(b);
        b=a*10+1;
       if(b<ma2)q.push(b);
    }
   // cout<<vc.size();

    int iteration = 5,cou=0,p,ck;
    ll num;
    int test,digit,u=1;
    p=50;
    scanf("%d %d %d",&test,&digit,&p);
   // while(test--){
            printf("Case #%d:\n",u++);
   for(i=0;i<vc.size();i++){
    a=vc[i];
    long long tmp=a;
    vector<ll>gc;
    j=2;
    ck=0;
    while(j<=10){
            b=a;
            k=0;
            c=0;
        while(b!=0){
            d=b%10;
            b=b/10;
            c=c+(d*arr[j][k]);
            k++;
        }
       // if(i==2)
        //cout<<c<<" "<<j<<endl;
        f=divis(c);
        if(f==-1){
            ck=1;
            break;
        }
        gc.push_back(f);
        j++;
    }
    if(ck==0){
           printf("%I64d ",tmp);
           for(int lo=0;lo<gc.size();lo++){
            printf(" %I64d",gc[lo]);}
            cout << endl;


            cou++;
    }
    gc.clear();
    if(cou==p)break;
   //}
    }
  //  cout<<cou<<endl;
}
