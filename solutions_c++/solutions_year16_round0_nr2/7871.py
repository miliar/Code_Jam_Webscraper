#include <bits/stdc++.h>
#define pb push_back
#define FOR(i,r) for( long long i=0;i<r;i++)
#define forn(i,n,r) for( long long i=n;i<r;i++)
#define gc getchar_unlocked
#define mod 109546051211
#define ET EXIT_FAILURE
using namespace std;
typedef  long long ll;
typedef unsigned long long ull;
/*  int i=system("{ gcc new.c -o new  ; } 2> error.txt");
    printf("ans %d\n",i);
    system("timeout 2 time  { ./new 1< input.txt 2> output.txt  1 ; }  2> time.txt");
*/
int opo(int x){
    if(x==1) return 2;
    else return 1;
}
ull mulmod(ull val,ull n,ull md)
{
    ull q=((double)val*(double)n/(double)md);
    ull res=val*n-md*q;
    res=(res%md+md)%md;
    return res;
}
ull ipow(ull base, ull exp){
    ull result = 1;
    while (exp){
        if (exp & 1){
            result=mulmod(result,base,mod);
        //    cout <<"result "<<result<<endl;
        }
        exp >>= 1;
        base=mulmod(base,base,mod);
    }
    return result;
}
map <string,int> hash;
map <string,vector <string> >::iterator it;
map <string,vector <string> > data;
map <string,bool> visited;
bool flg=0;
bool dfs(string strt,int team){
    if(visited[strt]==0){
        visited[strt]=1;
       // cout <<"strt "<<strt<<endl;
        for(int i=0;i<data[strt].size();i++){
            if(hash[data[strt][i]]==0){
                hash[data[strt][i]]=opo(team);
                dfs(data[strt][i],opo(team));
            }
            else{
                if(hash[data[strt][i]]!=opo(team)){
                    flg=1;
                    return 1;
                }
                else{
                    dfs(data[strt][i],opo(team));
                }
            }
        }
    }
}
//string s;
string convert(string s,int length){
    string tmp="";
    for(int i=length;i>=0;i--){
        if(s[i]=='+') tmp+='-';
        else tmp+='+';
    }
    for(int i=length+1;i<s.length();i++)
        tmp+=s[i];
    return tmp;
}
int main(){
    ios :: sync_with_stdio(false);
    int t;
    string s;
    cin >>t;
    for(int i=1;i<=t;i++){
        cin >>s;
        int cnt=0;
        while(1){
            int pos=0;
//            char comp=s[0];
            while(pos<s.length() && s[pos]==s[0]) pos++;
//            cout <<"pos "<<pos<<endl;
                if(pos==s.length()){
                    if(s[0]=='-') cout <<"Case #"<<i<<": "<<cnt+1<<'\n';
                    else cout <<"Case #"<<i<<": "<<cnt<<'\n';
                    break;
                }
                else{
                    s=convert(s,pos-1);
                    cnt++;
                }
        }
    }
    return 0;
}
