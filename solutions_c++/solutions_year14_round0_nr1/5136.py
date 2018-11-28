#include<iostream>


using namespace std;

int main()
{
    int T;
    cin>>T;
    int A[4][4];
    int B[4][4];
    int k;
    int a,b;
    int t=0;
    while(T--)
    {
        t++;
        int flag=0;
        cin>>a;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>A[i][j];

          cin>>b;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>B[i][j];

        for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
        {
             //cout<<A[a][i]<<endl;
               //cout<<B[b][j]<<endl;
            if(A[a-1][i]==B[b-1][j])
           {

                k=B[b-1][j];
                flag++;
                //cout<<flag<<endl;
           }

        }
        if(flag==0)
            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        else if(flag==1)
            cout<<"Case #"<<t<<": "<<k<<endl;
        else
            cout<<"Case #"<<t<<": Bad magician!"<<endl;



    }
}
