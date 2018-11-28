#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

void check(vector<int> &vec1, vector<int> &vec2)
{
    int count = 0;
    int e;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(vec1[i]==vec2[j])
            {
                e = vec1[i];
                count ++;
            }
        }
    }
    if(count==0)
        cout<<"Volunteer cheated!"<<endl;
    else
    {
        if(count==1)
            cout<<e<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    vector<vector<int> > board;
    for(int t=1;t<=T;t++)
    {
        board.clear();
        cout<<"Case #"<<t<<": ";
        int row1;
        cin>>row1;
        vector<int> vec1;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                int e;
                cin>>e;
                if(i==row1-1)
                    vec1.push_back(e);
            }
        }
        int row2;
        cin>>row2;
        vector<int> vec2;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                int e;
                cin>>e;
                if(i==row2-1)
                    vec2.push_back(e);
            }
        }

        check(vec1,vec2);
    }
    return 0;
}
