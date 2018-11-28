#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

typedef unsigned long long ull;
int T, n, j;
int ans[20];

vector<int> mul(vector<int> x, int y)
{

}

vector<int> add(vector<int> x, int y)
{

}

int mod(vector<int> x, int y)
{

}

bool prime(vector<int> x, int p)
{
    for (int i = 2; i<100; i++)
        if (mod(x, i) == 0)
        {
            ans[p] = i;
            return false;
        }
    return true;
}
bool prime(ull x, int p)
{
    if (x <= 1) return false;
    for (int i = 2; i*i <= x; i++)
        if (x%i == 0)
        {
            ans[p] = i;
            return false;
        }
    return true;
}



bool jamcoin(ull n)
{
    vector<int> d;
    for (;n;n/=2) d.push_back(n%2);
    for (int b = 2; b <= 10; b++)
    {
        ull x = n;
        ull m = 1;
        ull r = 0;
        //vector<int> r;
        for (int i = d.size() - 1; i >= 0; i--)
        {
            r = r*b + d[i];
            //r = mul(r,b);
            //r = add(r,d[i])
        }
        //cout<<r<<" ";
        if (prime(r, b))
            return false;
    }
    //cout<<endl;
    return true;
}

bool jamcoin2(ull n)
{
    for (int b = 2; b <= 10; b++)
    {
        ull x = n;
        ull m = 1;
        ull r = 0;
        while (x)
        {
            r += x%2*m;
            x /= 2;
            m *= b;
        }
        //cout<<r<<" ";
        if (prime(r, b))
            return false;
    }
    //cout<<endl;
    return true;
}

void print(ull x)
{
    vector<int> r;
    for (;x;x/=2)
        r.push_back(x%2);
    for (int i=r.size()-1;i>=0;i--)
        printf("%d",r[i]);
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    //freopen("B-large.in","r",stdin);
    freopen("a.txt","w",stdout);
	scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
        scanf("%d %d", &n, &j);
        printf("Case #%d:\n", cse);
        int cnt = 0;
        for (ull i = 1<<(n-2); cnt < j && i < (1<<(n-1)); i++)
        {
            ull x = i<<1|1;
            if (jamcoin(x))
            {
                cnt ++;
                print(x);
                for (int i = 2; i <= 10; i++)
                    printf(" %d",ans[i]);
                printf("\n");
            }
        }

	}
	return 0;
}

