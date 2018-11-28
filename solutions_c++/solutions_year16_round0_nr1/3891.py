/*
ID: jsnjhcb1
PROG: a
LANG: C++
*/
/*************************************************************************
	> File Name: a.cpp
	> Author: UCU
	> Mail: jsnjhcb@icloud.com
	> Created Time: 六  4/ 9 19:03:14 2016
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cctype>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<string>
#include<cstdlib>
#include<queue>
#include<cmath>
#include<iomanip>
#include<climits>
#include<fstream>
using namespace std;
long long solve(long long n){
    int cnt = 0;
    long long ans = 1;
    bool vis[10];
    memset(vis,false,sizeof vis);
    while(cnt < 10){
        long long tmp = ans * n;
        while(tmp){
            int k = tmp%10;
            if(!vis[k]){
                ++cnt;
                vis[k] = true;
            }
            tmp /= 10; 
        }
        ans++;
    }
    return (ans - 1) * n;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        cout << "Case #" << ca << ": ";
        long long n;
        cin >> n;
        if(n==0) cout << "INSOMNIA" << endl;
        else cout << solve(n) << endl;
    }
    return 0;
}
