#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

using namespace std;

bool is_parindrome(long long val)
{
    long long left = 1;
    while(val >= left*10){
        left *=10;
    }
    
    long long right = 1;
    while(left > right){
        long long leftnum = (val / left) % 10;
        long long rightnum = (val % (right*10))/right;
        // printf("left=%lld, right=%lld, leftnum=%lld, rightnum=%lld\n", left, right, leftnum, rightnum);
        if(leftnum != rightnum){
            return false;
        }
        right *=10;
        left /=10;
    }
    return true;
    
}
long long rev(long long num)
{
    long long revnum = 0;
    while(num){
        int a = num % 10;
        num /= 10;
        revnum *= 10;
        revnum += a;
    }
    return revnum;
}
vector<long long> fairsquares;
void init(void)
{
    long long i = 1;
    long long base = 1;
    // long long total = 0;
    long long MAXSQVAL = 100000000000000;
    while(1){
        long long val, sqval;
        val = i*base + rev(i/10);
        sqval = val * val;
        if(sqval > MAXSQVAL){
            break;
        }
        //if(sqval>=A && sqval<=B){
        if(is_parindrome(sqval)){
            // printf("i=%10lld, %10lld * %10lld = %10lld is parindrome\n", i, val, val, sqval);
            fairsquares.push_back(sqval);
            // total++;
        }
        //}
        
        val = i*(base*10)+rev(i);
        sqval = val * val;
        //if(sqval>=A && sqval<=B){
        if(is_parindrome(sqval)){
            // printf("i=%10lld, %10lld * %10lld = %10lld is parindrome\n", i, val, val, sqval);
            fairsquares.push_back(sqval);
            // total++;
        }
        //}
        
        i++;
        if(i>=base*10){
            base *=10;
        }
    }
}
void testcase(int t)
{
	string result_str = "OK";
    long long A, B;
    cin >> A >> B;

    long long total = 0;
    for(vector<long long>::iterator it = fairsquares.begin();it!=fairsquares.end();it++){
        long long sqval = *it;
        if(A<= sqval && sqval<=B){
            total ++;
        }
    }
    
    
#if 0
    while((val=i*i)<=B){
        if(is_parindrome(val)){
            printf("%lld * %lld = %lld is parindrome\n", i, i, val);
            total++;
        }
        i++;
    }
#endif
	cout << "Case #" << (t+1) << ": " << total << endl;
}

int main(int argc, char *argv[]) {
	int T;
    if(argc >= 2){
        int fd = open(argv[1], O_RDONLY);
        if(fd == -1){
            fprintf(stderr, "failed to open [%s]\n", argv[1]);
            exit(1);
        }
        int ret = dup2(fd, 0);
        if(ret == -1){
            fprintf(stderr, "failed to dup2[%s]\n", argv[1]);
            exit(1);
        }
    }
    init();
	cin >> T;
	for(int t=0;t<T;t++){
		testcase(t);
	}
	return 0;
}

