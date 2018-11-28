/*
ID: jsnjhcb1
PROG: b
LANG: C++
*/
/*************************************************************************
	> File Name: b.cpp
	> Author: UCU
	> Mail: jsnjhcb@icloud.com
	> Created Time: 六  4/ 9 19:22:40 2016
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
char s[110];
int main(){
    int T;
    scanf("%d",&T);
    for(int ca = 1;ca <= T; ++ca){
        printf("Case #%d: ",ca);
        scanf("%s",s);
        int size = (int)strlen(s);
        int ans = 0;
        for(int i=0;i<size-1;++i){
            if(s[i]!=s[i+1]){
                ++ans;
            }
        }
        if(s[size-1]=='-') ++ans;
        printf("%d\n",ans);
    }
    return 0;
}
