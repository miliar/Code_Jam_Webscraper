///HH_ace
#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef pair<long long int, long long int> PLL;
typedef vector<long long int> VL;

#define sdd(y) scanf("%lld", &y)
#define sd(x)  scanf("%d", &x)
#define F first
#define S second
#define pb push_back
#define MOD 1000000007

int a[500005];
int b[500005];
map<string,int> mp;
int main()
{
freopen("at.in","r",stdin);
freopen("at.out","w",stdout);
// ios_base::sync_with_stdio(false);

string zz[5]={"ZERO", "TWO", "FOUR", "SIX","EIGHT"};
string zz2[4]={ "THREE", "FIVE", "NINE" , "SEVEN"};
mp["ZERO"]=0;
mp["ONE"]=1;
mp["TWO"]=2;
mp["THREE"]=3;
mp["FOUR"]=4;

mp["FIVE"]=5;
mp["SIX"]=6;
mp["SEVEN"]=7;
mp["EIGHT"]=8;
mp["NINE"]=9;
int t;
sd(t);
for(int cs=1;cs<=t;cs++){

string s;

cin>>s;

int a[26];
int ans[10];
for(int i=0;i<26;i++)
        a[i]=0;

for(int i=0;i<10;i++)
        ans[i]=0;

int l=s.size();
for(int i=0;i<l;i++)
    ++a[s[i]-'A'];


//for(int i=0;i<10;i++)
  //  cout<<zz[i]<<endl;

/*
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER


*/


for(int i=0;i<5;i++){
string st=zz[i];
int lt=st.size();
int f=0;
int j;
while(1){

    for(j=0;j<lt;j++){
        if(!a[st[j]-'A'])
            f=1;


    }
    if(f)break;
    for(j=0;j<lt;j++){
            a[st[j]-'A']--;
    }
    ans[mp[st]]++;



}



}

for(int i=0;i<4;i++){
string st=zz2[i];
int lt=st.size();
int f=0;
int j;
while(1){

    for(j=0;j<lt;j++){
        if(!a[st[j]-'A'])
            f=1;


    }
    if(f)break;
    for(j=0;j<lt;j++){
            a[st[j]-'A']--;
    }
    ans[mp[st]]++;



}



}



int t=a['O'-'A'];
ans[1]=t;


cout<<"Case #"<<cs<<": ";
for(int i=0;i<10;i++)
{
    if(ans[i])
    {
        while(ans[i]--)
        {
            cout<<i;

        }

    }

}
cout<<endl;



}



return 0;
}
