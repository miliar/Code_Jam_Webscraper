#include <iostream>

using namespace std;

int main()
{
    int arrangement1[4][4];
    int arrangement2[4][4];
    int test;
    int answer1;
    int answer2;
    int actualAnswer;
    int numberOfMatches;
    cin>>test;
    for(int testNumber=1;testNumber<=test;testNumber++)
    {
        numberOfMatches=0;
        cin>>answer1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>arrangement1[i][j];
        cin>>answer2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>arrangement2[i][j];



        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                if(arrangement1[answer1-1][j]==arrangement2[answer2-1][k])
            {
                //cout<<"j="<<j<<" K ="<<k;
                numberOfMatches++;
                actualAnswer=arrangement1[answer1-1][j];
            }
        }
        if(numberOfMatches==1)
        {
            cout<<"Case #"<<testNumber<<": "<<actualAnswer<<endl;
        }
        else
            if(numberOfMatches>1)
        {
            cout<<"Case #"<<testNumber<<": Bad magician!"<<endl;
        }
        else if(numberOfMatches==0)
        {
            cout<<"Case #"<<testNumber<<": Volunteer cheated!"<<endl;
        }


    }
    return 0;

}
