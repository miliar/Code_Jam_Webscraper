#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include <sstream>
using namespace std;
int main()
{
    int t,i,ca=0,c;
    double p,q,u,v,k,a;
  //freopen("A-small-attempt4.in","r",stdin);
 //   freopen("out4.txt","w",stdout);
    scanf("%d",&t);
    string s,x,y;
    while(t--)
    {
        ca++;
        cin>>s;
        i=0;
        c=0;
        while(1)
        {
            if(s[i]=='/')
            {
               c=i;
               break;
            }
            i++;
        }
        x=s.substr(0,c);
        y=s.substr(c+1);
       // cout<<x<<" "<<y;
        istringstream ( x ) >> p;
        istringstream ( y ) >> q;
       // cout<<p<<" "<<q<<endl;
        if(((int)q)%2!=0)
        {
           ///cout<<s<<" ";
            printf("Case #%d: impossible\n",ca);
        }
        else
        {
           // cout<<s<<" ";
           u=q/p;
           v=log(q)/log(2);
           k=ceil(v);
           if(k!=v)
           {
                printf("Case #%d: impossible\n",ca);
           }
           else
           {
                a=ceil((log(u))/log(2));
             printf("Case #%d: %0.lf\n",ca,a);
           }
        }
    }
    return 0;
}
