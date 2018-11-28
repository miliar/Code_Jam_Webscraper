#include<iostream>
#include<stack>
#include<math.h>
#include<stdio.h>
using namespace std;

int fair[10000];

int main()
{
   // freopen("q.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        int a,b;
        cin>>a>>b;
        int cnt=0;
        for(int h=a;h<=b;h++)
        {
            int flag=0;
            int v=sqrt(h);

            if(v*v==h)
            {
                int m=h,n=h;
                stack<int>A;

                while(m!=0)
                {
                    int g=m%10;
                    m=m/10;
                    A.push(g);
                }

                while(n!=0)
                {
                    int g=n%10;
                    n=n/10;
                    int r=A.top();
                    A.pop();
                    if(r!=g)
                    {
                        flag=1;
                        break;
                    }
                }

                if(flag==0)
                {
                    int p=v,q=v;
                    stack<int>AX;

                    while(p!=0)
                    {
                        int g=p%10;
                        p=p/10;
                        AX.push(g);
                    }

                    while(q!=0)
                    {
                        int g=q%10;
                        q=q/10;
                        int r=AX.top();
                        AX.pop();
                        if(r!=g)
                        {
                            flag=1;
                            break;
                        }
                    }
                }

                if(flag==0) cnt++;
            }
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    return 0;
}
