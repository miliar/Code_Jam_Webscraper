#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int isPalindrome(unsigned long orig)
{
    unsigned long reversed = 0, n = orig;

    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }

    return (orig == reversed);
}

int A[25];

void precal()
{
    unsigned long long i,temp;
    int j=0;
    for(i=1; i<=10000000;i++)
        {
            if(isPalindrome(i))
            {
                temp=i*i;
                if(isPalindrome(temp))
                    {
                        A[j]=(int)temp;
                        j++;
                    }
            }
        }
}

int main()
{
//	freopen("A.in","r",stdin);freopen("SampleOut.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	precal();
	const int size=21;
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
        unsigned long long a,b,temp;
        int count=0,j=0;
		scanf("%llu%llu",&a,&b);
        while(j<size)
        {
            temp=A[j];
            if(temp<a)
                j++;
            else
                break;
        }

        if(j!=size)
            {
                while(j<size)
                {
                    temp=A[j];
                    if(temp<=b)
                        {
                            count++;
                            j++;
                        }
                    else
                        break;
                }
            }

		printf("Case #%d: ",caseId);
        printf("%d\n",count);
	}
	return 0;
}
