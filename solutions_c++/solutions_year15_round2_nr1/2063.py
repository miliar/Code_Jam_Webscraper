#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
using namespace std;
int rev(int n)
{
    int temp=0;
    while(n)
    {
        temp=temp*10+n%10;
        n/=10;
    }
    return temp;
}
class node
{
public:
    bool visited;
    int distance;
    vector<node*> links;
    node():visited{false},distance(1),links{}{}
};

class graph
{
    public:
    vector<node> nodes;
    void addedge(int i, int j)
    {
        nodes[i].links.push_back(&nodes[j]);
    }
    graph(int n):nodes(n){}

};
void bfs(node* root)
{
    queue<node*> q{};
    q.push(root);
    root->visited=true;
    while(!q.empty())
    {
        auto t=q.front();
        q.pop();
        for(auto i=t->links.begin();i!=t->links.end();++i)
        {
            if(!(*i)->visited)
            {
                (*i)->distance=t->distance+1;
                (*i)->visited=true;
            q.push(*i);
            }
        }
    }
}
int main()
{
    graph rlt(10000000);
    for(int i=0;i<=9999998;++i)
    {
        rlt.addedge(i,i+1);
        if((i+1)!=rev(i+1))
        {
            int temp=rev(i+1)-1;
            rlt.addedge(i,temp);
            //rlt.addedge(temp,i);
        }
    }
    bfs(&rlt.nodes[0]);
    int N,t;
    fstream in("small.in",ios::in);
    fstream out("out.out",ios::out);
    in>>N;
    for(int i=0;i<N;++i)
    {
        in>>t;
        out<<"Case #"<<i+1<<": "<<rlt.nodes[t-1].distance<<endl;
    }


}

