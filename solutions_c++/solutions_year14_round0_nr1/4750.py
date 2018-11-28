#include <iostream>
#include <stdio.h>
#include <strstream>
using namespace std;
int main()
{
    //freopen("2.in","r",stdin);
    //freopen("2.out","w",stdout);
    int T;
    cin>>T;
    string Ans[T];
    for(int i=0; i<T; i++)
    {
        int a,b;
        int A[4][4],B[4][4];
        cin>>a;
        for(int j=0; j<4; j++)//inout first arrangement
        {
            for(int k=0; k<4; k++)
            {
                cin>>A[j][k];
            }
        }
        cin>>b;
        for(int j=0; j<4; j++)//inout second arrangement
        {
            for(int k=0; k<4; k++)
            {
                cin>>B[j][k];
            }
        }
        int card[4];
        int count=0;
        for(int j=0; j<4; j++)//search
        {
            for(int k=0; k<4; k++)
            {
                if(A[a-1][j] == B[b-1][k])
                {
                    card[count]=A[a-1][j];
                    count++;
                }
            }
        }
        if(count == 1)
        {
            strstream ss;
            ss << card[0];
            ss >> Ans[i];
        }
        else if (count == 0)
        {
            Ans[i]="Volunteer cheated!";
        }
        else if (count > 1)
        {
            Ans[i]="Bad magician!";
        }
    }
    for(int i=0; i<T; i++)
    {
        cout<<"Case #"<<i+1<<": "<<Ans[i]<<endl;
    }
    return 0;
}
