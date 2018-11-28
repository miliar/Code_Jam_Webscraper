#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<limits.h>
#define N 1000005
using namespace std;


int dp[20][70000]={0,};

int cnt(int row,int col,int n)
{
    cout<<row<<" "<<col<<" "<<n<<endl;
    int case1 = ((row+1)/2)*((col+1)/2) + (row/2)*(col/2);
    cout<<case1<<endl;
    if(n<=case1) return 0;
    int ans = 0;
    n-=(case1);
    int side3 = col/2+row/2+((row%2==0)?((col-1)/2):(col/2));
    if(side3%2==0)
    {
            if(row%2==0||row==1) side3+=(row-1)/2;
            else side3 += (row-3)/2;
    }
    else
    {
        side3+=row/2;
    }

    cout<<"side"<<side3<<endl;
    if((row*col)%2==0) //2  side
    {
        if(n<3) return 2*n;
        n-=2;
        ans+=4;
        side3-=2;
    }
    //3 side
    if(n<=side3) return ans+n*3;
    n-=side3;




    return ans+n*4;
}
int get(int n,int b)
{
    return ((n&(1<<b))!=0)?1:0;
}
int getPos(int n,int R,int C,int r,int c)
{
    return get(n,r*C+c);
}
int getCnt(int n,int R,int C)
{
    int ans =0;
    for(int i=0;i<R;i++)
    for(int j=0;j<C;j++)
    {
        if(getPos(n,R,C,i,j)==0) continue;
        if(j+1<C && getPos(n,R,C,i,j+1)==1) ans++;
        if(i!=0) ans+=getPos(n,R,C,i-1,j);
    }
    //cout<<n<<" "<<R<<" "<<C<<endl;
    return ans;
}

int cnt2(int r,int c,int n)
{
    int ans = INT_MAX;
    for(int i=0;i<=(1<<(r*c));i++)
    {
        if(__builtin_popcount(i)==n) ans=min(ans,getCnt(i,r,c));
    }
    return ans;
}


int main()
{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);


    int T;
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int r,c,n;
        cin>>r>>c>>n;
       // cout<<n;
        printf("Case #%d: %d\n",t+1,cnt2(r,c,n));
    }
    return 0;
}
