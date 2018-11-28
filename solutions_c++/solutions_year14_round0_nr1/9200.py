#include<iostream>
#include<vector>
#include<fstream>
#include<set>
using namespace std;
int main()
{
    ifstream filein;
    ofstream fileout;
    filein.open("A-small-attempt2.in");
    fileout.open("A-small-attempt2.out");
    int t;
    filein>>t;
    for(int tc=1;tc<=t;tc++)
    {
            int a1;
            filein>>a1;
            int mat1[4][4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            filein>>mat1[i][j];
                    }
            }
            a1--;
            int a2;
            filein>>a2;
            a2--;
            int mat2[4][4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            filein>>mat2[i][j];
                    }
            }
            int common=0;
            set<int> myset;
            for(int i=0;i<4;i++)
            {
                    myset.insert(mat1[a1][i]);
                    myset.insert(mat2[a2][i]);
            }
            int x=myset.size();
            common=8-x;
            if(common==1)
            {
                 int flag=0;
                 for(int i=0;i<4;i++)
                 {
                         for(int j=0;j<4;j++)
                         {
                                 if(mat1[a1][i]==mat2[a2][j])              
                                 {
                                      fileout<<"Case #"<<tc<<": "<<mat1[a1][i]<<"\n";
                                      flag=1;
                                      break;
                                 }
                         }
                         if(flag==1)  break;
                 }
            }
            else if(common>1)      fileout<<"Case #"<<tc<<": "<<"Bad magician!"<<"\n";  
            else if(common==0)     fileout<<"Case #"<<tc<<": "<<"Volunteer cheated!"<<"\n";
    }
    filein.close();
    fileout.close();
    return 0;
}
