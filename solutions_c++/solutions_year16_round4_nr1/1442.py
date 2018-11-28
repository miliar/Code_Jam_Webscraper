#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;

int T;
int Peo[3];
int a[1<<14];
int ans[3];
int N;
//入口 0,i,0,N;
void dfs(int k,int num,int l, int r)
{
//    cout<<k<<endl;
    if (r - l == 1) {a[k] = num; return;}
    else {
        int chl = k*2+1,chr = k*2+2;
        int m = (l+r)/2;
        a[k] = num;
        if (num == 1) {
            if ( m -l > 1 and r - m > 1)
            {
            dfs(chl,2,l,m);
            dfs(chr,1,m,r);
            }
            else
            {
            dfs(chl,1,l,m);
            dfs(chr,2,m,r);
            }
        }
        else if (num == 2) {
            if (m - l > 1 and r - m > 1) {

            dfs(chl,3,l,m);
            dfs(chr,2,m,r);

            }
            else{
                 dfs(chl,2,l,m);
                 dfs(chr,3,m,r);
            }
        }
        else {
            if (m - l> 1 and r - m > 1)
            {
            dfs(chl,3,l,m);
            dfs(chr,1,m,r);
            }
            else {
            dfs(chl,1,l,m);
            dfs(chr,3,m,r);
            }
        }
    }
    return;
}
string paixu[1<<14];
string sor(int k,int l,int r)
{
    if (r - l == 1) {if (a[k] == 1) return "1";
    else if (a[k] == 2) return "2";
    else if (a[k] == 3) return "3";}
    else
    {
        int chl = k*2+1,chr = k*2+2,m = (l+r)/2;
        string x = sor(chl,l,m);
        string y = sor(chr,m,r);
        if (x > y) x = y + x;
        else x = x + y;

        return x;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out_large.txt","w",stdout);
    cin>>T;
    for (int k = 1; k <= T; k++)
    {
        cin>>N;
        N = (1<<N);
//        cout<<N<<endl;
        cin>>Peo[1]>>Peo[0]>>Peo[2];
        cout<<"Case #"<<k<<": ";
        int flag = false;
        memset(a,0,sizeof a);

        for (int j = 1; j <=3 ; j++)
        {
            dfs(0,j,0,N);
            ans[0] = ans[1] = ans[2] = 0;
            for (int i = 0; i < N; i++)
            {
                ans[ a[i+N-1] - 1 ]++;

            }
            int mark = true;
            for (int i = 0; i < 3; i++)
            {
                if (Peo[i] != ans[i]) mark = false;
                if (mark == false) break;
            }
            if (mark == true)
            {
                flag = true;
                break;
            }
        }

        if (!flag)
        {
            cout<<"IMPOSSIBLE"<<endl;
//            cout<<ans[0]<<" "<<ans[1]<<" "<<ans[2]<<endl;
        }
        else {
            string res = sor(0,0,N);
            for (int i = 0; i < N; i ++)
            {
                if (res[i] == '1') cout<<'P';
                else if (res[i] == '2') cout<<'R';
                else if (res[i] == '3')cout<<'S';
            }
            cout<<endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
}
