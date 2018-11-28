#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int i,sum=0,ans=0,counter=0;
    FILE *f1,*f2;
    f1=fopen("ques1.in","r");
    f2=fopen("sol.txt","w");
    int T;
    fscanf(f1,"%d",&T);
    while(T--)
    {
        counter++;
        sum=ans=0;
        int N;
        fscanf(f1,"%d",&N);
        char s[N+2];
        fgetc(f1);
        for(i=0;i<=N;i++)
        {
            s[i]=fgetc(f1);
        }
        s[i]='\0';
        for(i=0;i<=N;i++)
        {
            if(s[i]!='0' && sum>=i)
                sum+=s[i]-'0';
            else
            {
                if(s[i]!='0')
                {
                    ans+=(i-sum);
                    sum+=(i-sum);
                    sum+=s[i]-'0';
                }
                cout << "ans:" << ans << " sum:" << sum << endl;
            }
        }
        fprintf(f2,"Case #%d: %d\n",counter,ans);
    }
    return 0;
}
