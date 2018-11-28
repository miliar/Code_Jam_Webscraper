/*
MMP""MM""YMM   db      `7MN.   `7MF'`7MMM.     ,MMF' .g8""8q.`YMM'   `MM'
P'   MM   `7  ;MM:       MMN.    M    MMMb    dPMM .dP'    `YM.VMA   ,V
     MM      ,V^MM.      M YMb   M    M YM   ,M MM dM'      `MM VMA ,V
     MM     ,M  `MM      M  `MN. M    M  Mb  M' MM MM        MM  VMMP
     MM     AbmmmqMA     M   `MM.M    M  YM.P'  MM MM.      ,MP   MM
     MM    A'     VML    M     YMM    M  `YM'   MM `Mb.    ,dP'   MM
   .JMML..AMA.   .AMMA..JML.    YM  .JML. `'  .JMML. `"bmmd"'   .JMML.
*/

#include <bits/stdc++.h>

#define pii pair <int,int>
#define sc scanf
#define pf printf
#define Pi 2*acos(0.0)
#define ms(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define MP make_pair
#define oo 1<<29
#define dd double
#define ll long long
#define EPS 10E-10
#define ff first
#define ss second
#define MAX 10000
#define CIN ios_base::sync_with_stdio(0); cin.tie(0)
#define SZ(a) (int)a.size()
#define getint(a) scanf("%d",&a)
#define getint2(a,b) scanf("%d%d",&a,&b)
#define getint3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define loop(i,n) for(int i=0;i<n;i++)
#define TEST_CASE(t) for(int z=1;z<=t;z++)
#define PRINT_CASE printf("Case #%d: ",z)
#define all(a) a.begin(),a.end()
#define intlim 2147483648
#define inf 1000000
#define rtintlim 46340
#define llim 9223372036854775808
#define rtllim 3037000499
#define ull unsigned long long
#define I int

using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t,n;
    getint(t);
    TEST_CASE(t)
    {
        getint(n);
        int ans=0;
        string str;
        cin>>str;
        int a=0,b=0;
        a=str[0]-'0';
        b=SZ(str);
        for(int i=1;i<b;i++)
        {
            if(a<i)
            {
                int x=i-a;
                a+=x;
                ans+=x;
            }
            a+=str[i]-'0';
        }
        PRINT_CASE;
        pf("%d\n",ans);
        str.clear();
    }
    return 0;
}
