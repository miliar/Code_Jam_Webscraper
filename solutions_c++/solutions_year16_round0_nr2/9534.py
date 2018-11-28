#include <bits/stdc++.h>

using namespace std;
void revv(char arr[], int start, int end)
{
    int temp;
    while (start < end)
    {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
void rev(char arr[], int start, int end)
{
    char temp;
    revv(arr,start,end);
    for(int i=0; i<=end; i++)
    {
        if(arr[i]=='+')arr[i]='-';
        else if(arr[i]=='-')arr[i]='+';
    }
}
int check (char a[],int ln)
{
    int p=0;
    for(int i=0; i<ln; i++)
    {
        if(a[i]=='+')p++;
    }
    if(p==ln)return 1;
    else return 0;

}
int ch(char a[],int ln)
{
    int p=0;
    for(int i=0; i<ln; i++)
    {
        if(a[i]=='-')p++;
    }
    if(p==ln)return 1;
    else return 0;

}
int main()
{
    int t,l=1,st,en;
    char a[200];
    freopen("tk.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d\n",&t);
    while(t--)
    {
        memset(&a,0,sizeof(a));
        gets(a);
        int ln=strlen(a);
        int i=-1,p=0,rou=0,cnt=0;
        while(1)
        {
            if(rou==1)
            {
                i=0;
                rou=0;
            }
            else i++;
            if(ch(a,ln))
            {
                cnt++;
                break;
            }
            if(check(a,ln))
            {
                break;
            }
            if(a[i]!=a[i+1])
            {
                if(a[i+1]=='+')p=0;
                else if(a[i+1]=='-')p=1;
                if(p==0&&a[i+1]=='+')
                {
                    rev(a,0,i);
                    p=1;
                    rou=1;
                    cnt++;
                    continue;
                }
                else if(p==1&&a[i+1]=='-')
                {
                    rev(a,0,i);
                    p=0;
                    rou=1;
                    cnt++;
                    continue;
                }
            }


        }
        printf("Case #%d: %d\n",l++,cnt);

    }

    return 0;
}
