#include <bits/stdc++.h>

#define Max      40000
#define Max2     100010
#define mod      1000000007
#define Maxp     78499
#define pf       printf
#define sf       scanf
#define CLR(a)   memset(a,0,sizeof(a))
#define SET(a)   memset(a,-1,sizeof(a))
#define pb       push_back
#define fs       first
#define sc       second
#define TCASE    int T,t=1;scanf("%d",&T);while(T--)
#define loop(n)  for(int i=0;i<n;i++)
#define lop2(n)  for(int i=1;i<=n;i++)
#define lup(a)   for(int i=0;i<strlen(a);i++)
#define NL       pf("\n")
#define uplo     0b00100000
#define _        ios_base::sync_with_stdio(false); cin.tie(false);
#define check(a,b) a & (1 << b)

using namespace std;

typedef long long ll;
typedef unsigned long long llu;
typedef unsigned long lu;
const double eps = 1e-9;
const double PI  = 3.1415926535897932384626433832795;
const int    inf = 0x7f7f7f7f;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    TCASE
    {
        char ar[3000];
        sf("%s",ar);
        int len = strlen(ar);
        int res[10][30];
        CLR(res);
        res[0][25]=1;
        res[0][4]=1;
        res[0][17]=1;
        res[0][14]=1;

        res[1][14]=1;
        res[1][13]=1;
        res[1][4]=1;

        res[2][14]=1;
        res[2][19]=1;
        res[2][22]=1;

        res[3][19]=1;
        res[3][17]=1;
        res[3][4]=2;
        res[3][7]=1;

        res[4][5]=1;
        res[4][14]=1;
        res[4][20]=1;
        res[4][17]=1;

        res[5][5]=1;
        res[5][8]=1;
        res[5][21]=1;
        res[5][4]=1;

        res[6][18]=1;
        res[6][8]=1;
        res[6][23]=1;

        res[7][18]=1;
        res[7][4]=2;
        res[7][21]=1;
        res[7][13]=1;

        res[8][4]=1;
        res[8][8]=1;
        res[8][6]=1;
        res[8][7]=1;
        res[8][19]=1;

        res[9][4]=1;
        res[9][8]=1;
        res[9][13]=2;

//        for(int j=0;j<10;j++)
//        {
//            for(int i=0;i<26;i++)
//            {
//                for(int k=0;k<res[j][i];k++) pf("%c",i+'A');
//            }
//            pf("\n");
//
//        }



        int cur = 0;
        int res2[26];
        CLR(res2);
        for(int i=0;i<len;i++)
        {
            int x = ar[i] - 'A';
            res2[x]++;
        }
        //for(int i=0;i<26;i++)  pf("%c %d\n",i+'A',res2[i]);
        vector <int> ans;


            if(res2[22])
            {
                int x = res2[22];
                res2[22]=0;
                res2[14]-=x;
                res2[19]-=x;
                for(int j=0;j<x;j++) ans.pb(2);
            }
            if(res2[20])
            {
                int x = res2[20];
                res2[20]=0;
                res2[5]-=x;
                res2[14]-=x;
                res2[17]-=x;
                for(int j=0;j<x;j++) ans.pb(4);
            }
            if(res2[23])
            {
                int x = res2[23];
                res2[23]=0;
                res2[18]-=x;
                res2[8]-=x;
                for(int j=0;j<x;j++) ans.pb(6);
            }


        for(int i=0;i<10;i++)
        {
            int flag = 0,f=0;
            for(int j=0;j<26;j++)
            {
                if(res[i][j]==0) continue;
                if(res[i][j]>res2[j]) flag = 1;
                f = 1;
            }
            if(!flag && f)
            {
                for(int m=0;m<26;m++)
                      res2[m]-=res[i][m];
                ans.pb(i);
                i--;
            }
        }

        pf("Case #%d:",t++);

//        for(int i=0;i<26;i++)
//        {
//            if(res2[i])
//            {
//                pf("Mara\n");
//                return 0;
//            }
//        }
        sort(ans.begin(),ans.end());
        for(int i=0;i<ans.size();i++)
        {
            if(!i) pf(" ");
            pf("%d",ans[i]);
        }
        pf("\n");
    }
    return 0;
}
