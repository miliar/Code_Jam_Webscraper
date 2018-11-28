#include <cstdio>
#include <cstdlib>

using namespace std;


long long FSPal[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001};



int main()
{
	FILE *input = fopen("C.in","r");
	FILE *output = fopen("C.out","w+");

	int tests; fscanf(input,"%d",&tests);

	for(int test = 1 ; test <= tests ; test ++)
	{
		long long a,b; fscanf(input,"%lld%lld",&a,&b);

		int ans = 0;

		for(int i = 0 ; i < 40 ; i ++)
		{
			if(FSPal[i] >= a && FSPal[i] <= b){
				ans ++;
			}
		}		

		fprintf(output,"Case #%d: %d\n",test,ans);
	}
	
	system("pause");
	return 0;
}