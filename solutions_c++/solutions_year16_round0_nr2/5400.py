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



int main () {

    ios_base::sync_with_stdio(false);
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);


    int t;
    cin >> t;

    fore(tc,1,t+1){
        cout << "case #" << tc << ": ";
        string s;
        cin >> s;

        int ind = s.length()-1,ans = 0;

        while(ind>=0 && s[ind]=='+')
            ind--;

        while(ind>=0){
            char ch = s[ind];
            while(ind >=0 && ch == s[ind])
                ind--;

            ans ++;
        }

        cout << ans << endl;
    }

    return 0;
}
