#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

int you[4];
int pro[7];

void c5()
{
    int j;
    For(j,7)
    {
        int temp=pro[j];
        int res=0;
        while(temp%5==0&&temp>0)
        {
            res++;
            temp=temp/5;
        }
        if(res>you[3])
            you[3]=res;
    }
}

void c4()
{
    int j;
    For(j,7)
    {
        int temp=pro[j];
        int res=0;
        while(temp%4==0&&temp>0)
        {
            res++;
            temp=temp/4;
        }
        if(res>you[2])
            you[2]=res;
    }
}

void c3()
{
    int j;
    For(j,7)
    {
        int temp=pro[j];
        int res=0;
        while(temp%3==0&&temp>0)
        {
            res++;
            temp=temp/3;
        }
        if(res>you[1])
            you[1]=res;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    
    int num,i,j;
    cin >> num;
    int R=100,N=3,M=5,K=7;
    cin >> R >> N >> M >>K;
    cout << "Case #" << 1 << ": " <<endl;
    for(i=0;i<R;i++)
    {
        Fill(you,0);
        Fill(pro,0);
        For(j,K)
        {
            cin >> pro[j];
        }
        c5();
        c4();
        c3();
        int to=0;
        if(you[1]+you[2]+you[3]>=3)
        {
            while(you[1]>0)
            {
                you[1]--;
                cout << "3";
            }
            while(you[2]>0)
            {
                you[2]--;
                cout << "4";
            }
            while(you[3]>0)
            {
                you[3]--;
                cout << "5";
            }
            cout << endl;
            continue;
        }
        if(you[3]>0)
        {
            cout << "5";
            to++;
        }
        if(you[2]>0)
        {
            cout << "4";
            to++;
        }
        if(you[1]>0)
        {
            cout << "3";
            to++;
        }
       
        if(to==0)
            cout<<"222";
        else if(to==1)
            cout<<"22";
        else if(to==2)
            cout<<"2";
        
        cout << endl;
        
    }
    return 0;
    
}