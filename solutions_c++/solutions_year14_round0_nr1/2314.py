#include<fstream>
//#include<iostream>

using namespace std;

int main()
{
    ifstream fr;
    ofstream fw;
    fr.open("A-small-attempt0.in");
    fw.open("A-small.out");
    int t,ans1,ans2,mat1[4][4],mat2[4][4],cnt,ans;
    fr>>t;
    //cin>>t;
    for(int i=1;i<=t;i++)
    {
        cnt=0;
        fr>>ans1;
        //cin>>ans1;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                fr>>mat1[j][k];

        fr>>ans2;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                fr>>mat2[j][k];

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(mat1[ans1-1][j]==mat2[ans2-1][k])
                    {cnt++;ans=mat1[ans1-1][j];}
            }
        }

        //fw<<cnt<<endl;
        if(cnt>1)
            fw<<"Case #"<<i<<": Bad magician!\n";
        else if(cnt==0)
            fw<<"Case #"<<i<<": Volunteer cheated!\n";
        else if(cnt==1)
            fw<<"Case #"<<i<<": "<<ans<<endl;


    }
    return 0;
}
