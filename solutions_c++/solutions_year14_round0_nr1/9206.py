#include<bits/stdc++.h>
#define  mp make_pair
#define MOD 1000000007
#define sc(n) scanf("%d",&n);
#define p(n)   printf("%d",n);
#define nl      printf("\n");

using namespace std;


int arr[17];
int matx[5][5],maty[5][5];
long long   t,i,k;
int main()
{
	int n,m;

freopen("C:\\Users\\Chandan\\Desktop\\input.txt","r",stdin) ;
   freopen("C:\\Users\\Chandan\\Desktop\\output.txt","w",stdout);
   
    k=1;
    cin>>t;
while(t--)
{

int ans1,ans2,ans,c=0,j;

	cin>>ans1;
	for(i=0;i<4;i++)
	{
	
	for(j=0;j<4;j++)
	{
		
	cin>>matx[i][j];
	}
}
	
	
	cin>>ans2;
	
	for(i=0;i<4;i++)
	{
	
	for(j=0;j<4;j++)
	{
		
	cin>>maty[i][j];
	}
}
	ans1-=1;
	ans2-=1;
	bool flag=true;
for(i=0;i<4&&flag==true;i++)
{
	for(j=0;j<4;j++)
	{
	if(matx[ans1][i]==maty[ans2][j])
	
	{
		c++;
	if(c>1)
	{
		flag=false;
		break;
	}
	
	else
	ans=matx[ans1][i];
	}
	}
}	
	
	
if(c>1)
printf("Case #%lld: Bad magician!\n",k);
else
if(c==0)
printf("Case #%lld: Volunteer cheated!\n",k);
else
printf("Case #%lld: %d\n",k,ans);


k++;

}

	return 0;
}





