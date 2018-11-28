/*
    Author : RAJON BARDHAN
    AUST CSE 27th Batch
    All my programming success are dedicated to my love TANIA SULTANA RIMY

    ALGORITHM : AD HOC
*/
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define ff first
#define ss second
#define memo(a,b) memset(a,b,sizeof(a))
#define EPS 1e-8
#define PI 3.14159265358979323846
typedef long long ll ;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T ;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int Smax ;
        string input ;
        cin >> Smax >> input ;
        int already = 0 , ans = 0 ;
        for(int i=0;i<input.size();i++)
        {
            int t = input[i] - '0' ;
            if(already<i)
            {
                while(already!=i)
                {
                    already++;
                    ans++;
                }
            }
            already+=t;
        }
        cout << "Case #" << cas << ": " << ans << endl ;
    }
    return 0;
}
