#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int T;
    int a,b;

    vector<vector<int> > t1;
    vector<vector<int> > t2;

    cin>>T;


    for(int t=1;t<=T;++t)
    {
        t1=vector<vector<int> >(4,vector<int>(4));
        t2=vector<vector<int> >(4,vector<int>(4));
        cin>>a;
        a--;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                cin>>t1[i][j];
            }
        }
        cin>>b;
        b--;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                cin>>t2[i][j];
            }
        }

        int count=0;
        int sol=0;

        for(int i=0;i<4;++i)
        {
            if(find(t1[a].begin(),t1[a].end(),t2[b][i])!=t1[a].end())
            {
                sol=t2[b][i];
                ++count;
            }
        }

        cout<<"Case #"<<t<<": ";
        if(count==0)
        {
            cout<<"Volunteer cheated!";
        }
        else if(count==1)
        {
            cout<<sol;
        }
        else
        {
            cout<<"Bad magician!";
        }
        cout<<endl;
    }

    return 0;
}
