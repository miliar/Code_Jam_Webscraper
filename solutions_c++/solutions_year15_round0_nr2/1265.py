/// GCJ Qualification Round 2015
/// Problem B. Infinite House of Pancakes
/// -- SeiF
#include <bits/stdc++.h>

using namespace std;

queue <pair<vector <int>, int> > vis;
int x;
void printv(string n, vector<int> v)
{
    cout<<n<<": ";
    for (int i=0; i<v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int bfs()
{
    pair<vector <int>, int> cur;
    vector <int> temp;
    while(!vis.empty())
    {
        temp.clear();
        cur = vis.front();
        if(cur.first.empty())
            return cur.second;
        vis.pop();
        //printv("cur", cur.first);
        /// Eat Now
        for(int i=0;i<cur.first.size();i++)
        {
            if(cur.first[i]-1>0)
                temp.push_back(cur.first[i]-1);
        }
        sort(temp.begin(),temp.end());
        //printv("\teat", temp);
        vis.push(make_pair(temp,cur.second+1));

        /// Special Minute
        temp.clear();
        for(int i=1;i<=cur.first.back()/2;i++)
        {
            temp = cur.first;
            temp[temp.size()-1] -= i;
            temp.push_back(i);
            sort(temp.begin(), temp.end());
            vis.push(make_pair(temp, cur.second+1));
        }
        //cin>>x;
    }
    //printv("eat", temp);
}

int main()
{
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small-out_BFS_3.txt","w", stdout);
    int i,j,T,t=1;
    cin>>T;
    while(T--)
    {
        while(!vis.empty())
            vis.pop();
        vector <int> cur;
        int d,p;
        cin>>d;
        for (i=0;i<d;i++)
        {
            cin>>p;
            cur.push_back(p);
        }
        sort(cur.begin(), cur.end());
        //printv("CUR",cur);
        vis.push(make_pair(cur,0));
        printf("Case #%d: %d\n",t,bfs());
        t++;
    }
}
