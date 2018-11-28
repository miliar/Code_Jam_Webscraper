#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<bitset>
#include<cassert>
#include<iomanip>
using namespace std;

#define LL long long
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define VI vector<int>
#define VPI vector<PI>
#define PB push_back

#define MAXD 105
#define MAXNUM 25

struct number{
    char* n;
    int sz;
    number(){
        n = new char[MAXD+1];
        for(int i=0;i<=MAXD;i++) n[i] = '0';
        sz = MAXD;
        n[sz] = '\0';
        //normalize();
    }
    void normalize(){
        sz = MAXD;
        while(sz >= 0 && !(n[sz] >= '1' && n[sz] <= '9')){
            n[sz] = '0';
            sz--;
        }
        sz++;
        n[sz] = '\0';
        //printf("normalized %s to size %d\n", n, sz);
    }
    void printOutput(){
        char* str = new char[MAXD];
        for(int i=0;i<sz;i++) str[i] = n[sz-1-i];
        str[sz] = '\0';
        printf("%s\n", str);
    }
    void takeInput(){
        char* str = new char[MAXD];
        scanf("%s", str);
        int l = strlen(str);
        for(int i=0;i<l;i++) n[i] = str[l-1-i];
        n[l] = '\0';
        normalize();
        //printf("done with input for "); printOutput(a);
    }
    bool isPalindrome(){
        int i=0;
        while(sz-1-i > i){
            if(n[i] != n[sz-1-i]) return 0;
            i++;
        }
        return 1;
    }
};

vector<number> v,w;

number product(number& a,number& b)
{
    //printf("sizes (%d,%d)\n", a.sz, b.sz);
    number c;
    for(int i=0;i<MAXD;i++) c.n[i] = '0';
    for(int i=0;i<a.sz;i++){
        for(int j=0;j<b.sz;j++){
            int x = a.n[i] - '0';
            int y = b.n[j] - '0';
            //printf("(x,y)=(%d,%d)\n", x, y);
            int currd = i+j;
            int r = ((c.n[currd] - '0') + x*y);
            while(r >= 10){
                c.n[currd] = '0' + r%10;
                r/=10;
                currd++;
                r += c.n[currd] - '0';
            }
            c.n[currd] = '0' + r;
        }
    }
    c.normalize();
    return c;
}

number square(number& a)
{
    return product(a,a);
}

void check(number& a)
{
    a.normalize();
    if(a.isPalindrome()){
        number b = square(a);
        if(b.isPalindrome()){
            v.PB(b);
        }
    }
}

void oneTwo(int D,int s)
{
    if(s == -1){
        number a;
        a.n[0] = a.n[2*D-1] = '2';
        check(a);
    }
    else{
        number a;
        a.n[0] = a.n[2*D] = '2';
        a.n[D] = ('0' + s);
        check(a);
    }
}

void markAndCheckForEven(int p1,int p2,int p3,int D)
{
    number a;
    a.n[0] = a.n[2*D-1] = '1';
    if(p1 < D) a.n[p1] = a.n[2*D-1-p1] = '1';
    if(p2 < D) a.n[p2] = a.n[2*D-1-p2] = '1';
    if(p3 < D) a.n[p3] = a.n[2*D-1-p3] = '1';
    check(a);
}

void markAndCheckForOdd(int p1,int p2,int p3,int D,int centre)
{
    number a;
    a.n[0] = a.n[2*D] = '1';
    a.n[D] = '0' + centre;
    if(p1 < D) a.n[p1] = a.n[2*D-p1] = '1';
    if(p2 < D) a.n[p2] = a.n[2*D-p2] = '1';
    if(p3 < D) a.n[p3] = a.n[2*D-p3] = '1';
    check(a);
}

void oddLength(int D)
{
    oneTwo(D,0);
    oneTwo(D,1);
    for(int i=1;i<=D;i++){
        for(int j=i+1;j<=D+1;j++){
            for(int k=j+1;k<=D+2;k++){
                markAndCheckForOdd(i,j,k,D,0);
                markAndCheckForOdd(i,j,k,D,1);
                markAndCheckForOdd(i,j,k,D,2);
            }
        }
    }
}

void evenLength(int D)
{
    oneTwo(D,-1);
    for(int i=1;i<=D;i++){
        for(int j=i+1;j<=D+1;j++){
            for(int k=j+1;k<=D+2;k++){
                markAndCheckForEven(i,j,k,D);
            }
        }
    }
}

void preprocess()
{
    number a;
    a.n[0] = '1';
    a.normalize();
    v.PB(a);
    number b;
    b.n[0] = '4';
    b.normalize();
    v.PB(b);
    number c;
    c.n[0] = '9';
    c.normalize();
    v.PB(c);
    for(int D=1;D<=MAXNUM-1;D++){
        oddLength(D);
    }
    for(int D=1;D<=MAXNUM;D++){
        evenLength(D);
    }
}

bool same(number a,number b)
{
    if(a.sz == b.sz){
        for(int i=0;i<a.sz;i++) if(a.n[i] != b.n[i]) return 0;
        return 1;
    }
    return 0;
}

bool mySort(number a,number b)
{
    if(a.sz > b.sz) return 0;
    if(a.sz < b.sz) return 1;
    for(int i=a.sz-1;i>=0;i--){
        if(a.n[i] < b.n[i]) return 1;
        if(a.n[i] > b.n[i]) return 0;
    }
    return 0;
}

int main()
{
    freopen("input3.txt","r", stdin);
    freopen("outputL3.txt", "w", stdout);
    preprocess();
    sort(v.begin(),v.end(),mySort);
    w.PB(v[0]);
    for(int i=1;i<v.size();i++) if(!same(v[i],v[i-1])) w.PB(v[i]);
    //printf("size of vector is %d\n", w.size());
    //for(int i=0;i<w.size();i++) w[i].printOutput();
    int cases;
    scanf("%d", &cases);
    for(int casenum=1;casenum<=cases;casenum++){
        number a;
        a.takeInput();
        number b;
        b.takeInput();
        int idx1 = 0;
        while(idx1 <= w.size() && mySort(w[idx1],a)) idx1++;
        int idx2 = w.size()-1;
        while(idx2 >= 0 && mySort(b,w[idx2])) idx2--;
        printf("Case #%d: %d\n", casenum, idx2-idx1+1);
    }
    return 0;
}
