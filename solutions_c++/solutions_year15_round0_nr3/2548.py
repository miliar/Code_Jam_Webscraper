#include <iostream>

using namespace::std;
int n,k,T;
string s,S;
bool visitedK[10001];
bool visitedJ[10001];
char tabliczka(char a, char b){
    if(a=='1') return b;
    if(b=='1') return a;
    if(a=='i'){
    if(a=='i' && b=='i') return 'm';
    if(a=='i' && b=='j') return 'k';
    if(a=='i' && b=='k') return 'n';
    }
    if(a=='j'){
    if(a=='j' && b=='i') return 'l';
    if(a=='j' && b=='j') return 'm';
    if(a=='j' && b=='k') return 'i';
    }
    if(a=='k'){
    if(a=='k' && b=='i') return 'j';
    if(a=='k' && b=='j') return 'u';
    if(a=='k' && b=='k') return 'm';
    }
    if(a=='u'){
    if(a=='u' && b=='i') return '1';
    if(a=='u' && b=='j') return 'l';
    if(a=='u' && b=='k') return 'j';
    }
    if(a=='n'){
    if(a=='n' && b=='i') return 'k';
    if(a=='n' && b=='j') return '1';
    if(a=='n' && b=='k') return 'u';
    }
    if(a=='l'){
    if(a=='l' && b=='i') return 'n';
    if(a=='l' && b=='j') return 'i';
    if(a=='l' && b=='k') return '1';
    }
    if(a=='m'){
    if(a=='m' && b=='j') return 'n';
    if(a=='m' && b=='k') return 'l';
    if(a=='m' && b=='i') return 'u';
    if(b=='m' && a=='j') return 'n';
    if(b=='m' && a=='k') return 'l';
    if(b=='m' && a=='i') return 'u';
    }

}

char sprawdz(int pocz, int kon){
char last=char(S[pocz]);

if(pocz!=kon)for(int i=pocz+1; i<=kon; i++){
    //cout<<last<<"*"<<S[i]<<"==";
    last=tabliczka(last, S[i]);
   // cout<<last<<endl;
}

return last;
}
bool szukajK(int start){
if(visitedK[start]) return false;
visitedK[start]=true;
if(sprawdz(start, S.size()-1)=='k') return true;
return false;
}


bool szukajJ(int start){
if(visitedJ[start]) return false;
visitedJ[start]=true;
char last=S[start];
if(last=='j') if(szukajK(start+1)==true) return true;
    for(int i=start+1; i<S.size(); i++){
       last=tabliczka(last, S[i]);
       if(last=='j') if(szukajK(i+1)==true) return true;
    }
return false;
}

bool szukajI(int start){
char last=S[start];
if(last=='i') if(szukajJ(start+1)==true) return true;
    for(int i=start+1; i<S.size(); i++){
       last=tabliczka(last, S[i]);
       if(last=='i') if(szukajJ(i+1)==true) return true;
    }
return false;
}


int main(){

cin>>T;

for(int test=1; test<=T; test++){
cin>>n>>k;
cin>>s;
S.clear();
for(int i=0; i<k; i++){
    S+=s;
}
for(int i=0; i<=10000; i++){
    visitedK[i]=false;
    visitedJ[i]=false;
}
if(szukajI(0)==true) cout<<"Case #"<<test<<": YES"<<endl;
else cout<<"Case #"<<test<<": NO"<<endl;
}
return 0;
}
