// Coder nyble
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1; z<=t; z++)
    {
        int d,tmp;
        scanf("%d",&d);
        map<int,int> diner,diner1;

        for(int i=0; i<d; i++)
        {
            scanf("%d",&tmp);
            if(diner.count(tmp)>0)
            {
                diner[tmp]++;
            }
            else
            {
                diner[tmp]=1;
            }
        }
        diner1 = diner;
        auto it1 = diner.rbegin();

        int totalMinutes=0, spMinutes=0,minMinutes=it1->first;
        bool even = true;

        if(it1->first==9&&it1->second==1)
        {
            spMinutes+=2;
            if(diner.count(3)>0)
            {
                diner[3]+=3;
            }
            else
            {
                diner[3]=3;
            }
            diner.erase(it1->first);
            it1 = diner.rbegin();
        }

        tmp = it1->first/2;

        while(tmp >= it1->second)
        {
            if(it1->first%2 == 0)
            {
                even = true;
            }
            else
            {
                even = false;
            }

            if(even)
            {
                if(diner.count(tmp)>0)
                {
                    diner[tmp]+=2*it1->second;
                }
                else
                {
                    diner[tmp]=2*it1->second;
                }
            }
            else
            {
                if(diner.count(tmp)>0)
                {
                    diner[tmp]+=it1->second;
                }
                else
                {
                    diner[tmp]=it1->second;
                }
                if(diner.count(tmp+1)>0)
                {
                    diner[tmp+1]+=it1->second;
                }
                else
                {
                    diner[tmp+1]=it1->second;
                }
            }
            spMinutes+=it1->second;
            diner.erase(it1->first);
            it1 = diner.rbegin();
            if(minMinutes>(it1->first+spMinutes))
                minMinutes = it1->first+spMinutes;
            tmp = it1->first/2;
        }

        totalMinutes = spMinutes + (diner.rbegin())->first;

        if(totalMinutes<minMinutes)
            minMinutes = totalMinutes;

        ///////////////////

        it1 = diner1.rbegin();
        totalMinutes=0, spMinutes=0;
        if(minMinutes>(it1->first))
                minMinutes = it1->first;
        even = true;

        tmp = it1->first/2;

        while(tmp >= it1->second)
        {
            if(it1->first%2 == 0)
            {
                even = true;
            }
            else
            {
                even = false;
            }

            if(even)
            {
                if(diner1.count(tmp)>0)
                {
                    diner1[tmp]+=2*it1->second;
                }
                else
                {
                    diner1[tmp]=2*it1->second;
                }
            }
            else
            {
                if(diner1.count(tmp)>0)
                {
                    diner1[tmp]+=it1->second;
                }
                else
                {
                    diner1[tmp]=it1->second;
                }
                if(diner1.count(tmp+1)>0)
                {
                    diner1[tmp+1]+=it1->second;
                }
                else
                {
                    diner1[tmp+1]=it1->second;
                }
            }
            spMinutes+=it1->second;
            diner1.erase(it1->first);
            it1 = diner1.rbegin();
            if(minMinutes>(it1->first+spMinutes))
                minMinutes = it1->first+spMinutes;
            tmp = it1->first/2;
        }

        totalMinutes = spMinutes + (diner1.rbegin())->first;

        if(totalMinutes<minMinutes)
            minMinutes = totalMinutes;


        if(1)
        {
            printf("Case #%d: %d\n",z,minMinutes);
        }
    }
    return 0;
}
