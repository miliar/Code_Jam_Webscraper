#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

long long fp[10000007];
int cnt;
int dig[15],nums;

bool check_fp(long long x)
{
    nums=0;
    while(x)
    {
        dig[nums]=x%10;
        x/=10;
        nums++;
    }
    for(int i=0;i<nums/2;i++)
    {
        if(dig[i]!=dig[nums-i-1])return false;
    }
    return true;
}

// 2*n-1,2*n
//1,2 1 11
//3,4 121 1221
//5,6 12321 123321
//7 1234321
void inital()
{
    //cnt=0;
    long long tmp;
    //1,2
    for(int i=0;i<10;i++)
    {
        if(check_fp(i*i))fp[cnt]=i*i,cnt++;
    }
    for(int i=1;i<10;i++)
    {
        tmp=10*i+i;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
        //if(check_fp(tmp))fp[cnt]=10*i+i,cnt++;
    }
    //3,4
    for(int i=10;i<100;i++)
    {
        tmp=10*i+i/10;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
        //if(check_fp(10*i+i/10))fp[cnt]=10*i+i/10,cnt++;
    }
    for(int i=10;i<100;i++)
    {
        tmp=100*i+(i%10)*10+i/10;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
        //if(check_fp(100*i+(i%10)*10+i/10))fp[cnt]=100*i+(i%10)*10+i/10,cnt++;
    }
    //5,6
    for(int i=100;i<1000;i++)
    {
        tmp=100*i+((i/10)%10)*10+i/100;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
        //if(check(100*i+((i/10)%10)*10+i/100))fp[cnt]=100*i+((i/10)%10)*10+i/100,cnt++;
    }
    for(int i=100;i<1000;i++)
    {
        tmp=1000*i+(i%10)*100+((i/10)%10)*10+i/100;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
        //if(check_fp())
    }
    //7
    for(int i=1000;i<10000;i++)
    {
        tmp=1000*i+((i/10)%10)*100+((i/100)%10)*10+i/1000;tmp*=tmp;
        if(check_fp(tmp))fp[cnt]=tmp,cnt++;
    }
}

int find(long long x,long long y)
{
    int ret=0;
    for(int i=0;i<cnt;i++)
      if(fp[i]>=x && fp[i]<=y)ret++;
    return ret;
}

int main()
{
    //freopen("C-large-1.in","r",stdin);
    //freopen("C.out.txt","w",stdout);
    int t;
    long long A,B;
    inital();
    /*cout<<cnt<<endl;
    for(int i=0;i<100;i++)
      cout<<fp[i]<<" ";
    */
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>A>>B;
        cout<<"Case #"<<i<<": ";
        cout<<find(A,B)<<endl;
    }
    return 0;
}
