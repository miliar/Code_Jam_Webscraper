#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[1000001];
bool p[10]={0};

void dig(int a)
{
	if (a==0)
	{
		return;
	}
	p[a%10]=1;
	dig(a/10);
}

int main(void){

	for (int i = 1; i <= 1000000; ++i)
	{
		memset(p,0,sizeof(p));
		for (int j = 1,k; 1; ++j)
		{
			dig(i*j);
			for (k = 0; k < 10 && p[k]; ++k);
			if (k==10)
			{
				s[i]=i*j;
				break;
			}
		}
	}

    int t=0;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        
        printf("Case #%d: ", tt);

        int a;
        scanf("%d",&a);
        if (a==0)
        {
        printf("INSOMNIA\n");
        } else {
        printf("%d\n", s[a]);
        }

    }
    return 0;
}

