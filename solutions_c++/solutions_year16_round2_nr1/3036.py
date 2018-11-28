#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int t;
    char num[10][6]={"ZERO",  "TWO",  "FOUR",  "SIX", "SEVEN", "EIGHT","FIVE","THREE","ONE", "NINE"};
    int nl[10]={4,3,4,3,5,5,4,5,3,4};
    char s[2010];
    int vl[10]={0,2,4,6,7,8,5,3,1,9};
    int p=1;
    multiset<int> ms;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int l=strlen(s);
        int tl=l;
        for(int i=0;i<10;i++)
        {
            //cout<<"A";
            int fl[5]={0};
            do{
            for(int k=0;k<nl[i];k++)
            {
                for(int j=0;j<l;j++)
                {
                    if(s[j]==num[i][k])
                    {
                        fl[k]=1;
                        s[j]+=32;
                        break;
                    }
                }
            }
            for(int k=0;k<nl[i];k++)
            {
                if(fl[k]==0)
                    goto e1;
            }
            ms.insert(vl[i]);
            for(int k=0;k<nl[i];k++)
                for(int j=0;j<l;j++)
                if(s[j]==num[i][k]+32)
            {
                s[j]='0';
                //fl[k]=0;
                break;
            }
            //cout<<"B";
            for(int k=0;k<5;k++)
                fl[k]=0;
            //cout<<s<<"\n";
            }while(1);
            e1:
            for(int j=0;j<l;j++)
            if(s[j]>=97)
            s[j]-=32;
        }
        printf("Case #%d: ",p);
        for(multiset<int>::iterator i=ms.begin();i!=ms.end();i++)
            printf("%d",*i);
        printf("\n");
        ms.clear();
        p++;
    }
}
