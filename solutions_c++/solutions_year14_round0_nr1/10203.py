#include<iostream>
using namespace std;

int main()
{
    int T;
    int A[5][5],B[5][5], A_big[17],a_answer,b_answer;
    cin>>T;

    for(int i=1;i<=T;i++)
    {

        cin>>a_answer;
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                cin>>A[j][k];
                A_big[A[j][k]]=j;
            }
        }
        cin>>b_answer;
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                cin>>B[j][k];
            }
        }
        int count=0,cc=0;

            for(int j=1;j<5;j++)
            {
                if(A_big[B[b_answer][j]]==a_answer)
                {
                    count++;
                    cc=B[b_answer][j];

                }
            }


        if(count ==1)
        cout<<"Case #"<<i<<": "<<cc<<endl;

        if(count>1)
        cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;

        if(count==0)
        cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;


    }
}
