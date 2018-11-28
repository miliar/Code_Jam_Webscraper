#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<stack>
#include<ctype.h>
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >
#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)
#define maxi(v) max_element(all(v))
#define mini(v) min_element(all(v))
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
using namespace std;

int read_num()
{
    int num = 0;
    char ch;
    ch = getchar();
    while(!isdigit(ch))
        ch = getchar();
    do{
        num = num*10+(ch-'0');
        ch = getchar();
    }while(isdigit(ch));
    return  num;
}
int X[11] = {1,2,3,4,5,6,7,8,9,11,22};
int Y[5] = {1,4,9,121,484};
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n = read_num();
    fia(tt, 1, n+1)
    {
        int a = read_num();
        int b = read_num();
        int cnt = 0;
        for(int i = a ; i <= b; i++)
        {
            bool found = false;
            for(int j = 0; j < 5; j++)
            {
                if(i == Y[j])
                {
                    found = true;
                    break;
                }
            }
            if(found == true)
                cnt++;
        }
        cout<<"Case #"<<tt<<": "<<cnt<<endl;
    }
}