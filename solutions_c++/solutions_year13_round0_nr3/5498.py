#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;
bool Is(long long int target)
{
    if (target <= 1)
        return true;

    long long int currentSquare = 4;
    long long int currentNumber = 2;
    while (currentSquare <= target)
    {
        if (currentSquare == target)
            return true;
        currentNumber++;
    
        currentSquare = currentNumber * currentNumber;
    }
    return false;
}

int main()
{
	long long int t,i,j,a,b,k;
	long long int sqr;
	string s1;
	scanf("%lld",&t) ;
	int c = 1;
	while (t--) {
		int flag = 0;
		int flg = 0;
		scanf("%lld %lld",&a,&b);
		int count = 0;
		for (i = a; i <= b; i++) {
			flag = 0;
			if (Is(i)) {
				s1 = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
				for (j = 0,k = s1.size()-1; j <= s1.size()/2; j++,k--) {if (s1[j] != s1[k]){flag = 1;break;}}
				if (flag == 0) {
					sqr = sqrt(i);
					s1 = static_cast<ostringstream*>( &(ostringstream() << sqr) )->str();
					for (j = 0,k = s1.size()-1; j <= s1.size()/2; j++,k--) {if (s1[j] != s1[k]){flag = 1;break;}}
					if (flag == 0) {
//						printf("%lld %lld\n",i,sqr);
						flg = 1;
						count = 1;
						break;
					}
				}
			}
		}
		if (flg == 1) {			
			for (i = sqr+1; i <= b; i++) {
				flag = 0;
				if (i*i > b) {
					
					break;
				}
				s1 = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
				for (j = 0,k = s1.size()-1; j <= s1.size()/2; j++,k--) {if (s1[j] != s1[k]){flag = 1;break;}}
				if (flag == 0) {
				s1 = static_cast<ostringstream*>( &(ostringstream() << i*i) )->str();
				for (j = 0,k = s1.size()-1; j <= s1.size()/2; j++,k--) {if (s1[j] != s1[k]){flag = 1;break;}}
				}
				if (flag == 0) {
//					printf("%lld %lld\n",i,i*i);
					count++;
				}
				
			}
		}
		printf("Case #%d: %d\n",c,count);
		c++;
	}
	return 0;
}
