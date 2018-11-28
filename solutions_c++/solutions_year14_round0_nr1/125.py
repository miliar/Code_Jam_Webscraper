#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int T ;
    cin>>T ;
    int cnt = 1;
    while(T--)
    {
        int arr[4][4] , arr1[4][4] , temp1[16] ;
        int r1 , r2 ,  comp = 0 ;
        cin>>r1 ;
        for(int i = 0 ; i < 4 ; i++ )
        {
            for(int j = 0 ; j < 4 ; j++)
                cin>>arr[i][j] ;
        }
        cin>>r2 ;
        for(int i = 0 ; i < 4 ; i++ )
        {
            for(int j = 0 ; j < 4 ; j++)
                cin>>arr1[i][j] ;
        }


        for(int i = 0 ; i < 4 ; i++ )
        {
            for(int j = 0 ; j < 4 ; j++ )
            {
                if(arr[r1-1][i] == arr1[r2-1][j] )
                {
                    temp1[comp] = arr[r1-1][i] ;
                    comp++ ;
                }
            }
        }

        if(comp == 1)
            cout<<"Case #"<<cnt++<<": "<<temp1[comp-1]<<endl ;
        else if(comp == 0 )
            cout<<"Case #"<<cnt++<<": "<<"Volunteer cheated!"<<endl ;
        else
            cout<<"Case #"<<cnt++<<": "<<"Bad magician!"<<endl ;

    }
    return 0 ;
}
