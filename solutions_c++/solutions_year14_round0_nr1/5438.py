#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    int t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    cin >> t;
    int X=1;
    while(X<=t)
    {
        int row1, row2;
        int arr[4][4], arr2[4][4];
        cin >> row1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>arr[i][j];

        cin >> row2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>arr2[i][j];


        int flag1=-1, flagAgain=-1; int temp;

        for(int i=row1-1,k=row2-1,m=0;m<4;m++)
            for(int j=0;j<4;j++)
        {
            //cout << "Arr " << arr[i][m] << " i " << i << " m " << m<< endl << endl;;
            //cout << "Arr2 " << arr2[k][j] << " k " << k << " j " << j << endl << endl;

            if(arr[i][m] == arr2[k][j])
            {
                if(flag1==1)
                    flagAgain=1;

                flag1=1;
                temp=arr[i][m];
            }
        }

        if(flagAgain==1)
        {
            cout << "Case #"<< X << ": Bad magician!\n";
        }
        if(flag1==1 && flagAgain==-1)
        {
            cout << "Case #"<< X << ": " << temp << endl;
        }
        if(flag1==-1)
        {
            cout << "Case #"<< X << ": Volunteer cheated!\n";
        }

            X=X+1;
    }
}