#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef vector <int> vi;
typedef vector <long long> vill;

#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfll(a) printf("%I64d\n",a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb(a) push_back(a)
#define fore(i,a,b) for(i=a;i<=b;i++)

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n,k,i,t,j,m,m1,cnt,indx,fa;
    sc(t);
    string str;
    vector<char> a;

    fore(k,1,t){
        cin>>str;
        a.resize(0);
        if(str=="+"){
            printf("case #%d: 0\n",k);
            continue;
        }else if(str=="-"){
            printf("case #%d: 1\n",k);
            continue;
        }
        a.pb(str[0]);
        fore(i,1,str.length()-1){
            if(a[a.size()-1]!=str[i]){
                a.pb(str[i]);
            }
        }
        fa=0;
        if(a.size()==1){
            if(a[0]=='-'){
                printf("case #%d: 1\n",k);
                continue;
            }else{
                printf("case #%d: 0\n",k);
                continue;

            }

        }

        fore(i,0,a.size()-2){
            if(a[i]=='+'){
                fa=fa+2;
                i++;
            }else{
                fa=fa+1;
            }
        }
        printf("case #%d: ",k);
        pf(fa);
    }
    return 0;
}
