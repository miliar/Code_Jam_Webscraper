#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	lli z,n,i,j,ans;
	bool arr[10];
	scanf ("%lld", &z);

	for (i=1; i<=z; i++)
    {
        printf ("Case #%lld: ", i);

        for (j=0; j<10; j++)
            arr[j]=0;

        scanf ("%lld", &n);

        if (n==0)
        {
            printf ("INSOMNIA\n");
            continue;
        }

        ans=n;

        while (1)
        {
            for (j=ans; j; j/=10)
                arr[j%10]=1;

            for (j=0; j<10 && arr[j]; j++);

            if (j==10)
                break;

            ans+=n;
        }

        printf ("%lld\n", ans);
    }

	return 0;
}
