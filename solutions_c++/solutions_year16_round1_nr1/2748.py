#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define inf 10000000000000
char str[1009];
int main()
{   
    int i,t;
    scanf("%d",&t);
    int y=t;
    while(t--)
    {
        scanf("%s",str);
        int n=strlen(str);
        string s="";
        s=s+str[0];
        for(i=1;i<n;i++)
        {
            if(str[i]>=s[0])
            s=str[i]+s;
            else
            s=s+str[i];
        }
        printf("Case #%d: ",y-t);
        cout<<s;
        printf("\n");
    }
    return 0;
}