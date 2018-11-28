#include <iostream>
#include <vector>
using namespace std;
int digs[100];
bool ispal(long long x) {
    int dc = 0;
    while (x) {digs[dc++]=x%10;x/=10;}
    for (int i=0; i+i<dc; i++) if (digs[i]!=digs[dc-i-1]) return false;
    return true;
}
int tosquare[50];
int squared[100];
int found;
void go(int N, int upto);
void put(int N, int upto, int dig) {
    bool ok = true;
    tosquare[upto] = tosquare[N-1-upto] = dig;
    for (int i=0; i<upto; i++) {
        squared[i+upto] += 2*tosquare[i]*tosquare[upto];
        if (squared[i+upto]>=10) ok = false;
        squared[N-1-i+upto] += 2*tosquare[N-1-i]*tosquare[upto];
        if (squared[N-1-i+upto]>=10) ok = false;

        if (N-1-upto!=upto) {
            squared[i+N-1-upto] += 2*tosquare[i]*tosquare[N-1-upto];
            if (squared[i+N-1-upto]>=10) ok = false;
            squared[N-1-i+N-1-upto] += 2*tosquare[N-1-i]*tosquare[N-1-upto];
            if (squared[N-1-i+N-1-upto]>=10) ok = false;
        }
    }
    if (N-1-upto!=upto) squared[upto+N-1-upto] += 2*dig*dig;
    squared[2*upto] += dig*dig;
    if (N-1-upto!=upto) squared[2*(N-1-upto)] += dig*dig;
    if (squared[upto+N-1-upto]>=10 || squared[2*upto]>=10 || squared[2*(N-1-upto)]>=10) ok=false;
    
    if (ok) go(N,upto+1);
    
    if (N-1-upto!=upto) squared[upto+N-1-upto] -= 2*dig*dig;
    squared[2*upto] -= dig*dig;
    if (N-1-upto!=upto) squared[2*(N-1-upto)] -= dig*dig;    
    
    for (int i=0; i<upto; i++) {
        squared[i+upto] -= 2*tosquare[i]*tosquare[upto];
        squared[N-1-i+upto] -= 2*tosquare[N-1-i]*tosquare[upto];
        
        if (N-1-upto!=upto) {
            squared[i+N-1-upto] -= 2*tosquare[i]*tosquare[N-1-upto];
            squared[N-1-i+N-1-upto] -= 2*tosquare[N-1-i]*tosquare[N-1-upto];
        }
    }    
    tosquare[upto] = tosquare[N-1-upto] = 0;
}
vector<string> answers;
void go(int N, int upto) {
    if (upto==(N+1)/2) {
        int end = 2*N-1;
        while (squared[end]==0) end--;        
        bool pal = true;
        for (int i=0; i+i<end; i++) if (squared[i]!=squared[end-i]) {pal=false;break;}
        if (!pal) return;
        
        string ans = "";
        
        for (int i=0; i<=end; i++) ans += ('0'+squared[i]);
        
        int len = end+1;
        while (len<100) {len++;ans="0"+ans;}
        answers.push_back(ans);
        found++;      
        return;
    }
    
    if (upto) {
        put(N,upto,0);
    }
    put(N,upto,1);
    if (2*upto+1==N || upto==0) {        
        put(N,upto,2);
    }    
    if (N==1) {
        put(N,upto,3);
    }
    
}

int main() {
    // 1 digit: 1, 4, 9    
    for (int N=1; N<=50; N++) {
        found = 0;
        for (int i=0; i<2*N; i++) squared[i]=0;        
        go(N,0);
        
        /*
        if (N>1) {
            string twos = "2";
            for (int i=0; i<N-2; i++) twos += "0";
            twos += "2";
            answers.push_back(twos);            
            if (N%2==1) {
                twos[(N-1)/2]='1';
                answers.push_back(twos);                            
            }
        }
        */
    }
    int T; cin >> T; for (int t=1; t<=T; t++) {
        string A,B; cin >> A >> B;
        while (A.length()<100) A = "0"+A;
        while (B.length()<100) B = "0"+B;        
        
        int ret = 0;
        for (vector<string>::iterator it = answers.begin(); it!=answers.end(); it++) {
            string s = (*it);
            if (s > B) {
                break;
            }
            if (s < A) {
                continue;
            }
            ret++;
        }
        printf("Case #%d: %d\n",t,ret);
    }
}
