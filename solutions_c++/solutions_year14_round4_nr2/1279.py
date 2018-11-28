#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <climits>

using namespace std;

typedef long long LL;

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );

#define X first
#define Y second

#define MP make_pair

#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)


typedef pair<int,int> pint;
typedef map<int,int> mint;

#define sz 20
#define inf INT_MAX
int cnt;
int a[sz+2],L[sz+2],R[sz+2];

void merge(int p,int q,int r)
{
	int i,j,k,ind1,ind2;

	for(i = p,ind1 = 1;i <= q;i++)
	{
		L[ind1++] = a[i];
	}
	L[ind1] = inf;

	for(i = q+1,ind2 = 1;i <= r;i++)
	{
		R[ind2++] = a[i];
	}
	R[ind2] = inf;

	i = j = 1;

	for(k = p;k <= r;k++)
	{
		if(L[i] > R[j])
		{
			cnt += ind1 - i;
			a[k] = R[j];
			j++;
		}
		else
		{
			 a[k] = L[i];
			 i++;
		}
	}
}

void mergeSort(int p,int r)
{
	if(p < r)
	{
		int q = (p+r)/2;
		mergeSort(p,q);
		mergeSort(q+1,r);
		merge(p,q,r);
	}
}

#define SIZE 12
int arr[SIZE];
mint ini;

int main(){

    freopen("B-small-attempt3.in","r",stdin);
    freopen("out.out","w",stdout);

    //FRO

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){
        int n;
        scanf("%d",&n);

        ini.clear();
        for (int i=0;i<n;++i){
            scanf("%d",&arr[i]);
            ini[ arr[i] ]=i;
        }

        sort( arr,arr+n );
        int ans =INT_MAX;
        do{
            int now = 0;
            for (int i=1;i<n;++i){
                if ( arr[i]>arr[now] ){
                    now++;
                }else{
                    break;
                }
            }

            for (int i=now+1;i<n;++i){
                if ( arr[i]<arr[now] ){
                    now++;
                }else{
                    break;
                }
            }

            if ( now!=n-1 )continue;
            /*
            for (int i=0;i<n;++i){
                cout<<arr[i]<<" ";
            }cout<<endl;
            */

            cnt = 0;
            for (int i=0;i<n;++i){
                a[i+1]=ini[ arr[i] ];
            }
            mergeSort( 1,n );

            ans = min( ans,cnt );

        }while ( next_permutation(arr,arr+n) );
        printf("Case #%d: %d\n",kk,ans);
    }


    return 0;
}
