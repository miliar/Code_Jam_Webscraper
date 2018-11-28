#include <stdio.h>
#include <string>
using namespace std;

char inferior(char c){
    switch(c){
        case 'R':
            return 'S';
        break;
        case 'P':
            return 'R';
        break;
        case 'S':
            return 'P';
        break;
    }
}

string branch(char c, int n){
    if(n==0){
        string s=" ";
        s[0] = c;
        return s;
    }else if(n==1){
        switch(c){
            case 'R':
                return "RS";
            break;
            case 'P':
                return "PR";
            break;
            case 'S':
                return "PS";
            break;
        }
    }else{
        string a = branch(c, n-1);
        string b = branch(inferior(c), n-1);
        string op1 = a+b;
        string op2 = b+a;
        if(op1<op2){
            return op1;
        }
        return op2;
    }
}

void cnt(string &ss, int &r, int &p, int &s){
    r=p=s=0;
    for(unsigned i=0;i<ss.size();++i){
        if(ss[i]=='R'){
            ++r;
        }else if(ss[i]=='P'){
            ++p;
        }else{
            ++s;
        }
    }
}

void solve(int t, int N, int R, int P, int S){
    char c[] = {'R', 'P', 'S'};
    
    string best="";
    for(int i=0;i<3;++i){
        int r, p, s;
        string op = branch(c[i], N);
        cnt(op, r, p, s);
        if((r==R) && (p==P) && (s==S)){
            if((best.size()==0) || (op<best)){
                best = op;
            }
        }
    }
    if(best.size()==0){
        printf("Case #%d: IMPOSSIBLE\n",t);
    }else{
        printf("Case #%d: %s\n", t, best.c_str());
    }
}


int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        int N, R, P, S;
        scanf("%d%d%d%d", &N, &R, &P, &S);
        solve(t, N, R, P, S);
    }
    return 0;
}


