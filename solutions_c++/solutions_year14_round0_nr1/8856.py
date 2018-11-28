#include<iostream>

using namespace std;

int main()
{
    int t, i, j, k, posmat[4][4], row[4], count = 0, r1, r2, n;

    cin>>t;

    for ( i = 0 ; i < t ; ++i )
    {
        cin>>r1;
        for ( j = 0 ; j < 4; ++j )
            for ( k = 0 ; k <4 ; ++k )
                cin>>posmat[j][k];
        for ( j = 0 ; j < 4 ; ++j )
            row[j] = posmat[r1-1][j];
        cin>>r2;
        for ( j = 0 ; j < 4; ++j )
            for ( k = 0 ; k <4 ; ++k )
                cin>>posmat[j][k];
        for ( j = 0 ; j < 4 ; ++j )
            for ( k = 0 ; k < 4 ; ++k )
            if ( row[j] == posmat[r2-1][k] )
            {
                count++;
                n=row[j];
            }

        if ( count == 0 )
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        else if ( count == 1 )
            cout<<"Case #"<<i+1<<": "<<n<<endl;
        else
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        count = 0;
    }
}
