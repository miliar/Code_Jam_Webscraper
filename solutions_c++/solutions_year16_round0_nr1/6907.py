#include<bits/stdc++.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
#define mod 1000000007
#define ii  pair<int,int>

using namespace std;
typedef long long ll;



using namespace std;
/*struct node
{
    ll nm,tm;
}nd[2000010];

int cmp(const void *a,const void *b)
{
    node *va=(node *)a;
    node *vb=(node *)b;
    if(va->tm==vb->tm)
    {
        if(va->nm<vb->nm)
        return -1;
        else
        return 1;
    }
    else
    {
        if(va->nm<vb->nm)
        return -1;
        else
        return 1;
    }
    if(va->tm==vb->tm)
    return va->nm-vb->nm;
    else
    return va->tm-vb->tm;
}*/

/*ll g(ll a,ll b)
{
    if(b==0)
    return a;
    else
    return g(b,a%b);
}
ll lc(int a,int b)
{
    ll lcm=(a*b)/g(a,b);
    return lcm;
}*/


int main()
{

int tst,t;
freopen("A-large.in", "r", stdin);
freopen("AOUT-LARGE", "w", stdout);
scanf("%d",&t);
for(tst=1;tst<=t;tst++)
{
    long long num,prod;
    int count,digit,i;
    int arr[10];
    for(i=0;i<10;i++)
    arr[i]=0;

    scanf("%lld",&num);
    prod = num;

    while(prod>0){
    digit = prod%10;
    arr[digit]=1;
    prod/=10;
    }
    for(i=0;i<10;i++){
    if(arr[i]==0)
    break;
    }
    if(i==10)
    printf("Case #%d: %lld\n",tst,num);
    else if(num==0)
    printf("Case #%d: INSOMNIA\n",tst);
    else{
    for(count=2;;count++){
    prod = num*count;

    while(prod>0){
    digit = prod%10;
    arr[digit]=1;
    prod/=10;
    }
        for(i=0;i<10;i++){
        if(arr[i]==0)
        break;
        }
        if(i==10){
        printf("Case #%d: %lld\n",tst,count*num);
        break;
        }

    }

    }


}



    return 0;
}
