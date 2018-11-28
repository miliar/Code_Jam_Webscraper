#include <cstdio>
#include <cstdlib>

using namespace std;



int cmp( const void *aa , const void *bb )

{

return *(double *)aa > *(double *)bb ? 1 : -1;

}

int cmp2( const void *bb , const void *aa )

{

return *(double *)aa > *(double *)bb ? 1 : -1;

}

int main()
{
	double a[1010],b[1010];
	int t=0;
	scanf("%d",&t);
	int cc=0;
	while ( t-- )
	{
	    ++cc;
		int n;
		scanf("%d",&n);
		for ( int i=0; i<n; ++i ) scanf("%lf",&a[i]);
		for ( int j=0; j<n; ++j ) scanf("%lf",&b[j]);
		qsort(a,n,sizeof(a[0]),cmp);
		qsort(b,n,sizeof(b[0]),cmp2);
		int ii=0,jj=0;
		int pon1=0,pon2=0;


		int i1=0,i2=n-1;
		int j1=0;
		while ( i1<=i2 )
		{
			if ( a[i2]>b[j1] ) { i2--; ++j1; pon1++; }
			if ( a[i2]<b[j1] ) { i1++; ++j1; }
		}

		ii=0;jj=n-1;
		int kk=0;
		while ( ii<n )
		{
			while ( jj>=0 )
			{
				if ( b[jj]>a[ii] ) { kk++; ++ii; }
			   --jj;
			}
			if ( jj<0 ) { pon2=n-kk; break; }
		}
		printf("Case #%d: %d %d\n",cc,pon1,pon2);
	}
	return 0;
}

