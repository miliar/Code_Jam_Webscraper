#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t,ans1,ans2,ar1[4][4],ar2[4][4],count=0,el;
    ifstream input("input.txt");
    ofstream output("output.txt",ios::trunc);
    input>>t;
    for(int x=1;x<=t;x++){
    input>>ans1;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            input>>ar1[i][j];
    }
    input>>ans2;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            input>>ar2[i][j];
    }
    for(int i =0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(ar1[ans1-1][i]==ar2[ans2-1][j]){

                count++;
                el=ar1[ans1-1][i];
            }
        }
    }
    output<<"Case #"<<x<<": ";
    if(count==1)
        output<<el<<endl;
    if(count==0)
        output<<"Volunteer cheated!"<<endl;
    if(count>1)
        output<<"Bad magician!"<<endl;
    count=0;

}
return 0;}

