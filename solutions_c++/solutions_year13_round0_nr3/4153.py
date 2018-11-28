#include<iostream>
#include<cstdio>
using namespace std;
int main()
{

	freopen("input.in","r",stdin);
        freopen("output.txt","w",stdout);
long long int arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
	
	long long int  i,j,k;
	long long int test,count=0;
	long long int a,b;
	scanf("%lld",&test);
	for(k=1;k<=test;k++){
		count=0;
		scanf("%lld",&a);
		scanf("%lld",&b);
		for(i=0;i<39;i++){
			if( arr[i]>=a && arr[i]<=b )
				count++;
		}
		cout <<"Case #"<< k <<":"<<" "<<count;
		cout << endl;
	}
	return 0;
}

