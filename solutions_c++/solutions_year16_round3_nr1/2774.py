//#include<iostream>
#include<fstream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;

int main()
{
    ifstream cin("/home/ankit/Desktop/input.in");
    ofstream cout("/home/ankit/Desktop/output.txt");
    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        priority_queue<pair<int,char>> v;
        int n,x,c=65;
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cin>>x;
            v.push(make_pair(x,(char)c));
            c++;
        }
        cout<<"Case #"<<i<<": ";
        while(v.top().first>1)
        {
            int p=v.top().first;
            char pc=v.top().second;
            cout<<v.top().second;
            v.pop();
            v.push(make_pair(p-1,pc));
            p=v.top().first;
            pc=v.top().second;
            cout<<v.top().second;
            v.pop();
            v.push(make_pair(p-1,pc));
            cout<<" ";
        }
        vector<pair<int,char>> r;
        while(!v.empty())
        {
            if(v.top().first!=0)
            r.push_back(make_pair(v.top().first,v.top().second));
            //cout<<v.top().first<<v.top().second;
            v.pop();
        }
        int k=0,s=r.size();
        //cout<<s;
        if(s%2!=0)
        {
            cout<<r[k].second<<" ";
            k=1;
        }
        while(k<s-1)
        {
            cout<<r[k].second<<r[k+1].second<<" ";
            k+=2;
        }
        cout<<endl;
    }
    return 0;
}

