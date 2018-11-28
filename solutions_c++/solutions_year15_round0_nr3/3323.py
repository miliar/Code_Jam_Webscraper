//void * memset ( void * ptr, int value, size_t num )
#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
#define MAX 10010
#define MOD 1000000007

int mp[5][5] = {{0,0,0,0,0,},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};//map

int mul(int i, int j){

	int sign = 1;
	if(i<0){
		sign *= -1 ; i*= -1;
	}
	if(j<0){
		sign *= -1 ; j*= -1 ;
	}

	return (mp[i][j]*sign);

}

char s[MAX];
int cumi[MAX];//finding cumulative i
int cumk[MAX];//finding k
int arr[MAX];

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,k,l,i,x ;
	string str ;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>l>>x;
		cin>>str ;
		for(i=0;i<l*x;i++)
			s[i] = str[i%l];

		for(i=0;i<l*x;i++)
		{
			if(s[i] == 'i')
				arr[i]=2;
			else if(s[i] == 'j')
				arr[i]=3;
			else
				arr[i]=4;
		}
		
		cumi[0]=arr[0];
		for(int i=1;i<l*x;i++)
			cumi[i] = mul(cumi[i-1],arr[i]);

		cumk[l*x-1 ] =arr[l*x-1];
		for(int i=l*x-2;i>=0;i--)
			cumk[i] = mul(arr[i],cumk[i+1]);

		bool isexist = false;
		bool flag = false;
		
		for(int i=0;i<l*x-1;i++)
		{
			if(!isexist and (cumi[i] == 2))
				isexist = true;

			if(isexist and (cumi[i] == 4) and (cumk[i+1] == 4))
			{
				flag = true;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<k<<": YES"<<endl;
		else
			cout<<"Case #"<<k<<": NO"<<endl;
	}
	return 0;
}
