#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
vector<int> row1(4);
vector<int> row2(4);
main()
{
    ios_base::sync_with_stdio(false);
    ofstream myfile("output2.txt");
    ifstream ifile("A-small-attempt0.in");
    int t;
    ifile>>t;
    for(int z=1;z<=t;++z)
    {
        int r;
        ifile>>r;
        int p;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(i==r-1)
                {
                    ifile>>row1[j];
                    continue;
                }
                ifile>>p;
            }
        }
        ifile>>r;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(i==r-1)
                {
                    ifile>>row2[j];
                    continue;
                }
                ifile>>p;
            }
        }
        int count=0;
        int ans;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(row1[i]==row2[j])
                {
                    ++count;
                    ans=row1[i];
                    break;
                }
            }
        }
        switch(count)
        {
        case 0:
            myfile<<"Case #"<<z<<": "<<"Volunteer cheated!"<<endl;
            break;
        case 1:
            myfile<<"Case #"<<z<<": "<<ans<<endl;
            break;
        default:
            myfile<<"Case #"<<z<<": "<<"Bad magician!"<<endl;
            break;
        }
    }
}
