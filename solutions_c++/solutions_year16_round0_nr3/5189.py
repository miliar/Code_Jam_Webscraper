#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
using namespace std;
#define ll long double
#define LL long long
#define mod 1000000007
#define gc getchar
#define pc putchar

inline LL read_ll()
{
    LL n=0, ch=gc(), f=1;
    while(ch!='-'&&(ch<'0'||ch>'9'))ch=gc();
        if(ch=='-')
        {
            f=-1;
            ch=gc();
        }
    while(ch>='0'&&ch<='9')
        n=(n<<3)+(n<<1)+ch-'0',ch=gc();
    return n*f;
}

void output(LL n)
{
	if(n<0)
	{
	   n=-n;
	   pc('-');
	}
	int i=10;
	char buffer[11];
	buffer[10]='\n';
	do
	{
		 buffer[--i]=(n%10)+'0';
		 n/=10;
	}while(n);
	do
	{
		pc(buffer[i]);
	}while(++i<11);
}

bool Prim(ll p)
{
    for(ll i=2;i*i<=121;i++)
	{
		 if( fmod(p,i)==0)
		  return true;
	}
    return false;
}

int conquer(int [],int,int,int);
int mergesort(int A[],int s, int e)
{
    //cout<<"abc\n";
    if(e==s)
    {
        return 0;
    }
    int mid=(s+e)/2,inv=0;
    inv=mergesort(A,s,mid);
    inv+=mergesort(A,mid+1,e);
    inv+=conquer(A,s,e,mid);
    return inv;
}
int conquer(int A[],int s,int e,int mid)
{
    int B[10005];
    int i=s,j=mid+1,k=0,inv=0;
    while(i<=mid && j<=e)
    {
        if(A[i]<=A[j])
        {
            B[k++]=A[i];
            i++;
        }
        else
        {
            B[k++]=A[j];
            j++;
            inv+=mid-i+1;
        }
    }
    while(i<=mid)
    {
        B[k++]=A[i++];
    }
    while(j<=e)
        B[k++]=A[j++];
    k=0;
    for(int i=s; i<=e; i++)
    {
        A[i]=B[k++];
    }
    return inv;
}

ll basecon(int v[],int n ,int base)
{
	  ll ret=0;
	  for(int i=0;i<n;i++)
	  {
	  	 ret += ( v[i] * (ll)pow(base,i) );
	  }
	  return ret;
}
int main()
{
	int t, J, n;
    //freopen("C-small-attempt2.in","r",stdin);
    freopen("outccc.txt","w",stdout);

	cin>>t;
	int tst=0;

	while(t--)
	{
		tst++;
		cin>>n>>J;

		printf("Case #%d:\n",tst);
		int v[n+2];
		v[0]=1;v[n-1]=1;
		for(int i=0; i<(1<<(n-2)) ; i++)
		{

			for(int k=0;k<n-2;k++)
			{
				 if( i  & (1<<k) )
				 {
				 	v[k+1]=1;
				 }
				 else v[k+1]=0;
		    }
		    int cnt=0;
			for(ll  j=2;j<=10;j++)
			{
			  ll num = basecon(v,n,j);

			  if(Prim(num))
			  {
			  	cnt++;
			  }
			}
			if(cnt==9)
			{
				for(int j=n-1;j>=0;j--)
                    cout<<v[j];
                printf(" ");
    			J--;

			   for(int  j=2;j<=10;j++)
			   {
			      ll num = basecon(v,n,j);
			      for(ll aa=2;aa*aa<=num;aa++)
				  {
				    if( fmod(num,aa)==0 )
					{
					    //cout<<aa<<" ";
					  printf("%.0Lf ",aa);
					  break;
				    }
				  }
			   }
			   cout<<endl;
			}
            if(J==0)
			 break;
		}
	}
	return 0;
}
