#include <iostream>
using namespace std;

int i,j,k,s,l,x,n,result=0;
char ijk[10001];

int m(int a,int b){
    /* 1ijk
      +1234 */
    s = 1;
    if(a<0){ s*=-1; a*=-1; }
    if(b<0){ s*=-1; b*=-1; }

    if(a==1||b==1) return a*b*s;
    if(a==b) return -1*s;
    if(a==2){
        if(b==3) return 4*s;
        if(b==4) return -3*s;
    }
    if(a==3){
        if(b==2) return -4*s;
        if(b==4) return 2*s;
    }
    if(a==4){
        if(b==2) return 3*s;
        if(b==3) return -2*s;
    }
}

int c(char ch){
    if(ch=='i') return 2;
    if(ch=='j') return 3;
    if(ch=='k') return 4;
}

void problem(int target,int si,int sj){
    n = 1;
    for(i=si;i<=x;i++){
        for(j=sj;j<l;j++){
            n = m(n,c(ijk[j]));
            if(n==target&&target!=4){
                problem(target+1,i,j+1);
            }
        }
        sj=0;
    }
    if(target==4&&n==4) result=1;
}

int main(){
    int CASENO,TESTCASE;
    cin >> TESTCASE;
    for(CASENO=1;CASENO<=TESTCASE;CASENO++){
        result=0;
        cin >> l >> x;
        cin >> ijk;
        cout << "Case #" << CASENO << ": ";
        problem(2,1,0);
        if(result==1) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
