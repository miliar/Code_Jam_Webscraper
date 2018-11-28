#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        double c,f,x;
        double ans=0,cnt=0,ans1=0,preans=0,preans1=0,newcnt=2;
        int pa=0,pa1=0;
        cin>>c>>f>>x;

        while(1)
        {
            if(x<c)
            {
                cout<<"Case #"<<i<<": ";
                printf("%.7lf\n",x/2);
                break;
            }
            else{
                if(cnt==0)
                {
                    ans+=c/2;
                    ans1+=x/2;

                    preans=ans;
                    preans1=ans1;

                    cnt++;
                }
                else{
                    newcnt+=f;

                    ans+=c/newcnt;
                    ans1= preans+x/newcnt;

                  /*  if(preans<ans)
                    {
                        pa=1;
                        break;
                    }*/
                    if(preans1<ans1)
                    {
                        pa1=1;
                        break;
                    }
                    else{
                        preans=ans;
                        preans1=ans1;
                    }
                }
            }
        }
        if(pa1==1)
        {
            cout<<"Case #"<<i<<": ";
            printf("%.7lf\n",preans1);
        }
    }

    return 0;
}

