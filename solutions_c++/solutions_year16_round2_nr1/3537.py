#include<stdio.h>
#include<string.h>
struct node
{
    int val[150];
};
int ans[15];
bool c(node x)
{
    int i;
    for(i='A';i<='Z';i++) if(x.val[i]!=0) return false;
    return true;
}
bool print(node x)
{
    int i,j;
    bool check;
    node t;
    if(c(x))
    {
        for(i=0;i<10;i++)
        {
            for(j=0;j<ans[i];j++) printf("%d",i);
        }
        return true;
    }
    else
    {
        if(x.val['Z']&&x.val['E']&&x.val['R']&&x.val['O'])
        {
            t = x;
            t.val['Z']--;
            t.val['E']--;
            t.val['R']--;
            t.val['O']--;
            ans[0]++;
            check = print(t);
            ans[0]--;
            if(check) return true;
        }
        if(x.val['O']&&x.val['N']&&x.val['E'])
        {
            t = x;
            t.val['O']--;
            t.val['N']--;
            t.val['E']--;
            ans[1]++;
            check = print(t);
            ans[1]--;
            if(check) return true;
        }
        if(x.val['T']&&x.val['W']&&x.val['O'])
        {
            t = x;
            t.val['T']--;
            t.val['W']--;
            t.val['O']--;
            ans[2]++;
            check = print(t);
            ans[2]--;
            if(check) return true;
        }
        if(x.val['T']&&x.val['H']&&x.val['R']&&x.val['E']>1)
        {
            t = x;
            t.val['T']--;
            t.val['H']--;
            t.val['R']--;
            t.val['E']-=2;
            ans[3]++;
            check = print(t);
            ans[3]--;
            if(check) return true;
        }
        if(x.val['F']&&x.val['O']&&x.val['U']&&x.val['R'])
        {
            t = x;
            t.val['F']--;
            t.val['O']--;
            t.val['U']--;
            t.val['R']--;
            ans[4]++;
            check = print(t);
            ans[4]--;
            if(check) return true;
        }
        if(x.val['F']&&x.val['I']&&x.val['V']&&x.val['E'])
        {
            t = x;
            t.val['F']--;
            t.val['I']--;
            t.val['V']--;
            t.val['E']--;
            ans[5]++;
            check = print(t);
            ans[5]--;
            if(check) return true;
        }
        if(x.val['S']&&x.val['I']&&x.val['X'])
        {
            t = x;
            t.val['S']--;
            t.val['I']--;
            t.val['X']--;
            ans[6]++;
            check = print(t);
            ans[6]--;
            if(check) return true;
        }
        if(x.val['S']&&x.val['E']>1&&x.val['V']&&x.val['N'])
        {
            t = x;
            t.val['S']--;
            t.val['E']-=2;
            t.val['V']--;
            t.val['N']--;
            ans[7]++;
            check = print(t);
            ans[7]--;
            if(check) return true;
        }
        if(x.val['E']&&x.val['I']&&x.val['G']&&x.val['H']&&x.val['T'])
        {
            t = x;
            t.val['E']--;
            t.val['I']--;
            t.val['G']--;
            t.val['H']--;
            t.val['T']--;
            ans[8]++;
            check = print(t);
            ans[8]--;
            if(check) return true;
        }
        if(x.val['N']>1&&x.val['I']&&x.val['E'])
        {
            t = x;
            t.val['N']-=2;
            t.val['I']--;
            t.val['E']--;
            ans[9]++;
            check = print(t);
            ans[9]--;
            if(check) return true;
        }
        return false;
    }
}
main()
{
    int time;
    int i,num = 1;
    char s[2005];
    node p;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("digit_out1.txt","w",stdout);
    scanf("%d",&time);
    while(time--)
    {
        scanf(" %s",s);
        for(i='A';i<='Z';i++) p.val[i] = 0;
        for(i=0;i<10;i++) ans[i] = 0;
        for(i=0;i<strlen(s);i++)
        {
            p.val[s[i]]++;
        }
        printf("Case #%d: ",num++);
        print(p);
        printf("\n");
    }
}
