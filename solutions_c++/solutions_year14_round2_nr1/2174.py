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

char in[155][45] ;
char out[155][45] ;
char xori[155][45] ;

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int t ;
    cin>>t ;
    int cnt = 1 ;
    while(t--)
    {
        int N ;
        string in[100] ;
        char data[100][100] ;
        int sd[100][100] ;
        int avg[100] ;
        cin>>N;

        for(int i =0 ; i < N ; i++)
        {
            cin>>in[i] ;
        }

        int safelen = 0 ;
        int flag = 1 ;
        for(int i =0 ; i < N ; i++)
        {
            char ch = '-' ;
            int len = 0 ;
            for(int j = 0 ; j < in[i].length() ; j++ )
            {
                if(ch != in[i][j] )
                {
                    ch = in[i][j] ;
                    data[i][len] = in[i][j] ;
                    sd[i][len] = 1 ;
                    len++ ;
                }
                else
                {
                    sd[i][len-1]++ ;
                }
            }
            data[i][len] = '\0' ;
            if(safelen == 0 )
                safelen = len ;

            if(safelen != len )
                flag = 0 ;

        }
        for(int i =0 ; i < 100 ; i++)
        {
            avg[i] = 0 ;
        }
        for(int i =0 ; i < N ; i++)
        {
            int j = 0 ;
            while(data[i][j] != '\0' )
            {
                avg[j] += sd[i][j] ;
                j++ ;
            }
        }
        int j = 0 ;
        while(data[0][j] != '\0' )
        {
            char w = data[0][j] ;
            for(int i =0 ; i < N ; i++)
            {
                if(data[i][j] != w )
                {
                    flag = 0 ;
                    break ;
                }

            }
            j++ ;
        }

        int flips = 0 ;
        for(int i =0 ; i < N ; i++)
        {
            int j = 0 ;
            while(data[i][j] != '\0' )
            {
                flips += abs( sd[i][j] - avg[j]/N );
                j++ ;
            }
        }


        if(flag == 1)
            cout<<"Case #"<<cnt++<<": "<<flips<<endl ;
        else
            cout<<"Case #"<<cnt++<<": Fegla Won"<<endl ;
    }

    return 0 ;
}
