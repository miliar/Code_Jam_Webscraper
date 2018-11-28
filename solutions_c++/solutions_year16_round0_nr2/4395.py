#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.o", "w", stdout);
    int t,l,i,j,a,k;
    long long cnt=0;
    string s;
    scanf("%d",&t);
    getchar();
    for(int ca=1; ca<=t; ca++)
    {
        cin >> s;
        l=s.size();
        cnt=0;
        a=l-1;
        int ck=1;
        while(ck!=0)
        {
            ck=0;
            for(i=a; i>=0; i--)
            {
                if(s[i]=='-')
                {
                    if(s[0]!='-')
                    {
                        cnt++;
                        k=0;
                        while(s[k++]!='-') s[k-1]='-';
                    }
                    cnt++;
                    reverse(s.begin(),s.begin()+i+1);
                    for(j=0; j<=i; j++)
                    {
                        if(s[j]=='+') s[j]='-';
                        else s[j]='+';
                    }
                    ck=1;
                    break;
                }
            }
            if(ck) a=i;
            else a=i-1;
        }
        printf("Case #%d: %lld\n",ca,cnt);
    }


}
