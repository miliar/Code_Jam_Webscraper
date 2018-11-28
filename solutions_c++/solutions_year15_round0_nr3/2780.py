#include<iostream>
#include<vector>
#include<cstdio>
#include<cstring>
using namespace std;
vector<int> v;
char mat[5][5]={"hijk","ihkj","jkhi","kjih"};
int mat2[4][4]={0,0,0,0,
                0,1,0,1,
                0,1,1,0,
                0,0,1,1};
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,ca,ans,n,p,m,ind,x,l,signi,signj,signk,flag,j,k;
    char tempi,temp2,tempj,tempk;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
    {
        char s[10010],s1[10010];
        scanf("%d %d\n",&l,&x);
        scanf("%s",&s);
        strcpy(s1,s);
        for(i=1;i<x;i++)
        {
            strcat(s,s1);
        }
        s[l*x]='\0';
        l=strlen(s);
        flag=0;
        for(i=0;i<=l-3;i++)
        {
            if(!i)
            {
                signi=0;
                tempi=s[i];
            }
            if(tempi=='i' && signi==0)
            {
                for(j=i+1;j<=l-2;j++)
                {
                    if(j==i+1)
                     {
                         signj=0;
                         tempj=s[j];
                     }
                    if(tempj=='j' && signj==0)
                    {
                        if(flag)
                         break;
                        k=j+1;
                        if(k==j+1)
                        {
                            signk=0;
                            tempk=s[k];
                        }
                        while(k<(l-1))
                        {
                            temp2=s[k+1];
                            signk=signk^mat2[tempk-'h'][temp2-'h'];
                            tempk=mat[tempk-'h'][temp2-'h'];
                            k++;
                        }
                        if(tempk=='k' && signk==0)
                        {
                            flag=1;
                            break;
                        }
                    }
                    if(flag)
                     break;
                    temp2=s[j+1];
                    signj=signj^mat2[tempj-'h'][temp2-'h'];
                    tempj=mat[tempj-'h'][temp2-'h'];
                }
            }
            if(flag)
              break;
            temp2=s[i+1];
            signi=signi^mat2[tempi-'h'][temp2-'h'];
            tempi=mat[tempi-'h'][temp2-'h'];
        }
        if(flag)
        printf("Case #%d: YES\n",ca);
        else
        printf("Case #%d: NO\n",ca);
    }
    return 0;
}
