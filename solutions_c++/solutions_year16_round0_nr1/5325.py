#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
#include <bits/stdc++.h>

#define LLMAX 1000000000000000000
#define LL long long
#define LD long double
#define mod 1000000007
#define fore(a,b,c)  for(int a=b;a<c;a++)
#define forw(a,b,c)  for(int a=b;a>c;a--)
#define pb push_back
#define fs first
#define sc second
#define mp make_pair


using namespace std;

LL n,x;
int vis[10] = {0};

void dig (){
    while(x){
        vis[x%10] = 1;
        x /= 10;
    }
}

int main () {

    ios_base::sync_with_stdio(false);
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);


    int t;
    cin >> t;

    fore(tc,1,t+1){
        cin >> n;
        cout << "case #" << tc << ": ";
        bool ans = true;

        fore(j,0,10)
            vis[j] = 0;

        fore (i,1,100000){
            x = n*i;
            dig();
            bool flag = true;
            fore(j,0,10)
                if(!vis[j])
                    flag = false;

            if(flag){
                ans = false;
                cout << n*i << endl;
                break;
            }
        }

        if(ans)
            cout << "INSOMNIA\n";

    }

    return 0;
}
