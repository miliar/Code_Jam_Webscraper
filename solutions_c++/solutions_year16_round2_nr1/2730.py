#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
int T;
char s[3000];
int kase = 1;
int m[300];
int M[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        cin>>s;
        printf("Case #%d: ",kase++);
        int l =strlen(s);
        memset(m,0,sizeof(m));
        memset(M,0,sizeof(M));
        for(int i=0;i<l;i++)
        {
            m[s[i]]++;
        }
        if(m['Z']!=0)
        {
            int t = m['Z'];
            for(int i=0;i<t;i++)
            {
                m['Z']--;
                m['E']--;
                m['R']--;
                m['O']--;
                M[0]++;
            }
        }
        if(m['X']!=0)
        {
            int t = m['X'];
            for(int i=0;i<t;i++)
            {
                m['X']--;
                m['I']--;
                m['S']--;
                M[6]++;
            }
        }
        if(m['S']!=0)
        {
            int t = m['S'];
            for(int i=0;i<t;i++)
            {
                m['S']--;
                m['E']--;
                m['V']--;
                m['E']--;
                m['N']--;
                M[7]++;
            }
        }
        if(m['V']!=0)
        {
            int t = m['V'];
            for(int i=0;i<t;i++)
            {
                m['F']--;
                m['I']--;
                m['V']--;
                m['E']--;
                M[5]++;
            }
        }
        if(m['F']!=0)
        {
            int t = m['F'];
            for(int i=0;i<t;i++)
            {
                m['F']--;
                m['O']--;
                m['U']--;
                m['R']--;
                M[4]++;
            }
        }
        if(m['R']!=0)
        {

            int t = m['R'];
            for(int i=0;i<t;i++)
            {
                m['R']--;
                m['T']--;
                m['H']--;
                m['E']-=2;
                M[3]++;
            }
        }
        if(m['H']!=0)
        {
            int t = m['H'];
            for(int i=0;i<t;i++)
            {
                m['E']--;
                m['I']--;
                m['G']--;
                m['H']--;
                m['T']--;
                M[8]++;
            }
        }
        if(m['T']!=0)
        {
            int t = m['T'];
            for(int i=0;i<t;i++)
            {
                m['T']--;
                m['W']--;
                m['O']--;
                M[2]++;
            }
        }
        if(m['I']!=0)
        {
            int t = m['I'];
            for(int i=0;i<t;i++)
            {
                m['N']--;
                m['I']--;
                m['N']--;
                m['E']--;
                M[9]++;
            }
        }
        if(m['O']!=0)
        {
            int t = m['O'];
            for(int i=0;i<t;i++)
            {
                m['O']--;
                m['N']--;
                m['E']--;
                M[1]++;
            }
        }
        for(int i=0;i<10;i++)
        {
            if(M[i]>0)
            {
                for(int j=0;j<M[i];j++)
                {
                    printf("%d",i);
                }
            }

        }
        printf("\n");
    }
    return 0;
}
