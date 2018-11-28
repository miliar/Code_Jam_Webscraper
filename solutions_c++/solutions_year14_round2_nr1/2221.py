#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define MOD 1000000009


template <typename X> X gcd(X a, X b){if(!b)return a; else return gcd(b, a%b);}
int main()
{
freopen("C:/Users/UMANG JALAN/Desktop/CODE/inp.txt","r",stdin);
freopen("C:/Users/UMANG JALAN/Desktop/CODE/out.txt","w",stdout);
int t,n;
int z=1;
scanf("%d",&t);
while(t--)
{
    scanf("%d",&n);
    string str[n+1];
    for(int i=0;i<n;i++) cin>>str[i];
    int a[27]={0};int b[27]={0};
    for(int i=0;i<str[0].length();i++) a[str[0][i]-'a']++;
     for(int i=0;i<str[1].length();i++) b[str[1][i]-'a']++;
     bool flag=false;
     for(int i=0;i<26;i++){
            if(a[i]==0 && b[i] || (a[i] && b[i]==0)) {flag=true; break;}
        }
        int cnt=0;
    if(flag==false)
    {
        int i=0,j=0;
        while(flag==false && str[0][i]!='\0' && str[1][j]!='\0')
        {
            if(str[0][i]==str[1][j]) {i++;j++;continue;}
            else {
                if(str[0][i-1]==str[0][i]) {str[0].erase(str[0].begin()+i); cnt++;}
                else if(str[1][j-1]==str[1][j]) {str[1].erase(str[1].begin()+j); cnt++;}
                else flag=true;
            }
        }
        if(str[0][i]=='\0' && str[1][j]!='\0')
        {
            while(str[1][j]!='\0' && flag==false) {
                if(str[1][j]==str[1][j-1]) {j++;cnt++;continue;}
                else flag=true;
            }
        }
        else if(str[0][i]!='\0' && str[1][j]=='\0')
        {
            while(str[0][i]!='\0' && flag==false) {
                if(str[0][i]==str[0][i-1]) {i++;cnt++;continue;}
                else flag=true;
            }
        }
    }
    if(flag) printf("Case #%d: Fegla Won\n",z);
    else printf("Case #%d: %d\n",z,cnt);z++;
}
}
