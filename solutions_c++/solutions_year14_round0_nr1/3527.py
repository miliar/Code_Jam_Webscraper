#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <fstream>
#define si(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#ifndef ONLINE_JUDGE
    #define gc getchar
#else
    #define gc getchar_unlocked
#endif
#define ll long long
#define ull unsigned long long
#define rep(i,a,b) for(int i=a;i<b;i++)
#define repi(i,a,b) for(int i=a;i>b;i--)
#define MOD 1000000007
using namespace std;

int main()
{
    int t;
    cin>>t;
    rep(i,1,t+1)
    {
        int choice1, choice2;
        int first[4][4], second[4][4];
        cin>>choice1;
        rep(j,0,4)
        {
            rep(k,0,4)
            {
                cin>>first[j][k];
            }
        }
        cin>>choice2;
        rep(j,0,4)
        {
            rep(k,0,4)
            {
                cin>>second[j][k];
            }
        }
        int possible[4];
        rep(j,0,4)
        {
            possible[j]=first[choice1-1][j];
        }
        bool cheat=true;
        int cnt=0;
        int num=0;
        rep(j,0,4)
        {
            if(second[choice2-1][j]==possible[0] || second[choice2-1][j]==possible[1] || second[choice2-1][j]==possible[2] || second[choice2-1][j]==possible[3])
            {
                cheat=false;
                cnt++;
                num=second[choice2-1][j];
            }
        }
        if(cheat)
        {
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
            continue;
        }
        else
        {
            if(cnt>1)
            {
                cout<<"Case #"<<i<<": Bad magician!"<<endl;
            }
            else
            {
                cout<<"Case #"<<i<<": "<<num<<endl;
            }
        }
    }
}
