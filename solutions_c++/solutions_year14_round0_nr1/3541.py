#include <iostream>
#include <set>
using namespace std;

int T, a1, a2;
int c[4][4];

void readCards()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>c[i][j];
}


int main()
{
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>a1;
        readCards();
        set<int> p;
        for(int j=0;j<4;j++)
            p.insert(c[a1-1][j]);
        cin>>a2;
        readCards();
        int count = 0;
        int ans = 0;
        for(int j=0;j<4;j++)
            if(p.count(c[a2-1][j]))  { count++; ans = c[a2-1][j]; }
        cout<<"Case #"<<t<<": ";
        
        switch(count)
        {
            case 0:
                cout<<"Volunteer cheated!"<<endl;
                break;
            case 1:
                cout<<ans<<endl;
                break;
            default:
                cout<<"Bad magician!"<<endl;
                break;
        }
    }
}