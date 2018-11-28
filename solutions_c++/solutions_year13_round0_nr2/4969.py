#include<iostream>
#include<vector>
#include<list>
#define pos pair<int, int>

using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int n,m;
        cin>>n>>m;
        int lawn[n][m];
        vector <list < pos > > sqAtLevel (101, list < pos > ());
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>lawn[i][j];
                (sqAtLevel.at(lawn[i][j])).push_back(pos(i,j));
            }
        }
        vector <bool> blackCol (n,false);
        vector <bool> blackRow (m,false);
        bool possible=true;
        for(int i=100;i>=1;i--)
        {
        	//cout<<"i-"<<i<<endl;
            for(list <pos > :: iterator it= sqAtLevel.at(i).begin(); it!=sqAtLevel.at(i).end(); it++)
            {
                pos p = *it;
                //cout<<"pos:"<<p.first<<" "<<p.second<<endl;
                if(blackCol[p.first] && blackRow[p.second])
                {
               	    //cout<<"In if"<<endl;
                    possible=false;
                    break;
                }
            }
            if(!possible)
                break;
            for(list <pos > :: iterator it= sqAtLevel.at(i).begin(); it!=sqAtLevel.at(i).end(); it++)
            {

                pos p = *it;
                //cout<<"blacked:"<<p.first<<" "<<p.second<<endl;
                blackCol[p.first]=true;
                blackRow[p.second]=true;
            }
        }
        if(possible)
            cout<<"Case #"<<t<<": YES\n";
        else
            cout<<"Case #"<<t<<": NO\n";
    }
    return 0;
}
