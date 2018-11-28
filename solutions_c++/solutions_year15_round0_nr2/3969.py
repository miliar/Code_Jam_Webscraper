#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<string>
#include<cstdlib>
#include<queue>

using namespace std;

/*
int recsplit(priority_queue<int>q)
{
    
    
    int maxv=q.top();
    if(maxv==2)
    {
        return 2;
    }
    
    if(maxv==1)
        return 1;
    
        maxv=q.top();
        q.pop();
    int time=maxv;
    
    for(int j=2;j<=min(3,maxv-1);j++)
    {
        priority_queue<int>q2=q;
        int nv=maxv/j;
        q2.push(nv);
        q2.push(maxv-nv);
        time=min(time,1+recsplit(q2));
        
    }
    
    return time;
}
*/
int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        vector<int>q;
        int d;
        cin>>d;
        int maxv=-1;
        for(int i=0;i<d;i++)
        {
            int v;
            cin>>v;
            maxv=max(maxv,v);
            q.push_back(v);
        }
        
        /*
        int maxv=q.top();
        int time=maxv;
        int splits=0;
        while(maxv>1)
        {
            maxv=q.top();
            q.pop();
            int nv=maxv/2;
            splits++;
            q.push(nv);
            q.push(maxv-nv);
            int cur_time=q.top()+splits;
            
            time=min(time,cur_time);
        }
        
        cout<<"Case #"<<i+1<<": "<<time<<endl;*/
        //int ans=recsplit(q);
        int ans=maxv;
        //i sized splits
        for(int i=1;i<=maxv;i++)
        {
            int splits=0;
            int max_rem=-1;
            for(int j=0;j<d;j++)
            {
                if(q[j]<i)
                    continue;
                
                splits+=(((q[j]))/i-1);
               
                if(q[j]%i!=0)
                {
                    splits++;
                }
                max_rem=max(max_rem,i);
            }
            ans=min(ans,splits+max_rem);
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    
}
