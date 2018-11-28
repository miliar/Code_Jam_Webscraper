#include <iostream>
#include <stdio.h>
#include <map>
#include <cmath>
#include <assert.h>
#include <vector>
using namespace std;
int tt;
int A[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
map<char,int> mp;
int mul(int a,int b)
{
    int flag = 1;
    int temp = a*b;
    if(temp<0)flag = -1;
    a = abs(a);b = abs(b);
    return A[a][b]*flag;
}
int num(int a,int b)
{
    int flag = 0;
    int ans = 0;
    int X = a,Y = b;
    a = abs(a);b = abs(b);
    for(int i=1;i<=4;i++)
    {
        if(abs(A[a][i]) == b){flag = 1;ans = i;break;}
    }
    assert(flag);
    if(mul(X,ans)==Y)return ans;
    return (-ans);
}
int AA[10005*12];
int IAA[10005*12];
int cal(int i,int j)
{
    if(i>j)return 0;
    if(i==0)return AA[j];
    return num(AA[i-1],AA[j]);
}
void solve()
{
    mp['i'] = 2;mp['j'] = 3;mp['k'] = 4;
    int L,X;
    scanf("%d%d",&L,&X);
    string ss;
    cin >> ss;
    string st = ss;
    int upto = min(X,12+(X%4));
    for(int i=1;i<upto;i++) st+=ss;
    int len = st.length();
    int curr = 1;
    //cout<<st<<endl;
    int flag = 0;
    vector<int> I;
    for(int i=0;i<len;i++)
    {
        curr = mul(curr,mp[st[i]]);
        AA[i] = curr;
        if(AA[i] == 2)I.push_back(i);
    }
    //for(int i=0;i<len;i++)cout<<AA[i]<<" ";cout<<endl;
    IAA[0] = curr;
    curr = 1;
    vector<int> K;
    for(int i=1;i<len;i++)
    {
        IAA[i] = num(AA[i-1],IAA[0]);
        //cout<<IAA[i]<<" ";
        if(IAA[i]==4)K.push_back(i);
    }
    //cout<<endl;
    int lenI = I.size();
    int lenK = K.size();
    //for(int i=0;i<lenI;i++)cout<<I[i]<<" ";cout<<endl;
    //for(int i=0;i<lenK;i++)cout<<K[i]<<" ";cout<<endl;
    for(int i=0;i<lenI;i++)
    {
        int posi = I[i];
        for(int j=0;j<lenK;j++)
        {
            if((posi < K[j])&& (cal(posi+1,K[j]-1) == 3)){flag = 1;break;}
        }
        if(flag)break;
    }
    if(flag)printf("Case #%d: YES\n",tt);
    else printf("Case #%d: NO\n",tt);
}
int main()
{
    int t;
    scanf("%d",&t);
    for(tt = 1;tt <= t; tt++)
    {
        solve();
    }
}
