#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char s[1005];
int ssi[1005];

int main()
{
    freopen ("standing_ovation.in","r",stdin);
    freopen ("standing_ovation.out","w",stdout);
    int cases;
    int n;
    int len;
    int res;
    int num_person;
    scanf("%s",s);
    cases = atoi(s);
    for(int i=0;i<cases;i++)
    {
            res = 0;
            num_person = 0;
            scanf("%s",s);
            n = atoi(s);
            scanf("%s",s);
            len = strlen(s);
            for(int j=0;j<len;j++)
            {
                    ssi[j] = s[j]-'0';
                    if(!j) num_person+=ssi[j];
                    else
                    {
                        if(num_person < j)
                        {
                         res+=(j-num_person);
                         num_person+=(j-num_person);
                        }
                        num_person+=ssi[j];
                    }
            }
            printf("Case #%d: %d\n",i+1,res);
    }
    fclose(stdout);
    return 0;
}
