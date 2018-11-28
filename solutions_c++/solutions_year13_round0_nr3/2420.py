#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
#include<string>
#include<cstring>
#include<cmath>
bool palin[10000005];
int main()
{
    long long int tc,test;
    long long int a,b,chk,l,h,temp,no,c,t,i;
     freopen("C:\\Users\\SAGAR\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\SAGAR\\Desktop\\output.txt","w",stdout);
    memset(palin,false,sizeof(palin));
    for(i=1;i<10000005;i++)
    {
                           temp=i;no=0;
                           while(temp)
                           {
                           c=temp%10;
                           no=no*10+c;
                           temp/=10;
                           }
                           if(no==i)
                           palin[i]=true;
    }
    scanf("%lld",&test);
    for(tc=1;tc<=test;tc++)
    {
                           long long int count=0;
                           scanf("%lld%lld",&a,&b);
                           l=(long long int)sqrt(a);
                           h=(long long int)sqrt(b);
                           for(i=l;i<=h;i++)
                           {
                                            if(a<=(i*i)&&(i*i)<=b)
                                            {
                                            if(palin[i])
                                            {
                                                        chk=i*i;
                                                        temp=chk;no=0;
                                                        while(temp)
                                                        {
                                                                   c=temp%10;
                                                                   no=no*10+c;
                                                                   temp/=10;
                                                        }
                                            if(no==chk)
                                            count++;
                                            }
                                            }
                           }
                            printf("Case #%lld: %lld\n",tc,count);
    }
    return 0;
}
    
