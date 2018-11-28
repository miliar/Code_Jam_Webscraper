#include<bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long int
#include<fstream>

using namespace std ;

int main()
{
    ios_base::sync_with_stdio(false) ;

    int test ;

    cin >> test ;

    ofstream myfile ;

    myfile.open("GCJ-1.txt") ;

    int N ; string s1 ; int minneeded = 1e8 , x = 1 ;

    while(test--)
    {
        minneeded = 1e8 ;

        cin >> N >> s1 ;

        int maxaudience = N ; // max people require to stand up and clap

        int cost[N + 1] ;

        for(int i = 0 ; i < s1.length() ; i++)
            cost[i] = s1[i] - '0' ;

        int needed = 0 , t = 0 ;

        for(int i = 0 ; i < s1.length() ; i++)
        {
             if(i == 0 && cost[0] == 0)
              {
                  t = 1 ;
                  needed = 1 ;
              }

            else {

            if(cost[i] != 0)
            {
                if(t >= i || t == 0)
                    t = t + cost[i] ;

            else
            {
                needed = needed + i - t ;
                t = t + (i - t) ;
                t = t + cost[i] ;
            }

            }

                }
        }

         myfile << "Case" << " " << "#" << x << ":" << " " << needed << endl ;

         x = x + 1 ;

    }

    return 0 ;
}
