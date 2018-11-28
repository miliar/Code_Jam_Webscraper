#include <bits/stdc++.h>
#define GCJ 1
using namespace std;

string s;
map <char,int> m;
map <int,int> nm;
string mc[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

void clearmem(){
    for (int i=0;i<=9;i++)
        nm[i] = 0;
    for (char ch = 'A';ch<='Z';ch++){
        m[ch] = 0;
    }
}
void delnum(int numtodel,int am){
    for (int i=0;mc[numtodel][i];i++){
        m[mc[numtodel][i]] -= am;
    }
}
void solve(){
    cin >> s;
    for (int i=0;s[i];i++)
        m[s[i]]++;
    int tn;
    tn = m['Z'];
    delnum(0,tn);
    nm[0] = tn;
    tn = m['W'];
    delnum(2,tn);
    nm[2] = tn;
    tn = m['U'];
    delnum(4,tn);
    nm[4] = tn;
    tn = m['X'];
    delnum(6,tn);
    nm[6] = tn;
    tn = m['S'];
    delnum(7,tn);
    nm[7] = tn;
    tn = m['G'];
    delnum(8,tn);
    nm[8] = tn;
    tn = m['H'];
    delnum(3,tn);
    nm[3] = tn;
    tn = m['O'];
    delnum(1,tn);
    nm[1] = tn;
    tn = m['V'];
    delnum(5,tn);
    nm[5] = tn;
    tn = m['I'];
    delnum(9,tn);
    nm[9] = tn;
    for (int i=0;i<=9;i++){
        for (int j=0;j<nm[i];j++)
            printf ("%d",i);
    }
    printf ("\n");
}

int main(){
    int TC;
    if (GCJ){
        freopen ("A-large.in","r",stdin);
        freopen ("A-large.out","w",stdout);
    }
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        clearmem();
        solve();
    }
return 0;
}
