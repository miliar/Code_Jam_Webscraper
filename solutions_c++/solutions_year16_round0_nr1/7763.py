#include<stdlib.h>
#include<conio.h>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fin=freopen("A-small.in","r",stdin);
    assert(fin!=NULL);
    FILE *fout=freopen("A-small.out","w",stdout);
    long long int i,j,k,no,cnt,dig,s,tmp,t,p=1;
    long long int c[10];
    scanf("%lld",&t);
                while(p<=t)
                {
                    for(k=0;k<10;k++)
                        c[k]=0;
                    s=2;
                    cnt=0;
                    scanf("%lld",&no);
                        tmp=no;
                    if(no==0)
                    {
                        printf("Case #%d: ",p);
                        printf("INSOMNIA\n");
                    }
                    else
                    {
                        while(no>0)
                        {
                            dig=no%10;
                            c[dig]++;
                            no=no/10;
                        }
                        for(k=0;k<10;k++)
                        {
                            if(c[k]>0)
                            cnt++;
                        }
                        if(cnt==10)
                            printf("%lld",no);
                        else
                        {

                            while(1)
                            {
                                no=tmp*s;
                                while(no>0)
                                {
                                    dig=no%10;
                                    if(!(c[dig]>0))
                                    {
                                        c[dig]++;
                                        cnt++;
                                    }
                                    no=no/10;
                                }
                                s++;
                                if(cnt==10)
                                {
                                    printf("Case #%d: ",p);
                                    printf("%lld",tmp*(s-1));
                                    break;
                                }
                            }
                        }
                    }
                p++;
                }










}
