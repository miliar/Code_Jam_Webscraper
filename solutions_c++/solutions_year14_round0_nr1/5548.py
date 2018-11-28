#include<iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int count=1;
    while(t--)
    {
        cout<<"Case #"<<count<<": ";
        count++;
        int num1;
        cin>>num1;
        int mat1[6][6];
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>mat1[i][j];
            }
        }

        int num2;
        cin>>num2;
        int mat2[6][6];
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>mat2[i][j];
            }
        }
        int index1[20]={0};
        int index2[20]={0};
        int i=num1-1;
        for(int j=0; j<4; j++)
        {
            index1[mat1[i][j]]++;
        }
        i=num2-1;
        for(int j=0; j<4; j++)
        {
            index2[mat2[i][j]]++;
        }
        int temp=0;
        for(int i=1; i<=16; i++)
        {
            if(index1[i]==1 && index2[i]==1)
            temp++;
        }
        if(temp==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else if(temp>1)
        {
            cout<<"Bad magician!"<<endl;
        }
        else
        {
            for(int i=1; i<=16; i++)
            {
                if(index1[i]==1 && index2[i]==1)
                {
                    cout<<i<<endl;
                    break;
                }
            }
        }



    }
}
