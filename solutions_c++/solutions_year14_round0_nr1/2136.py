#include<bits/stdc++.h>
using namespace std;
vector<int> canbe,yes;
int main()
{
    int t,i,j,k,l,m,n;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>j;
        canbe.clear();
        yes.clear();
        for(k=0;k<4;k++)
        {
            for(l=0;l<4;l++)
            {
                cin>>m;
                if((k+1)==j)
                canbe.push_back(m);
            }
        }
        cin>>j;
        yes.clear();
        for(k=0;k<4;k++)
        {
            for(l=0;l<4;l++)
            {
                cin>>m;
                if((k+1)==j)
                {
                    for(n=0;n<canbe.size();n++)
                    {
                        if(m==canbe[n])
                        {
                            yes.push_back(m);
                            break;
                        }
                    }
                }
            }
        }
        if(yes.size()>1)
        cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        else if(yes.size()==0)
        cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        else
        cout<<"Case #"<<i+1<<": "<<yes[0]<<endl;
    }
    return 0;
}
