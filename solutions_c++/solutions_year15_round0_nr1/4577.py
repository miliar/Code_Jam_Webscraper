#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int a[1200] ;
int main()
{
    int t , n ,step = 0;
    char arr[2000];
    //freopen("testin.txt", "r", stdin);
    //freopen("testout.txt", "w", stdout);
    scanf("%d", &t) ;
    while( t-- )
    {
        scanf("%d %s", &n,arr) ;
        int num = arr[0] - '0';
        int ans = 0;
        for(int i = 1; i <= n; i++)
        {
        	if(num < i)
        	{
        		ans += i - num;
        		num = i;
        	}
        	num += arr[i] - '0';
        }

        printf("Case #%d: %d\n", ++step, ans) ;
    }
    return 0 ;
}
