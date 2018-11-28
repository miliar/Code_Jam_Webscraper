#include<iostream>
#include<cstdio>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<algorithm>
#include<list>
#define ll long long
#define ld long double
#define eps 10e-8
using namespace std;

ld T, C, F, X, N, kupic, odrazu, dodaj, temp2, result;

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> T;
    for(int lzd=1; lzd<=T; ++lzd)
    {
        cin >> C >> F >> X;
        N=2.000000000000000000;
        result=0.0000000000000000000;
        kupic=C/N;
       dodaj=N+F;
        temp2=X/dodaj;
        kupic+=temp2;
        odrazu=X/N;
        //cout.precision(12);
        //cout << kupic << " " << odrazu << endl;
        while(kupic<odrazu+eps) //kupic lepiej niz dobic od razu
        {

            result+=C/N;
            N+=F;
            kupic=C/N;
                    dodaj=N+F;
        temp2=X/dodaj;
            kupic+=temp2;
            odrazu=X/N;
            //cout << kupic << " " << odrazu << endl;
        }
        result+=odrazu;
        printf("Case #%d: %.7Lf\n", lzd, result);
    }
    return 0;
}
