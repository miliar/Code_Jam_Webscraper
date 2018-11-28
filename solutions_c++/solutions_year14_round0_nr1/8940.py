#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int arr1[5][5],arr2[5][5];

int main()
{
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int k=0,T,R1,R2;
    
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		printf("Case #%d: ",k);
		
		scanf("%d",&R1);R1--;
		fo(i,4)
			fo(j,4)
				scanf("%d",&arr1[i][j]);
		
		scanf("%d",&R2);R2--;
		fo(i,4)
			fo(j,4)
				scanf("%d",&arr2[i][j]);
		
		int cnt=0,num=-1;
		
		fo(i,4)
			fo(j,4)
				if(arr1[R1][i] == arr2[R2][j])
					cnt++,num=arr1[R1][i];
		
		if(!cnt)printf("Volunteer cheated!\n");
		else if(cnt>1)printf("Bad magician!\n");
		else printf("%d\n",num);
	}
}


































