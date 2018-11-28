/*
*Rainto96
*Beijing University of Posts and Telecommunications School of Software Engineering
*http://blog.csdn.net/u011775691
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <climits>
using namespace std;
#define pb push_back
#define ALL(x) x.begin(),x.end()
#define VINT vector<int>
#define PII pair<int,int>
#define MP(x,y) make_pair((x),(y))
#define ll long long
#define ull unsigned long long
#define MEM0(x)  memset(x,0,sizeof(x))
#define MEM(x,val) memset((x),val,sizeof(x))
#define scan(x) scanf("%d",&(x))
#define scan2(x,y) scanf("%d%d",&(x),&(y))
#define scan3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define scan4(x,y,z,k) scanf("%d%d%d%d",&(x),&(y),&(z),&(k))
#define Max(a,b) a=max(a,b)
#define Min(a,b) a=min(a,b)
#define fuck(x) cout<<#x<<" - "<<x<<endl
char str[10111];
int len;
bool check(){
    for(int i=0;i<len;i++){
        if(str[i] == '-') return false;
    }
    return true;
}
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;scan(T);
    for(int cas = 1; cas<=T;cas++){
        printf("Case #%d: ",cas);
        scanf("%s",str);
        len = strlen(str);
        int ans=0;
        while(!check()){
            //cout<<str<<endl;
            int pos=-1;
            for(int i=0;i<len;i++){
                if(str[i] == '+') pos=i;
                else break;
            }
            if(pos!=-1) ans++;
            pos++;
            reverse(str,str+pos);
            //cout<<"1:"<<pos<<endl;
            for(int i=0;i<pos;i++){
                if(str[i]=='+') str[i]='-';
                else str[i]='+';
            }
            for(int i=len-1;i>=0;i--){
                if(str[i] == '-'){
                    pos = i;
                    break;
                }
            }
            pos++;
            //cout<<"2:"<<pos<<endl;
            reverse(str,str+pos);
            for(int i=0;i<pos;i++){
                if(str[i]=='+') str[i]='-';
                else str[i]='+';
            }
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
