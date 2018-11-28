#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <utility>
#define inf 1000000000
#define ll long long
#define M 1000002013

using namespace std;

struct ss{
    ll t,p,id;
};

ll n,m;

vector <ss> myvec;
stack <ss> st;

bool mycomp(ss x,ss y)
{
    if(x.t!=y.t) return (x.t<y.t);
    return (x.id<y.id);
}

ll sum(ll x)
{
    return ( (x*(x+1))/2)%M  ;
}

ll cost(ll d,ll mul)
{
    mul%=M;
    ll ret=sum(n)-sum(n-d);

    ret%=M;

    return (ret*mul)%M;



}

int main()
{
   int Test,cas;
   ll a,b,c,ac,ret,i;
   ss tmp,now;


    freopen("A-large(3).in","r",stdin);
    freopen("a-large-out.txt","w",stdout);

    scanf("%d",&Test);

    //cout<<"HERE"<<endl;


    for(cas=1;cas<=Test;cas++)
    {

        cin>>n>>m;

        ac=0;
        ret=0;

        myvec.clear();
        while(!st.empty()) st.pop();

        for(i=0;i<m;i++)
        {
            cin>>a>>b>>c;

            ret=(ret+cost(b-a,c))%M;

            tmp.t=a;
            tmp.p=c;
            tmp.id=0;

            myvec.push_back(tmp);

            tmp.t=b;
            tmp.p=c;
            tmp.id=1;

            myvec.push_back(tmp);

        }

        sort(myvec.begin(),myvec.end(),mycomp);

         //cout<<"HERE"<<endl;

        for(i=0;i<myvec.size();i++)
        {

            now=myvec[i];

            //cout<<now.id<<" "<<now.p<<" "<<now.t<<endl;

            if(now.id==0)
            {
               // cout<<"HERE "<<st.size()<<endl;
                st.push(now);
                //cout<<"why"<<endl;
            }



            else
            {
                ll num=now.p;

                while(num>0)
                {
                    tmp=st.top();
                    st.pop();

                    if(tmp.p>=num)
                    {
                        ac=(ac+cost(now.t-tmp.t,num))%M;
                        tmp.p-=num;
                        num=0;
                    }

                    else
                    {
                        ac=(ac+cost(now.t-tmp.t,tmp.p))%M;
                        num-=tmp.p;
                        tmp.p=0;

                    }

                    if(tmp.p!=0)
                    {
                        st.push(tmp);
                    }
                }

            }
        }



        ret=ret-ac;

        if(ret>=0) ret%=M;

        while(ret<0) ret+=M;

        printf("Case #%d: ",cas);
        cout<<ret<<endl;

    }

    return 0;
}
