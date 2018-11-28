#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int fsn[1000];
bool isPalindrome(int num)
{
    if(num<10)return true;
    if(num<100)
    {
        if(num/10==num%10)return true;
        else return false;
    }
    else if(num/100==num%10)return true;
    else return false;
}
void dolist()
{
    memset(fsn,0,sizeof(fsn));
    fsn[1]=1;
    for(int i=2; i<=1000; i++)
    {
        int t=sqrt(i+0.0);
        if(isPalindrome(i) && t*t==i && isPalindrome(t))fsn[i]=1;
    }
}
int main()
{
    int T;
    int a,b;

    dolist();
    for(int i=1; i<=1000; i++)
        fsn[i]+=fsn[i-1];
   // freopen("in.txt","r",stdin);

   // freopen("C-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int cas=1; cas<=T; cas++)
    {
        cin>>a>>b;
        printf("Case #%d: %d\n",cas,fsn[b]-fsn[a-1]);
    }
    return 0;
}
