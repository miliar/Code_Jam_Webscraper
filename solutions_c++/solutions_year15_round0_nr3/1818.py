
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <algorithm>
#define maxv 10009

using namespace std;

int T;
int F[maxv][maxv];
int A[maxv];
int n;
long long X;
int multiTable[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1} };
char charMap[5]={'0','1','i','j','k'};

void input(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
}



int charToInt(char p){
    if (p=='1') return 1;
    if (p=='i') return 2;
    if (p=='j') return 3;
    if (p=='k') return 4;
}

int intToChar(int u) {
    return charMap[u];
}

int multiply(int a, int b) {

    int sign = a*b/abs(a*b);
    a=abs(a); b=abs(b);
    int res = multiTable[a-1][b-1];
    res = res *sign;
    return res;
}

int power(int x, int i) {
    if (x==1) {
        return 1;
    }
    if (x==-1) {
        if (i%2==0) {
            return 1;
        } else {
            return -1;
        }
    }
    i=i%4;
    if (i==0) return 1;
    if (i==1) return x;
    if (i==2) return -1;
    if (i==3) return -x;
}
//F[1,n]^pre * x=i
int prefix(int x) {
    int res=-1;
    for (int i=0; i<4; i++) {
        //cout<<"power"<<multiply(power(F[1][n],i),x)<<" "<<power(F[1][n],i)<<" "<<x;
        if (multiply(power(F[1][n],i),x)==2)
            return i;
    }
    return -1;
}

//y*F[1,n]^pre = k;
int suffix(int x) {
    int res=-1;
    for (int i=0; i<4; i++) {
        //cout<<"ff"<<x<<" "<<power(F[1][n],i)<<"ll";
        if (multiply(x,power(F[1][n],i)) ==4)
            return i;
    }
    return -1;
}

void solve(){

    string str;
    string ans;
    int pre[maxv];
    int suff[maxv];

    cin>>T;
    int temp;
    bool res = false;

    for (int t=0;t<T; t++) {
        res=false;
        cin>>n>>X;
        cin.ignore();
        //reading string
        getline(cin,str);
        //tranform str to A
        for (int i=1; i<=n; i++) {
            A[i]=charToInt(str[i-1]);

        }
        //end reading
        for (int i=1; i<=n+1; i++){
            F[i][i-1]=1;
        }

        F[1][0]=1; F[n+1][n]=1;
        for (int i=1; i<=n; i++) {
            for (int j=i; j<=n; j++) {
                F[i][j]=multiply(F[i][j-1],A[j]);
            }
        }

        //cout<<F[1][n];
        int x,y;
        //dynamic programming
        for (int i=0; i<=n; i++){
            x=F[1][i];
            pre[i]=prefix(x);
            //cout<<pre[i]<<"|";
        }
        for (int i=1; i<=n+1; i++){
            x=F[i][n];
            suff[i]=suffix(x);
            //cout<<suff[i]<<" ";
        }

        //cout<<endl;
        for (int i=0; i<=n; i++) {
            if (pre[i]==-1) continue;
            if (res) break;
            for (int j=1; j<=n+1; j++){
                if (suff[j]==-1) continue;
                //cout<<i<<" "<<j<<" "<<pre[i]<<" "<<suff[j]<<endl;
                if (i<j && pre[i]+suff[j]<X) {
                    if (pre[i]+suff[j]==X-1) {
                        if (F[i+1][j-1]==3) {
                            res=true;
                            break;
                        }
                    }
                    if (pre[i]+suff[j]<X-1) {
                        //
                        if (multiply(multiply(F[i+1][n],power(F[1][n],X-pre[i]-suff[j]-2)),F[1][j-1])==3) {
                            res=true;
                            break;
                        }
                    }
                }
                if (i>=j && pre[i]+suff[j]<X-1) {
                    //cout<<"handle"<<i<<" "<<j<<" "<<F[i+1][n]<<" "<<power(F[1][n],X-pre[i]-suff[j]-2)<<endl;
                    if (multiply(multiply(F[i+1][n],power(F[1][n],X-pre[i]-suff[j]-2)),F[1][j-1])==3) {
                        //cout<<"fuck";
                        res=true;
                        break;
                    }
                }
            }
        }
        ans="NO";
        if (res) {
            ans="YES";
        }
        cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
}

void output(){

}

void process(){
    input();
    solve();
    output();
}

int main() {
    process();
    return 0;
}

