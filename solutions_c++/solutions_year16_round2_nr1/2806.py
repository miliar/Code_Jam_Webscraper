#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
//freopen("D.in","r",stdin);
//freopen("D.out","w",stdout);
#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define dbg(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define maxn 10001
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
#define eps 1e-9
const int MAXN=220;
double a[MAXN][MAXN]={
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {1,1,0,2,0,1,0,2,1,1},
            {0,0,0,0,1,1,0,0,0,0},
            {0,0,0,0,0,0,0,0,1,0},
            {0,0,0,1,0,0,0,0,1,0},
            {0,0,0,0,0,1,1,0,1,1},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,1,0,0,0,0,0,1,0,2},
            {1,1,1,0,1,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {1,0,0,1,1,0,0,0,0,0},
            {0,0,0,0,0,0,1,1,0,0},
            {0,0,1,1,0,0,0,0,1,0},
            {0,0,0,0,1,0,0,0,0,0},
            {0,0,0,0,0,0,0,1,0,1},
            {0,0,1,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,1,0},
            {0,0,0,0,0,0,0,0,0,0},
            {1,0,0,0,0,0,0,0,0,0}
        },x[MAXN];//方程的左边的矩阵和等式右边的值，求解之后x存的就是结果
int equ,var;//方程数和未知数个数
/*
*返回0表示无解，1表示有解
*/
int Gauss()
{
    int i,j,k,col,max_r;
    for(k=0,col=0; k<equ&&col<var; k++,col++)
    {
        max_r=k;
        for(i=k+1; i<equ; i++)
            if(fabs(a[i][col])>fabs(a[max_r][col]))
                max_r=i;
        if(fabs(a[max_r][col])<eps)return 0;
        if(k!=max_r)
        {
            for(j=col; j<var; j++)
                swap(a[k][j],a[max_r][j]);
            swap(x[k],x[max_r]);
        }
        x[k]/=a[k][col];
        for(j=col+1; j<var; j++)a[k][j]/=a[k][col];
        a[k][col]=1;
        for(i=0; i<equ; i++)
            if(i!=k)
            {
                x[i]-=x[k]*a[i][k];
                for(j=col+1; j<var; j++)a[i][j]-=a[k][j]*a[i][col];
                a[i][col]=0;
            }
    }
    return 1;
}
int cnt[26];
char aa[2020];
int con(char a)
{
    return a-'a';
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        clr(cnt);
        scanf("%s",aa);
        int i;
        for (i=0;i<strlen(aa);i++)
            cnt[aa[i]-'A']++;
        for (i=0;i<26;i++)
            x[i]=cnt[i];
        Gauss();
        vector <int> v;
        for (i=0;i<10;i++)
        {
            while(v[i]--)
            v.push_back(i);
        }
        sort(v.begin(),v.end());
        for (i=0;i<v.size();i++)
            cout<<v[i];
    }
    return 0;
}
