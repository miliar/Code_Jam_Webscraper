#include <iostream>
#include<vector>
#include <fstream>
#include <algorithm>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;
int main()
{
    READ("A-small-attempt3.in");
    WRITE("A-small-attempt3.out");
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        int r1;
        cin>>r1;
        vector<int> row1;
        for(int j=1; j<=4; j++)
        {
            int te;
            if(j!=r1)
            {
                cin>>te;
                cin>>te;
                cin>>te;
                cin>>te;
            }
            else
            {
                cin>>te;
                row1.push_back(te);
                cin>>te;
                row1.push_back(te);
                cin>>te;
                row1.push_back(te);
                cin>>te;
                row1.push_back(te);
            }
        }
        int r2;
        cin>>r2;
        vector<int> row2;
        for(int j=1; j<=4; j++)
        {
            int te;
            if(j!=r2)
            {
                cin>>te;
                cin>>te;
                cin>>te;
                cin>>te;
            }
            else
            {
                cin>>te;
                row2.push_back(te);
                cin>>te;
                row2.push_back(te);
                cin>>te;
                row2.push_back(te);
                cin>>te;
                row2.push_back(te);
            }
        }
        int flg=0;
        int in=-1;
        for(int j=0; j<4; j++)
        {
            if(find (row1.begin(), row1.end(), row2[j])!=row1.end()&&flg==0)
            {
                flg=1;
                in=j;
            }
            else if(find (row1.begin(), row1.end(), row2[j])!=row1.end()&&flg==1)
            {
                cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
                flg=2;
                break;
            }
        }
        if(flg==1)
            cout<<"Case #"<<i+1<<": "<<row2[in]<<endl;
        if(flg==0)
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
