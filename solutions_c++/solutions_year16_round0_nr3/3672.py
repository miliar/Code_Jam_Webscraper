#include <vector>
#include <cstdio>
#define N 34000000

using namespace std;
bool isprime[N];
vector <unsigned long long> primes;
unsigned long long powers[11][16];

void calc_powers(void)
{
	int i,j;
	for (i=2;i<=10;++i) {
		powers[i][0]=1;
		for (j=1;j<=15;++j) {
			powers[i][j] =powers[i][j-1]*i;
			//printf("%llu ",powers[i][j]);
		}
		//printf("\n");
	}
	
}

int divisible_by(unsigned long long n)
{
	int sz = primes.size();
	//printf("here %s n %llu", __FUNCTION__,n);
	int i;
	for (i=0;primes[i]*primes[i]<n;++i) {
		if(n%primes[i]==0) {
			//printf("%llu is divisible by %llu\n",n, primes[i]);
			return primes[i];
		}
	}
	return 0;
}

unsigned long long in_base_x(int pattern, int base)
{
	unsigned long long ret = 0;
	//printf("here %s", __FUNCTION__);
	int i;
	for (i=0;i<16;++i) {
		if (pattern&(1<<i)) {
			ret += powers[base][i];
		}
	}
	return ret;	
}

vector<unsigned long long> is_jam(int pattern)
{
	unsigned long long nums[11][2], lt1, lt2;
	vector <unsigned long long> divs;
	int i;
	//printf("here %s", __FUNCTION__);
	for (i=2;i<=10;++i) {
		lt1 = in_base_x(pattern, i);
		lt2 = divisible_by(lt1);
		if (lt2 ==0) {
			divs.clear();
			return divs;
		}
		divs.push_back(lt2);
		
	}

	return divs;
}
char binary_string[20];
void to_binary(int a)
{
	int i;
	//printf("convert %d to binary\n",a);
	for (i=0;i<16;++i) {
		if (a&(1<<i)) {
			binary_string[15-i]='1';
		} else {
			binary_string[15-i]='0';
		}
		//printf("pos %d char %c\n",15-i, binary_string[15-i]);
	}
	binary_string[16]=0;
}


int main()
{
    int i;
	for (i=0;i<N;++i)
		isprime[i]=1;
	
	unsigned long long li=2;
	while(li<N) {
		//printf("%llu\n", li);
		primes.push_back(li);
		unsigned long long j;
		for (j = li*li;j<N;j+=li) {
			isprime[j]=0;
		}
		li++;
		while(li <N && !isprime[li]) {
			li++;
		}
	}
	calc_powers();
	int pattern = 32769;
	vector <unsigned long long> ans;
	int count =0;
	printf("Case #1:\n");
	while (count<50) {
		ans = is_jam(pattern);
		if (ans.size()!=0) {
			to_binary(pattern);
			printf("%s", binary_string);
			for (i=0;i<ans.size();++i)
				printf(" %llu",ans[i]);
			printf("\n");
			count++;
		}
		pattern+=2;
		
	}
	
	return 0;
}