#include <queue>
#include <map>
#include <iostream>
#include <string>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
//    freopen("in.txt","r",stdin);
    int N,n,temp;
    string modify;
    int cnt=0;
    while(cin>>N&&N)
    {
        cout<<"Scenario #"<<++cnt<<endl;
        queue<int> q[1010];
        queue<int>Q;
        bool visit[1010]={false};

        map<int,int>mapQ;
        for(int i=0;i<N;++i)
        {
            cin>>n;
            while(n--)
            {
                cin>>temp;
                mapQ[temp]=i;
            }
        }
        int ask;
        while(cin>>modify&&modify[0]!='S')
        {
            if(modify[0]=='E')
            {
                cin>>temp;
                ask=mapQ[temp];
                q[ask].push(temp);
                if(!visit[ask])
                {
                    Q.push(ask);
                    visit[ask]=true;
                }
            }
            else
            {
                cout<<q[Q.front()].front()<<endl;
                q[Q.front()].pop();
                if(q[Q.front()].empty())
                {
                    visit[Q.front()]=false;
                    Q.pop();
                }
            }
        }
        cout<<endl;
    }

    return 0;
}