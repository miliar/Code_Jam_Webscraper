#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)   for(i=a;i>=b;i--)
# define toint(n)   (n-'0')
typedef long long ll;

int MaxinNum(int a[], int top)          // num[] = count of number of elemnts o feach no.
{
    int i,maxi;
    fo(i,1,top)
    if(a[i]>0)
        maxi=i;
    return maxi;                            // i =
}

int Solve1(int d, int num[])
{
    int top,cnt,cost,ans,back=0;
    
    top=MaxinNum(num,1001);
    ans=top;
    
    while(top>3)
    {
        cnt=num[top];
        back+=cnt;
        
        num[top]=0;
        num[top-3]+=cnt;
        num[3]+=cnt;
        
        top=MaxinNum(num,top);
        
        cost=top+back;
        //printf("cost: %d\n",cost);
        if(cost<ans)
            ans=cost;
        
        //if(top<=3)
        //  ans+=top;
    }
    
    return ans;
}

int Solve2(int d, int num[])
{
    int top,cnt,cost,ans,back=0;
    
    top=MaxinNum(num,1001);
    ans=top;
    
    while(top>3)
    {
        cnt=num[top];
        back+=cnt;
        
        num[top]=0;
        num[top/2]+=cnt;
        num[top-top/2]+=cnt;
        
        top=MaxinNum(num,top);
        
        cost=top+back;
        //printf("cost: %d\n",cost);
        if(cost<ans)
            ans=cost;
        
        //if(top<=3)
        //  ans+=top;
    }
    
    return ans;
}

int main()
{
    //freopen("B-small-attempt3.in","r",stdin);
    //freopen("B-small-attempt3.out","w",stdout);
    int t,d,a[1001],num[1001],ans,k,i,ans1,ans2,num2[1001];
    s(t);
    fo(k,1,t+1)
    {
        fo(i,0,1001)
            num[i]=num2[i]=0;
        
        s(d);
        fo(i,0,d){
            s(a[i]);
            num[a[i]]++;
        }

        fo(i,1,1001)
            num2[i]=num[i];
        
        ans1=Solve1(d,num2);
        ans2=Solve2(d,num);

        ans1<ans2?ans=ans1:ans=ans2;
        
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}