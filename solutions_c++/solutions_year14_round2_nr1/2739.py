#include<bits/stdc++.h>
using namespace std;
#define SZ 110
#define pf printf
string arr[SZ];
int tbl[SZ][SZ];
int info[SZ][SZ];
int lim;
string make_def(string str,int ind)
{
    int inx = 0;
    string ans = "";
    ans.push_back(str[0]);
    int cunt = 0;
    for(int i=1,p = 0; i<str.size(); i++,p++)
    {
        if(str[p]!=str[i])
        {
            ans.push_back(str[i]);
            info[ind][inx++] = cunt;
            lim = inx;
            cunt = 1;
        }
        else
        {
            cunt++;
        }
    }
    info[ind][inx] = cunt;
    return ans;
}



int main()
{
    freopen("in.in","r",stdin);
    freopen("out_2.txt","w",stdout);
    int T,N;
    string def,pre;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        memset(info,0,sizeof(info));
        for(int i=0; i<SZ; i++)arr[i].clear();
        def.clear();
        pre.clear();
        bool flag = false;
        cin>>N;
        for(int i=0; i<N; i++)
        {
            cin>>arr[i];
            def = make_def(arr[i],i);
            if(i==0)pre = def;
            else if(pre!=def)
            {
                pf("Case #%d: Fegla Won\n",t);
                flag = true;
                break;
            }
            if(flag)break;
        }
        if(flag)continue;
        int sum = 0;
        for(int i=0; i<=lim; i++)
        {
            sum+=abs(info[0][i]-info[1][i]);
        }
        pf("Case #%d: %d\n",t,sum);
    }
    return 0;
}

