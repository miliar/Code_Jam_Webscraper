//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007
#define zoom 10000000.0
int tcase;
int blocks;
double in;
int naomi[10000];
int ken[10000];
int deceit(){
    int left=0,right=blocks-1;
    int sn=0;
    int coun=0;
    while(left<=right){
        //cout << sn << " " << left << " " << right << " " << coun << endl;
        if (naomi[sn]<ken[left]){
            right--;
            sn++;
        }
        else{
            sn++;
            left++;
            coun++;
        }
    }
    return coun;
}
int war(){
    int sk=0,sn=0;
    int coun=0;
    while(sk<blocks && sn<blocks){
        if (ken[blocks-1-sk]<naomi[blocks-1-sn]){
            sn++;
            coun++;
        }
        else{
            sk++;
            sn++;
        }
    }
    return coun;
}
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&tcase);
    for (int i=1;i<=tcase;i++){
        scanf("%d",&blocks);
        
        for (int j=0;j<blocks;j++){
            scanf("%lf",&in);
            naomi[j]=(int)(in*zoom);    
        }
        sort(naomi,naomi+blocks);
        for (int j=0;j<blocks;j++){
            scanf("%lf",&in);
            ken[j]=(int)(in*zoom);
        }
        sort(ken,ken+blocks);
        
        //calculate the Deceitful
        int bohong=deceit();
        
        //calculate the War not deceit
        int jujur=war();
        
        printf("Case #%d: %d %d\n",i,bohong,jujur);
    }
    return 0;
}
