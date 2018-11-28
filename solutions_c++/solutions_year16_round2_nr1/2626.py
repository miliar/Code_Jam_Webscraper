//Coded by: speeDemon/thunderclash
#include<bits/stdc++.h>
#define MOD 1000000007
#define dbg(x)
using namespace std;
typedef long long ll;

ll cnt[10];
ll alp[255];
bool used[2001];

int main()
{
    freopen("Alarge.in","r",stdin);
    freopen("As.txt","w",stdout);
    ll t,tinit;
    char s[2001];
    ll i;
    cin>>t;
    tinit = t;
    while(t--)
    {
        getchar();
        scanf("%s",s);
        for(i=0;i<=9;++i)
            cnt[i] = 0;
        for(i='A';i<='Z';++i)
            alp[i] = 0;
        for(i=0;i<=2000;++i)
            used[i] = false;

        for(i=0;s[i]!='\0';++i)
        {
            if(used[i] == false && alp[s[i]]>0){
                --alp[s[i]];
                used[i] = true;
            }
            else if(used[i] == false)
            {
                switch(s[i])
                {
                case 'Z':
                    cnt[0]++;
                    used[i] = true;
                    alp['E']++;alp['R']++;alp['O']++;
                    break;
                case 'W':
                    cnt[2]++;
                    used[i] = true;
                    alp['T']++;alp['O']++;
                    break;

                case 'U':
                    cnt[4]++;
                    used[i] = true;
                    alp['F']++;alp['O']++;alp['R']++;
                    break;
                case 'X':
                    cnt[6]++;
                    used[i] = true;
                    alp['S']++;alp['I']++;
                    break;
                case 'G':
                    cnt[8]++;
                    used[i] = true;
                    alp['E']++;alp['I']++;alp['H']++;alp['T']++;
                    break;
                }
            }
        }
        for(i=0;s[i]!='\0';++i){
            if(used[i] == false && alp[s[i]]>0){
                --alp[s[i]];
                used[i] = true;
            }
        }

        for(i=0;s[i]!='\0';++i)
        {
            if(used[i] == false && alp[s[i]]>0){
                --alp[s[i]];
                used[i] = true;
            }
            else if(used[i] == false)
            {
                switch(s[i])
                {
                    case 'H':
                    cnt[3]++;
                    used[i] = true;
                    alp['T']++;alp['R']++;alp['E']++;alp['E']++;
                    break;
                case 'O':
                    cnt[1]++;
                    used[i] = true;
                    alp['N']++;alp['E']++;
                    break;
                case 'S':
                    cnt[7]++;
                    used[i] = true;
                    alp['E']++;alp['V']++;alp['E']++;alp['N']++;
                    break;
                 }
            }
        }
        for(i=0;s[i]!='\0';++i){
            if(used[i] == false && alp[s[i]]>0){
                --alp[s[i]];
                used[i] = true;
            }
        }
        for(i=0;s[i]!='\0';++i)
        {
            if(used[i] == false && alp[s[i]]>0){
                --alp[s[i]];
                used[i] = true;
            }
            else if(used[i] == false)
            {
                switch(s[i])
                {
                case 'F':
                    cnt[5]++;
                    used[i] = true;
                    alp['I']++;alp['V']++;alp['E']++;
                    break;
                case 'N':
                    cnt[9]++;
                    used[i] = true;
                    alp['I']++;alp['N']++;alp['E']++;
                    break;
                 }
            }
        }
        printf("Case #%lld: ",tinit-t);
        for(i=0;i<=9;++i)
        {
            while(cnt[i]){
                printf("%d",i);
                --cnt[i];
            }
        }

        printf("\n");


    }
    return 0;
}
