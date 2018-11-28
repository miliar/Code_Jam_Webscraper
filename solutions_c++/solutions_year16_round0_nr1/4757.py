#include <iostream>
#include<stdio.h>
# define ll long long int
using namespace std;
int visit[10];
int main()
{
    freopen("input.in","r",stdin);
    freopen("outputt2.txt","w",stdout);
    int test;
    ll n,ans,temp;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        for(int i=0;i<10;i++)
            visit[i]=0;
        cin>>n;
            if(n==0)
            {
                ans=0;
//                break;
            }
            else
            {
 //           cout<<"yoyoyoyoyo";
                temp=n;
               int j=1;
        while(1)
        {
            temp=n*j;
            while(temp)
            {
                visit[temp%10]=1;
                temp/=10;
            }
            int i;
            for(i=0;i<10;i++)
            {
            if(visit[i]==0)
                break;
            }
            if(i==10)
            {
                ans=n*j;
                break;
            }
            j++;
        }
            }
        if(ans==0)
        printf("Case #%d: INSOMNIA\n",t+1);
        else
        printf("Case #%d: %lld\n",t+1,ans);
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
