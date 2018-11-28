// code by swayam raina

#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()
{
    FILE *in = fopen("A-small-attempt0.in","r");
    FILE *out = fopen("output_problemA.txt","w");
    int tc,s_max;
    char str[1001];
    fscanf(in,"%d",&tc);
    for(int j=1;j<=tc;j++)
    {
        fscanf(in,"%d",&s_max);
        long long int need = 0;
        fscanf(in,"%s",str);
        long long int standing = str[0]-'0';
        for(int i=1;i<=s_max;i++)
        {
            if(str[i]-'0')
            {
                if(standing >= i)
                {
                    standing += (str[i]-'0');
                }
                else
                {
                    need += (i-standing);
                    standing += (str[i]-'0') + need;
                }
            }
        }
        fprintf(out,"Case #%d: %lld\n",j,need);
    }
    return 0;
}
