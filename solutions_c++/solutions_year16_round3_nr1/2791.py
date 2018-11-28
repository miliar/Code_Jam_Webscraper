//Md. Ahsan Kabir Shohagh
#include<bits/stdc++.h>
using namespace std;
#define sz 100000
#define pb(a) push_back(a)
#define ll long long
#define ull unsigned long long
#define fread freopen("input.txt","r",stdin)
#define fwrite freopen("output.txt","w",stdout)
#define inf (1<<29)
#define mem(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
#define quick ios_base::sync_with_stdio(0)
struct amar
{
    int first;
    char second;
    amar() {}
    amar(int _,char __)
    {
        first=_;
        second=__;
    }
    bool operator<(const amar & x)const
    {
        return first<x.first;
    }
};
int main()
{
    fread;
    fwrite;
    int t,n,p;
    priority_queue< amar >pq;
    vector<amar>tmp;
    cin>>t;
    for(int ca=1; ca<=t; ca++)
    {
        while(!pq.empty()) pq.pop();
        tmp.clear();

        cin>>n;
        for(int i=0; i<n; i++)
        {
            cin>>p;
            pq.push(amar(p,(char)(i+'A')));
        }
        printf("Case #%d:",ca);
        while(!pq.empty())
        {
            tmp.clear();
            while(!pq.empty())
            {
                tmp.pb(pq.top());
                pq.pop();
            }
            for(int i=0; i<tmp.size(); i++)
            {
                pq.push(tmp[i]);
            }

            int tot=0,mx=0;
            //top 2ta niye
            if(tmp[0].first>1)
            {
                tot+=tmp[0].first-2;
                mx=tmp[0].first-2;
                for(int i=1; i<tmp.size(); i++)
                {
                    tot+=tmp[i].first;
                    mx=max(mx,tmp[i].first);
                }
                double majority=(mx*100.0/tot);

                if(majority<=50.0)
                {
                    printf(" %c%c",pq.top().second,pq.top().second);
                    amar now = pq.top();
                    pq.pop();
                    now.first-=2;
                    if(now.first>0)
                    {
                        pq.push(now);
                    }
                    continue;
                }
            }

            //top 1ta + 2nd top 1ta
            tot=0,mx=tmp[0].first-1;
            tot+=tmp[0].first-1;
            tot+=tmp[1].first-1;
            mx=max(mx,tmp[1].first-1);
            for(int i=2; i<tmp.size(); i++)
            {
                tot+=tmp[i].first;
                mx=max(mx,tmp[i].first);
            }
            if(tot==0) tot=1;
            double majority=(mx*100.0/tot);

            if(majority<=50.0)
            {
                printf(" %c",pq.top().second);
                amar now = pq.top();
                pq.pop();
                printf("%c",pq.top().second);
                amar now2 = pq.top();
                pq.pop();
                if(now.first-1>0)
                {
                    now.first--;
                    pq.push(now);
                }
                if(now2.first-1>0)
                {
                    now2.first--;
                    pq.push(now2);
                }
                continue;
            }
            //top 1ta
            printf(" %c",pq.top().second);
            amar now = pq.top();
            pq.pop();
            now.first-=1;
            if(now.first>0)
            {
                pq.push(now);
            }
        }
        puts("");
    }
    return 0;
}
/*
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
*/
