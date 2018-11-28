#include <iostream>

using namespace std;
#define SZ 4
int a[SZ][SZ];
int b[SZ][SZ];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;int testcaseno=1;
    while(t--)
    {
        int row1;cin>>row1;row1-=1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;++j){cin>>a[i][j];}
        }
        int row2;cin>>row2;row2-=1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;++j)cin>>b[i][j];
        }
        int matches=0;int matched_card;//count of number of matches
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(a[row1][i]==b[row2][j]){matched_card=a[row1][i];matches++;break;}
            }
        }
        if(matches==1)
        {
            cout<<"Case #"<<testcaseno<<": "<<matched_card<<endl;
        }
        else if(matches==0)//no match; volunteer cheated
        {
            cout<<"Case #"<<testcaseno<<": "<<"Volunteer cheated!"<<endl;
        }
        else//multiple matches; bad magician
        {
            cout<<"Case #"<<testcaseno<<": "<<"Bad magician!"<<endl;
        }
        testcaseno++;
    }
    return 0;
}
