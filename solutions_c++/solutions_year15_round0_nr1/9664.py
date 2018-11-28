#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    int t;
    scanf("%d",&t);
    int l=1;
    while(t--)
    {
        int s,count=0,ext=-1;
        scanf("%d",&s);
        string str;
        cin>>str;
        for(ll i=0;i<=s;i++){
            if(str[i]=='0'){
                if(ext<i){
                count++;
                ext++;
                }
            }
            else
                ext+=str[i]-'0';
        }
        printf("Case #%d: %d\n",l,count);
        l++;
    }
}
