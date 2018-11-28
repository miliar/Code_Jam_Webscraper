#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int readInt(){
    char c;
    int n=0;
    c=getchar();
    while(c<'0'||c>'9')c=getchar();
    while(c>='0'&&c<='9'){
        n*=10;
        n+=(c-'0');
        c=getchar();
    }
    return n;
}

void setFlag(vector<bool>& f, int n){
    while(n){
        int r = n%10;
        f[r] = true;
        n /= 10;
    }
}
bool check(vector<bool>& f){
    for(int i=0; i<10; ++i){
        if(!f[i])  return false;
    }
    return true;
}

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int n;
    int ret;
    int T = 1,flag;
    scanf("%d",&T);
    int cas=0;
    vector<bool> f(10,false);
    while (T--)
    {
        //scanf("%d",&n);
        n = readInt();
        if(n == 0){
            printf("Case #%d: INSOMNIA\n",++cas);
            continue;
        }
        f.assign(10,false);
        int m = n;
        setFlag(f,m);
        //printf("%d ",m);
        while(1){
           m += n;
           setFlag(f,m);
           //printf("%d ",m);
           if(check(f))  break;
        }
        //printf("\n");

        printf("Case #%d: %d\n",++cas,m);
    }
    return 0;
}
