#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define ii pair<int,int>
#define vi vector<int>
#define _(A,v) memset(A,v,sizeof(A))
#define all(A) (A).begin(),(A).end()
#define forn(i,n)for(int i=0;i<n;i++)
#define foreach(it,A) for(__typeof((A).begin())it=(A).begin();it!=(A).end();it++)
#define endl '\n'
#define dbg(xD) cerr<<" >"<<__LINE__<<": "<<#xD<<" = "<<xD<<endl
#define fast_io ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

int alpha[100],n;
char S[2001];

string solve(){
    string ans="";
    _(alpha,0);
    n=strlen(S);
    int sum=0;
    forn(i,n)alpha[S[i]]++;
    if(alpha['Z']){
        while(true){
            if(alpha['Z'] and alpha['E'] and alpha['R'] and alpha['O'])
                ans+='0',alpha['Z']--,alpha['E']--,alpha['R']--,alpha['O']--,sum+=4;
            else break;
        }
    }
    if(alpha['W']){
        while(true){
            if(alpha['T'] and alpha['W'] and alpha['O'])
                ans+='2',alpha['T']--,alpha['W']--,alpha['O']--,sum+=3;
            else break;
        }
    }
    if(alpha['U']){
        while(true){
            if(alpha['F'] and alpha['O'] and alpha['U'] and alpha['R'])
                ans+='4',alpha['F']--,alpha['O']--,alpha['U']--,alpha['R']--,sum+=4;
            else break;
        }
    }
    if(alpha['X']){
        while(true){
            if(alpha['S'] and alpha['I'] and alpha['X'])
                ans+='6',alpha['S']--,alpha['I']--,alpha['X']--,sum+=3;
            else break;
        }      
    }
    if(alpha['G']){
        while(true){
            if(alpha['E'] and alpha['I'] and alpha['G'] and alpha['H'] and alpha['T'])
                ans+='8',alpha['E']--,alpha['I']--,alpha['G']--,alpha['H']--,alpha['T']--,sum+=5;
            else break;
        }
    }
    if(alpha['F']){
        while(true){
            if(alpha['F'] and alpha['I'] and alpha['V'] and alpha['E'])
                ans+='5',alpha['F']--,alpha['I']--,alpha['V']--,alpha['E']--,sum+=4;
            else break;
        }
    }
    while(true){
        if(alpha['T'] and alpha['H'] and alpha['R'] and alpha['E']>=2)
            ans+='3',alpha['T']--,alpha['H']--,alpha['R']--,alpha['E']-=2,sum+=5;
        else break;
    }
    while(true){
        if(alpha['S'] and alpha['E']>=2 and alpha['V'] and alpha['N'])
            ans+='7',alpha['S']--,alpha['E']-=2,alpha['V']--,alpha['N']--,sum+=5;
        else break;
    }
    while(true){
        if(alpha['N']>=2 and alpha['I'] and alpha['E'])
            ans+='9',alpha['N']-=2,alpha['I']--,alpha['E']--,sum+=4;
        else break;
    }
    while(true){
        if(alpha['O'] and alpha['N'] and alpha['E'])
            ans+='1',alpha['O']--,alpha['N']--,alpha['E']--,sum+=3;
        else break;
    }
    sort(all(ans));
    return ans;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tc,n;
    scanf("%d",&tc);
    for(int caseNo=1;caseNo<=tc;caseNo++){
        scanf("%s",S);
        printf("Case #%d: ",caseNo);
        printf("%s\n",solve().c_str());
    }
    return 0;
}