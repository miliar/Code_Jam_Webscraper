#include<iostream>
using namespace std;
int main()
{
    int t,temp;
    cin>>t;
    temp=t;
    while(t--)
    {
        int answer1,answer2,card1[4][4],card2[4][4],result,counter=0;
        cin>>answer1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
             cin>>card1[i][j];
            }

        }
        cin>>answer2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
              cin>>card2[i][j];
            }

        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {

                if(card1[answer1-1][i]==card2[answer2-1][j])
                {
                    result = card1[answer1-1][i];
                    counter++;
                }
            }
        }
        if(counter==1)
            cout<<"Case #"<<temp-t<<": "<<result<<endl;
        else if(counter>=1)
            cout<<"Case #"<<temp-t<<": Bad magician!"<<endl;
        else
            cout<<"Case #"<<temp-t<<": Volunteer cheated!"<<endl;
    }

}
