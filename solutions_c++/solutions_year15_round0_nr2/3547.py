#include <bits/stdc++.h>

#define set(p) memset(p,-1,sizeof(p))
#define clr(p) memset(p,0,sizeof(p))
#define ll long long int
#define llu unsigned long long int
#define si(a) scanf("%d",&a)
#define loop(i,a,n) for(i=(a);i<(n);i++)
#define pii pair<int,int>
#define pb(x) push_back(x)
#define v(x) vector<x>

using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


long long int power(long long int x,long long int y,ll mod)
{
    long long int temp,ty,my;

    if( y == 0)
        return 1;
    temp = power(x, y/2,mod);
    ty=(temp%mod)*(temp%mod);
    if (y%2 == 0)
        {

                return ty%mod;
        }
    else
        {
                my=(x%mod)*(ty%mod);
                return my%mod;
        }
}



long long int maxxi(long long int a,long long int b)
{
        return a>b?a:b;
}

long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}




struct abhi
{
       ll proces;
       ll abhi1;
};

struct abhi brr[100010];

bool cmp(struct abhi x,struct abhi y)
{
        return x.abhi1<y.abhi1;
}



int abhi[10001];

int solve(int d, int modi, int m)
{
    int took[10010];
    int ind = 0,i;

	loop(i,0,d)
	{
		if(abhi[i]>modi)
        {
			took[ind] = abhi[i] - modi;

			ind++;
		}
	}

    loop(i,0,ind)
    {
		if(took[i]>0 && m<=0)
        {
			return 0;
		}

		if(took[i] <= modi)
		{
			m--;
		}
		else
		{
			took[i]=took[i]-modi;
			m--;
			i--;
		}
	}

	return 1;
}

int main()
{
    //freopen("C:\\Users\\ABHISHEK004\\Desktop\\abb.in","r",stdin);
    //freopen("C:\\Users\\ABHISHEK004\\Desktop\\ab.out","w",stdout);

	int i,t,di,tt,answer;
    si(t);
    tt=t;
	while(t--)
	{

        answer = 100010100;
		si(di);

		loop(i,0,di)
            si(abhi[i]);

		loop(i,0,1001)
		{
			int left = 1;
			int right = 1000;
			while(left<right)
            {
				int mid = left + (right-left)/2;

				int proces = solve(di,mid,i);

				if(proces == 1)
				{
					right = mid;
				}
                else
                {
					left =  mid+1;
				}
			}

			if(answer>(i+left))
            {
				answer = i + left;
			}
		}

		printf("Case #%d: %d\n", tt-t, answer);
	}
	return 0;
}
