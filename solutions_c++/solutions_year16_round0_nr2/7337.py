/****************************************************************
*    sonu kumar
*    MNNIT allahabad
*    computer science and engineering
****************************************************************/
#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(i) push_back(i)
#define mp(i,j) make_pair(i,j)
#define line printf("\n")
#define space printf(" ")
#define sci(i) scanf("%d",&i)
#define scl(i) scanf("%lld",&i)
#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
using namespace std;
int main()
{
    int t;
    sci(t);
    cin.ignore();
    for(int sonu=1;sonu<=t;sonu++)
    {
        vector<int>arr;
        char str[1000];
        scanf("%s",str);
        int len=strlen(str);
        int i=0,indt=-1;
        while(i<len)
        {
            if(str[i]=='+')
                {
                    arr.pb(1);
                    while(str[i]=='+'&&i<len)
                        i++;
                }
                if(str[i]=='-')
                {
                    arr.pb(2);
                    while(str[i]=='-'&&i<len)
                        i++;
                }
        }
        int s=arr.size();
        for(int i=0;i<s;i++)
        {
        if(arr[i]==2)
        indt=i;
        }
        int ans=0;
        //chk(s),chk(indt);
        for(int i=0;i<=indt;i++)
        {
            if(i==indt)
                ans++;
            else
            {
                if(arr[i]==1&&arr[i+1]==2)
                    ans++;
                if(arr[i]==2&&arr[i+1]==1)
                    ans+=2;
                arr[i+1]=2;
            }
        }
        printf("Case #%d: %d\n",sonu,ans);
    }
    return 0;
}
