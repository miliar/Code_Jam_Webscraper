#include <iostream>

using namespace std;

int main()
{
    short T;
    cin>>T;
    for(short i=0; i<T; i++)
    {
        short X, Y;
        cin>>X;
        short A[4][4];
        short B[4][4];
        for(short j=0; j<4; j++)
        {
            for(short k=0; k<4; k++)
            {
                cin>>A[j][k];
            }
        }
        cin>>Y;
        for(short j=0; j<4; j++)
        {
            for(short k=0; k<4; k++)
            {
                cin>>B[j][k];
            }
        }
        short z=0;
        short w;
        for(short j=0; j<4; j++)
        {
            for(short k=0; k<4; k++)
            {
                if(A[X-1][j]==B[Y-1][k])
                {
                    z++;
                    w=A[X-1][j];
                }
            }
        }
        if(z==1)cout<<"Case #"<<i+1<<": "<<w<<endl;
        else if(z>1)cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        else if(z==0)cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    }
    return 0;
}
