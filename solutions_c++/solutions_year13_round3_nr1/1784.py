#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

int main()
{
	freopen("A1.in","rt",stdin);
	freopen("A1.out","wt",stdout);
    int t;
    cin>>t;
    char vowels[5]={'a', 'e', 'i', 'o', 'u'};
    for(int zz=0;zz<t;zz++)
    {
        char name[101];
        memset(name,0,sizeof(name));
        int len;
        scanf("%s %d", name, &len);
        int out=0;
        for(int i=0;i<strlen(name);i++)
        {
            int ttt=strlen(name)-i;
            for(int j=1;j<strlen(name)+1-i;j++)
            {
                char tmp[101];
                memset(tmp,0,sizeof(tmp));
                strncpy(tmp, name+i,j);
//                printf(tmp);
                int con=0;
                for(int k=0;k<strlen(tmp);k++)
                {
                    bool isCon = true;
                    for(int l=0;l<5;l++)
                    {
                        if (tmp[k] == vowels[l])
                        {
                            isCon=false;
                            break;
                        }
                    }
                    if (isCon)
                        con++;
                    else
                        con=0;
                    if (con >= len)
                        break;
                    
                }
                if (con >= len)
                    out++;
            }
        }
        printf("Case #%d: %d\n", zz+1, out);
    }
}