#include <iostream>
#include<stdio.h>
#include<string.h>
#include<map>
using namespace std;
char s[2001];
map<int, string> m;
int cnt[91],cnt2[91],ans[10];
int main()
{
    freopen("input3.in","r",stdin);
    freopen("output4.txt","w",stdout);
    //for(int i=0; i<=9; i++)
    //{
        m[0]="ZERO";
        m[1]="ONE";
        m[2]="TWO";
        m[3]="THREE";
        m[4]="FOUR";
        m[5]="FIVE";
        m[6]="SIX";
        m[7]="SEVEN";
        m[8]="EIGHT";
        m[9]="NINE";
    //printf("%d",m[0].length());
    //}
    int t;
    scanf("%d",&t);
    int c=1;
    while(t--)
    {
        //q=0;
        printf("Case #%d: ",c);
        c++;
        scanf("%s",s);
        for(int i=0; i<=9; i++) ans[i]=0;
        for(int i=65; i<=90; i++)
        {
            cnt[i]=0;
            cnt2[i]=0;
        }
        int l=strlen(s);
        for(int i=0; i<l; i++)
        {
            cnt[s[i]]++;
            cnt2[s[i]]++;
        }
        int v;
        for(int i=0; i<l; i++)
        {
            if(s[i]=='W'&&cnt[s[i]]>0)
            {
                cnt['T']--;
                cnt['W']--;
                cnt['O']--;
                ans[2]++;
            }
            else if(s[i]=='U'&&cnt[s[i]]>0)
            {
                cnt['F']--;
                cnt['O']--;
                cnt['U']--;
                cnt['R']--;
                ans[4]++;
            }
            else if(s[i]=='X'&&cnt[s[i]]>0)
            {
                cnt['S']--;
                cnt['I']--;
                cnt['X']--;
                ans[6]++;
            }
            else if(s[i]=='G'&&cnt[s[i]]>0)
            {
                cnt['E']--;
                cnt['I']--;
                cnt['G']--;
                cnt['H']--;
                cnt['T']--;
                ans[8]++;
            }
        }
        for(int i=65; i<=90; i++) cnt2[i]=cnt[i];
        for(int i=0; i<=9; i++)
        {
            if(i==2||i==4||i==6||i==8) continue;
            //printf("%d ",i);
            v=0;
            string x=m[i];
           // cout<<cnt[x[0]];
            ab:
            for(int j=0; j<x.length(); j++)
            {
                //cout<<"lol";
                if(cnt[x[j]]>0)
                    cnt[x[j]]--;
                else
                {
                    v=-1;
                    break;
                    //goto ab;
                }
            }
            if(v==0)
            {
                for(int k=65; k<=90; k++) cnt2[k]=cnt[k];
                ans[i]++;
                goto ab;
            }
            else
            {
                for(int k=65; k<=90; k++) cnt[k]=cnt2[k];
            }
            //else v=0;
        }
        for(int i=0; i<=9; i++)
        {
            while(ans[i]--) printf("%d",i);
        }
        printf("\n");

    }
    return 0;
}
