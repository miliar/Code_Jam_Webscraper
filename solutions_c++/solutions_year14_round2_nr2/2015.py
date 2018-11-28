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
#include <iomanip>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int t ;
    cin>>t ;
    int cnt = 1 ;
    while(t--)
    {
        int A, B , K  ;

        cin>>A>>B>>K ;
        unsigned long long num = 0 ;

        for(int i = 0 ; i < A ; i++ )
        {
            for(int j = 0 ; j < B ; j++ )
            {
                int temp = i&j  ;
                if( temp < K )
                    {
                        num++ ;
                    }
            }
        }
            cout<<"Case #"<<cnt++<<": "<<num<<endl ;
    }

    return 0 ;
}
