#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int a[4],b[4],caseNo=1,t,r1,r2,temp,i,j,match,matchNo;
    ifstream input;
    ofstream output;
    output.open("output.txt");
    input.open("input.txt");
    input>>t;
    //cout<<t;
    while(caseNo<=t)
    {
        //input>>
        matchNo=0;
        input>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(i==(r1-1))
                    input>>a[j];
                else
                    input>>temp;
        input>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(i==(r2-1))
                    input>>b[j];
                else
                    input>>temp;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i]==b[j])
                {
                    match=a[i];
                    matchNo++;
                    continue;
                }
            }
        }
                if(matchNo==0)
                {
                    output<<"Case #"<<caseNo<<": "<<"Volunteer cheated!"<<endl;
                }
                if (matchNo==1)
                {
                    output<<"Case #"<<caseNo<<": "<<match<<endl;
                }
                if(matchNo>1)
                {
                    output<<"Case #"<<caseNo<<": "<<"Bad magician!"<<endl;
                }

        cout<<caseNo;
        caseNo++;
    }
    input.close();
}
