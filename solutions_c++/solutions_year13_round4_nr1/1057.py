//#include<iostream>
#include<fstream>
#include <algorithm>
using namespace std;
ifstream cin ("temp.in");
ofstream cout ("temp.out");
struct node 
{
       int w;
       int p;
};
bool operator < (const struct node &a,const struct node &b)
       {
         if (a.w<b.w) return 1;
         else return 0;
       }
int main ()
{
    int t;
    cin>>t;
    int i;
    for (i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        int n,m;
        cin>>n>>m;
        long long int total=0;
        int j;
        struct node in[1000];
        struct node out[1000];
        for (j=0;j<m;j++)
        {
            cin>>in[j].w>>out[j].w>>in[j].p;
            out[j].p=in[j].p;
            total=total+(n+n-out[j].w+in[j].w+1)*(out[j].w-in[j].w)/2*in[j].p;
            total%=1000002013;
        }
        sort (in,in+m);
        sort (out,out+m);
        int p=0,q=0;
        struct node stack[1000];
        int z=0;
        long long int now=0;
        while (p<m||q<m)
        {
             // for (j=0;j<z;j++) cout<<stack[j].w<<" "<<stack[j].p<<endl;
              //cout<<"*******"<<endl;
              if (p<m&&in[p].w<=out[q].w)
              {
                 stack[z].w=in[p].w;
                 stack[z].p=in[p].p;
                 z++;
                 p++;
              }
              else
              {
                  while (out[q].p>0)
                  {
                        //cout<<"%%%"<<out[q].p<<endl;
                        if (stack[z-1].p>out[q].p)
                        {
                            now=now+(n+n-out[q].w+stack[z-1].w+1)*(out[q].w-stack[z-1].w)/2*out[q].p;
                            now%=1000002013;
                            stack[z-1].p-=out[q].p;
                            out[q].p=0;
                        }
                        else
                        {
                            now=now+(n+n-out[q].w+stack[z-1].w+1)*(out[q].w-stack[z-1].w)/2*stack[z-1].p;
                            now%=1000002013;
                            out[q].p-=stack[z-1].p;
                            z--;
                        }
                  }
                  q++;
              }
        }
        //cout<<total<<" "<<now<<endl;
        long long int ans;
        if (total<now) ans=total+1000002013-now;
        else ans=total-now;
        cout<<ans<<endl;
    }        
    return 0;
}
