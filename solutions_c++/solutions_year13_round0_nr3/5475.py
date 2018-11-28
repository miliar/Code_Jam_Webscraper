#include<fstream>
#include<stdlib.h>
#include<math.h>
using namespace std;
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");
int main()
{
    int t, i, j, k, count, len, flag;
    fin>>t;
    int a, b;
    char str[5];
    for(i=0;i<t;i++)
    {
        count = 0;
        fin>>a>>b;
        for(j=a;j<=b;j++)
        {
            flag = 1;
            itoa(j, str, 10);
            for(len=0;str[len+1];len++);
            for(k=0;str[k];k++, len--)
            {
                if(str[k]!=str[len])
                {
                    flag = 0;
                    break;
                }
            }
            if(flag==0)
                continue;
            if(fmod(sqrt(j),1)!=0)
            {
                flag = 0;
                continue;
            }
            itoa(sqrt(j), str, 10);
            for(len=0;str[len+1];len++);
            for(k=0;str[k];k++, len--)
            {
                if(str[k]!=str[len])
                {
                    flag = 0;
                    break;
                }
            }
            if(flag == 1)
                count++;
        }
        fout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    return 0;
}
