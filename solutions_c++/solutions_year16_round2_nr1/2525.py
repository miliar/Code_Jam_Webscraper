#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF     INT_MAX
#define MAX     INT_MAX
#define MOD     1000000007
#define LL      long long

int arr[200];
int main()
{
    READ();
    WRITE();

    int t;
    cin >> t;

    int TC = 0;

    while(t--)
    {
        memset(arr,0,sizeof(arr));
        string s;
        cin >> s;

        for(int i=0;i<s.size();i++)
        {
            arr[s[i]]++;
        }

        vector <int> vec;

        if(arr['Z'] > 0 && arr['E'] > 0 && arr['R'] > 0 && arr['O'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['Z']);
            vecTemp.pb(arr['E']);
            vecTemp.pb(arr['R']);
            vecTemp.pb(arr['O']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(0);
                arr['Z']--;
                arr['E']--;
                arr['R']--;
                arr['O']--;
//                arr['E']--;
            }
        }


        if(arr['T'] > 0 && arr['W'] > 0 && arr['O'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['T']);
            vecTemp.pb(arr['W']);
            vecTemp.pb(arr['O']);
//            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(2);
                arr['T']--;
                arr['W']--;
                arr['O']--;
//                arr['E']--;
//                arr['E']--;
            }
        }

        if(arr['F'] > 0 && arr['O'] > 0 && arr['U'] > 0 && arr['R'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['F']);
            vecTemp.pb(arr['O']);
            vecTemp.pb(arr['U']);
            vecTemp.pb(arr['R']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(4);
                arr['F']--;
                arr['O']--;
                arr['U']--;
                arr['R']--;
//                arr['E']--;
            }
        }

        if(arr['S'] > 0 && arr['I'] > 0 && arr['X'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['S']);
            vecTemp.pb(arr['I']);
            vecTemp.pb(arr['X']);
//            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(6);
                arr['S']--;
                arr['I']--;
                arr['X']--;
//                arr['E']--;
//                arr['E']--;
            }
        }

       if(arr['O'] > 0 && arr['N'] > 0 && arr['E'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['O']);
            vecTemp.pb(arr['N']);
            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(1);
                arr['O']--;
                arr['N']--;
                arr['E']--;
//                arr['E']--;
//                arr['E']--;
            }
        }

        if(arr['T'] > 0 && arr['H'] > 0 && arr['R'] > 0 && arr['E'] > 1)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['T']);
            vecTemp.pb(arr['H']);
            vecTemp.pb(arr['R']);
            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(3);
                arr['T']--;
                arr['H']--;
                arr['R']--;
                arr['E']--;
                arr['E']--;
            }
        }


        if(arr['F'] > 0 && arr['I'] > 0 && arr['V'] > 0 && arr['E'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['F']);
            vecTemp.pb(arr['I']);
            vecTemp.pb(arr['V']);
            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(5);
                arr['F']--;
                arr['I']--;
                arr['V']--;
                arr['E']--;
//                arr['E']--;
            }
        }

        if(arr['S'] > 0 && arr['E'] > 1 && arr['V'] > 0 && arr['N'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['S']);
            vecTemp.pb(arr['E']);
            vecTemp.pb(arr['V']);
            vecTemp.pb(arr['N']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(7);
                arr['S']--;
                arr['E']--;
                arr['V']--;
                arr['E']--;
                arr['N']--;
            }
        }


        if(arr['E'] > 0 && arr['I'] > 0 && arr['G'] > 0 && arr['H'] > 0 && arr['T'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['E']);
            vecTemp.pb(arr['I']);
            vecTemp.pb(arr['G']);
            vecTemp.pb(arr['H']);
            vecTemp.pb(arr['T']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(8);
                arr['E']--;
                arr['I']--;
                arr['G']--;
                arr['H']--;
                arr['T']--;
            }
        }


        if(arr['N'] > 1 && arr['I'] > 0 && arr['E'] > 0)
        {
            vector <int> vecTemp;
            vecTemp.pb(arr['N']);
            vecTemp.pb(arr['I']);
            vecTemp.pb(arr['E']);
//            vecTemp.pb(arr['N']);
//            vecTemp.pb(arr['E']);
            sort(vecTemp.begin(),vecTemp.end());
            for(int i=0;i<vecTemp[0];i++)
            {
                vec.pb(9);
                arr['N']--;
                arr['I']--;
                arr['N']--;
                arr['E']--;
//                arr['N']--;
            }
        }

        sort(vec.begin(),vec.end());

        cout << "Case #" << ++TC << ": ";

        for(int i=0;i<vec.size();i++)cout << vec[i] ;
        cout << endl;


    }


    return 0;
}

