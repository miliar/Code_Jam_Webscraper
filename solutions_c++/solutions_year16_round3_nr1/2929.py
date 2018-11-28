#include <bits/stdc++.h>

#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     SIZE      1000001
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;

const int mod=1000000007;

struct node{
    char ch;
    int v;
    bool operator < (const node & obj) const
    {
        if(v<=obj.v)
            return true;
        return false;
    }
};
int main()
{
    int T;
    //FILE *fp=fopen("A_smallOutput.txt","w");
    cin>>T;
    for(int t=1;t<=T;++t)
    {
     int ans;
     priority_queue<node> pp;
     int N;
     cin>>N;
     int total=0;
     node arr[N+7];
     for(int i=0;i<N;++i)
     {
         cin>>arr[i].v;
         total+=arr[i].v;
         arr[i].ch=(char)65+i;
        pp.push(arr[i]);
     }
     cout<<"Case #"<<t<<": ";

    while(!pp.empty())
    {
        node tmp=pp.top();
        pp.pop();
        node tmp2=pp.top();
        pp.pop();
        if(tmp.v>=2)
        {

            //after two from top
            double d1=((tmp.v-2)/(double)(total-2));
            double d2=((tmp.v-1)/(double)(total-2));
            double d3=((tmp2.v-1)/(double)(total-2));
            double d4=((tmp2.v)/(double)(total-2));
            //cout<<tmp.v<<" "<<tmp.ch<<" "<<tmp2.v<<" "<<tmp2.ch<<endl;
            if(d1<=0.5&&d4<=0.5)
            {
                cout<<tmp.ch<<tmp.ch<<" ";
                tmp.v-=2;
                if(tmp.v>0)
                    pp.push(tmp);
                pp.push(tmp2);
                total-=2;
            }
            else if(d2<=0.5&&d3<=0.5)
            {
                cout<<tmp.ch<<tmp2.ch<<" ";
                tmp.v-=1;
                tmp2.v-=1;
                if(tmp.v>0)
                pp.push(tmp);
                if(tmp.v>0)
                pp.push(tmp2);
                total-=2;
                }
            else
            {
                cout<<tmp.v<<" ";
                tmp.v-=1;
                if(tmp.v>0)
                    pp.push(tmp);
                pp.push(tmp2);
                total-=1;
            }
        }
        else
        {

            if(pp.size()%2==0)
            {
                cout<<tmp.ch<<tmp2.ch<<" ";
                while(!pp.empty())
                {
                    node tt=pp.top();
                    pp.pop();

                    node tt2=pp.top();
                    pp.pop();
                    cout<<tt.ch<<tt2.ch<<" ";
                }
            }
            else
            {
                cout<<tmp.ch<<" ";
                node tt3=pp.top();
                pp.pop();
                cout<<tmp2.ch<<tt3.ch<<" ";
                while(!pp.empty())
                {
                    node tt=pp.top();
                    pp.pop();

                    node tt2=pp.top();
                    pp.pop();
                    cout<<tt.ch<<tt2.ch<<" ";
                }
            }
        }
    }
    cout<<endl;
    //fprintf(fp,"Case #%d: %d\n",t,ans);
    }
 //   fclose(fp);
    return 0;
}
