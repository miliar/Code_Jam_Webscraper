#include "iostream"
#include "cstdio"
#include "set"

using namespace std;

int t,n,tmp,ans,out=0;
set<int> s;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int  cas=1; cas<=t; cas++)
    {
        s.clear();
        ans=0;
        cin>>n;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>tmp;
                if(i==n)
                    s.insert(tmp);
            }
        }
        cin>>n;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>tmp;
                if(i==n&&s.find(tmp)!=s.end())
                {
                    ans++;
                    out=tmp;
                }
            }
        }
        if(ans==0)
            cout<<"Case #"<<cas<<": Volunteer cheated!"<<endl;
        else if(ans==1)
            cout<<"Case #"<<cas<<": "<<out<<endl;
        else
            cout<<"Case #"<<cas<<": Bad magician!"<<endl;
    }
    return 0;
}
