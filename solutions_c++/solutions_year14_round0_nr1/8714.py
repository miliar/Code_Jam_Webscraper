#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int main()
{
    fstream myfile("A-small-attempt0.in");
    fstream out("out.txt");

    if(myfile.is_open())
    {
        int t;
        myfile>>t;

        for(int test=1;test<=t;test++)
        {
            int r1,r2;
            myfile>>r1;

            int matF[4][4],matS[4][4];

            vector<bool> row1,row2; row1.resize(17); row2.resize(17);
            for(int i=0;i<17;i++) row1[i]=row2[i]=false;

            for(int i=0;i<4;i++)for(int j=0;j<4;j++) myfile>>matF[i][j];
            myfile>>r2;

            for(int i=0;i<4;i++) row1[matF[r1-1][i]]=true;

            for(int i=0;i<4;i++)for(int j=0;j<4;j++) myfile>>matS[i][j];

            for(int i=0;i<4;i++) row2[matS[r2-1][i]]=true;

            int cnt=0,ans;
            for(int i=1;i<17;i++)
            {
                if(row1[i]&& row2[i]) {cnt++; ans=i;}
            }
            if(cnt==1)
            out<<"Case #"<<test<<": "<<ans<<"\n";
            else if(cnt==0)
            out<<"Case #"<<test<<": Volunteer cheated!\n";
            else if(cnt>1)
            out<<"Case #"<<test<<": Bad magician!\n";

        }
    }
    myfile.close(); out.close();


    return 0;
}
