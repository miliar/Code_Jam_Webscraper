#include<bits/stdc++.h>
using namespace std;

void open(){ freopen("input.txt","r",stdin);
				freopen("output.txt","w",stdout);}

int main()
{
    open();
    long long int T,N;
    scanf("%lld",&T);
    for(int t=1;t<=T;t++)
    {
        string str;
        cin>>str;
        int arr[26]={0};
         int ans[1000];
         int ptr=0;
        int len=str.length();
        for(int i=0;i<len;i++)
            arr[str.at(i)-65]++;
        while(arr['Z'-65]>0)
        {
            ans[ptr]=0;
            ptr++;
            arr['Z'-65]--;
            arr['E'-65]--;
            arr['R'-65]--;
            arr['O'-65]--;
        }
        while(arr['W'-65]>0)
        {
            ans[ptr]=2;
            ptr++;
            arr['T'-65]--;
            arr['W'-65]--;
            arr['O'-65]--;
        }
        while(arr['X'-65]>0)
        {
            ans[ptr]=6;
            ptr++;
            arr['S'-65]--;
            arr['I'-65]--;
            arr['X'-65]--;
        }

        while(arr['G'-65]>0)
        {
            ans[ptr]=8;
            ptr++;
            arr['E'-65]--;
            arr['I'-65]--;
            arr['G'-65]--;
            arr['H'-65]--;
            arr['T'-65]--;
        }

        while(arr['S'-65]>0)
        {
            ans[ptr]=7;
            ptr++;
            arr['S'-65]--;
            arr['E'-65]--;
            arr['V'-65]--;
            arr['E'-65]--;
            arr['N'-65]--;
        }

        while(arr['T'-65]>0)
        {
            ans[ptr]=3;
            ptr++;
            arr['T'-65]--;
            arr['H'-65]--;
            arr['R'-65]--;
            arr['E'-65]--;
            arr['E'-65]--;
        }

        while(arr['R'-65]>0)
        {
            ans[ptr]=4;
            ptr++;
            arr['F'-65]--;
            arr['O'-65]--;
            arr['U'-65]--;
            arr['R'-65]--;
        }

        while(arr['F'-65]>0)
        {
            ans[ptr]=5;
            ptr++;
            arr['F'-65]--;
            arr['I'-65]--;
            arr['V'-65]--;
            arr['E'-65]--;
        }

        while(arr['O'-65]>0)
        {
            ans[ptr]=1;
            ptr++;
            arr['O'-65]--;
            arr['N'-65]--;
            arr['E'-65]--;
        }

        while(arr['N'-65]>0)
        {
            ans[ptr]=9;
            ptr++;
            arr['N'-65]--;
            arr['I'-65]--;
            arr['N'-65]--;
            arr['E'-65]--;
        }
        sort(ans,ans+ptr);
        printf("Case #%d: ",t);
        for(int i=0;i<ptr;i++)
             printf("%d",ans[i]);
        printf("\n");
        //printf("Case #%d: %lld",t,);
    }
    return 0;
}
