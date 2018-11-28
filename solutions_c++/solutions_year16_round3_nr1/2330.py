#include<bits/stdc++.h>
using namespace std;
#define ll long long
map<ll,bool> done;
priority_queue<pair<ll,char> > pq;
ll n,i,p[100],x,y,d,t;
pair<ll,char> a,b;
char cx,cy;
int main()
{
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	ll z=0LL;
	while(t--)
    {
        z++;
        done.clear();
        char ch='A';
        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>p[i];
            done[p[i]]=true;
            pq.push(make_pair(p[i],ch));
            ch++;
        }
        cout<<"Case #"<<z<<": ";
        while(!pq.empty())
        {
            a=pq.top();
            pq.pop();
            b=pq.top();
            pq.pop();
            
            x=a.first;
            cx=a.second;
            y=b.first;
            cy=b.second;
            
            if(y>x)
            {
                while(y>x+1)
                {
                    cout<<cy<<cy<<" ";
                    y-=2;
                }
                if(y==x+1)
                {
                    cout<<cy<<" ";
                    y-=1;
                }
            }
            else
            {
                while(x>y+1)
                {
                    cout<<cx<<cx<<" ";
                    x-=2;
                }
                if(x==y+1)
                {
                    cout<<cx<<" ";
                    x-=1;
                }
            }
            
            if(pq.empty())
            {
                while(min(x,y)>0)
                {
                    cout<<cx<<cy<<" ";
                    x--;
                    y--;
                }
                break;
            }
            d=pq.top().first;
            
            while(min(x,y)>d)
            {
                cout<<cx<<cy<<" ";
                x--;
                y--;
            }
            
            if(x>y)
            {
                if(y>0)
                    pq.push(make_pair(y,cy));
                while(x>0)
                {
                    if(x==1)
                    {
                        cout<<cx<<" ";
                        x=0;
                        break;
                    }
                    cout<<cx<<cx<<" ";
                    x-=2;
                    if(done[x]==true)
                        break;
                }
                if(x>0)
                    pq.push(make_pair(x,cx));
            }
            else
            {
                if(x>0)
                    pq.push(make_pair(x,cx));
                while(y>0)
                {
                    if(y==1)
                    {
                        cout<<cy<<" ";
                        y=0;
                        break;
                    }
                    cout<<cy<<cy<<" ";
                    y-=2;
                    if(done[y]==true)
                        break;
                }
                if(y>0)
                    pq.push(make_pair(y,cy));
            }
        }
        cout<<"\n";
    }
    return 0;
}