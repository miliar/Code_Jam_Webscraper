#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; cin>>t; while(t--)
#define fr freopen("in.txt", "r", stdin)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf


using namespace std;

string num[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int x[10][26];

void preprocess(void)
{
    memset(x, 0, sizeof(x));
    for(int i=0; i<10; i++)
        for(int j=0; j<num[i].length(); j++)
            x[i][num[i][j]-'A']++;
}

bool isf(int i, int alp[26])
{
    for(int j=0; j<26; j++)
        if(x[i][j]>alp[j])
            return 0;
    return 1;
}

string ans;
bool ansf=0;
void solve(int i, int alp[26], string res)
{
    //for(int i=0; i<26; i++) cout<<alp[i]<<' ';cout<<endl;
    if(ansf)
        return;
    bool flag=1;
    for(int j=0; j<26; j++){
        if(alp[j]!=0)
            flag=0;
        if(alp[j]<0)
            return;
    }
    if(i<0)
        return ;
    if(flag==1){
        ans=res;
        ansf=1;
      // cout<<"Ans found";
        return ;
    }
    flag=isf(i, alp);
    if(flag)
    {
        solve(i-1, alp, res);
        for(int j=0; j<26; j++)
            alp[j]-=x[i][j];
        res+=char('0'+i);
        solve(i, alp, res);
        solve(i-1, alp, res);
        for(int j=0; j<26; j++) alp[j]+=x[i][j];
    }
    else
    {
        solve(i-1, alp, res);
    }
}

int main()
{
    freopen("out.txt","w", stdout);
    preprocess();
    fr;
    int cs=1;
    cst{
        ansf=0;
        string s;
        cin>>s;
        //cout<<s.length();
        int alp[26];
        memset(alp, 0, sizeof(alp));
        for(int i=0; i<s.length(); i++)
            alp[s[i]-'A']++;
       // for(int i=0; i<26; i++) cout<<alp[i]<<' ';cout<<endl;
      // cout<<s<<endl;
        solve(9, alp, "");
       /* if(ansf==0)
            cout<<s<<endl;*/
        cout<<"Case #"<<cs++<<": ";//<<ans<<endl;
        for(int j=ans.length()-1; j>=0; j--)
            cout<<ans[j];
        cout<<endl;
    }
    return 0;
}




