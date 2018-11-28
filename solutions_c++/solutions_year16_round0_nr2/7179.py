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

int main()
{
freopen("at.txt","r",stdin);
freopen("att.txt","w",stdout);
// ios_base::sync_with_stdio(false);

int t;
sd(t);
for(int ct=1;ct<=t;ct++){
string s;
cin>>s;

int l=s.size();
--l;

int f=0,i,j;
for(i=0;;){

 for(j=l;;){
        if(s[j]=='+' && j==0)
            {f=1;break;}
            else if(s[j]=='-' && j==0)
            {++i;f=1;break;}

        if(s[j]=='+')
            --j;
        else
        {l=j;break;}

    }

    if(f)
    break;


    for(int k=0;k<=j;k++){
        if(s[k]=='-')s[k]='+';
        else s[k]='-';
    }




++i;
}


cout<<"Case #"<<ct<<": "<<i<<endl;




}



return 0;
}
