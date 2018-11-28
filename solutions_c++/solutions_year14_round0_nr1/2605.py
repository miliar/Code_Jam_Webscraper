#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream file;
    ofstream output;
    file.open("A-small-attempt0.in");
    output.open("answer.txt");

    int n=0;

    file>>n;

    int arr[2][4][4];

    for(int i=1;i<=n;i++)
    {
        int ans[2];
        int values[16]={0};

        for(int j=0;j<2;j++)
        {
            file>>ans[j];

            for(int i=0;i<4;i++)
                for(int k=0;k<4;k++)
                {
                    file>>arr[j][i][k];

                    if(j==0&&ans[0]==i+1)values[arr[j][i][k]-1]++;
                    if(j==1&&ans[1]==i+1)values[arr[j][i][k]-1]++;
                }
        }

        int result=0;
        int answer=-1;

        for(int i=0;i<16;i++)
            if(values[i]==2)
            {
                result++;
                answer=i+1;
            }

        if(result==1)
        {
            //cout<<"Case #"<<i<<": "<<answer<<endl;
            output<<"Case #"<<i<<": "<<answer<<endl;
        }
        if(result==0)
        {
            //cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
            output<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }
        if(result>1)
        {
            //cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
            output<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        }

    }


}
