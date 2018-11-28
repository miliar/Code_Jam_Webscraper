#include <iostream>

using namespace std;

/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
*/
int main()
{
    int T, q1, q2;

    cin>>T;
    for(int x=1; x<=T; x++)
    {
        cin>>q1;

        int M1[4][4], M2[4][4], F=0;
        bool G=true,B=false,V=false;

        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4;j++)
            {
                cin>>M1[i][j];
            }
        }

        cin>>q2;

        for(int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin>>M2[i][j];
            }
        }

        int c=0;
        q2--; q1--;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                //cout<<"comparing "<<M1[q1][i] <<" and "<<M2[q2][j]<<endl;
                if(M1[q1][i]==M2[q2][j])
                {
                    F=M1[q1][i];
                    c++;
                }
            }
        }

        if(c==0)
        {
            G=false; B=false; V=true;
        }
        else if(c>1)
        {
            G=false; B=true; V=false;
        }
        cout<<"Case #"<<x<<": ";
        if(G)
        {
            cout<<F;
        }
        else if(B)
        {
            cout<<"Bad magician!";
        }
        else if(V)
        {
            cout<<"Volunteer cheated!";
        }
        cout<<endl;
    }
    return 0;
}

