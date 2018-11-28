#include <iostream>
#include <sstream>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int cases;
	int numberCase = 1;
	long long int number;
	long long int copy;
	long long int copy2;
	bool digits[10] = {false};
	int count = 10;
	int mult = 1;
	int i = 0;
	scanf("%d\n",&cases);
	while(cases > 0){
		scanf("%lld\n",&number);
		if(number <= 0){
			printf("Case #%d: INSOMNIA\n",numberCase);
		}else{
			while(count > 0){
				copy = number * mult;
				copy2 = copy;
				while(copy2 > 0){
					if(count <= 0){
						break;
					}
					if(!digits[copy2%10]){
						count--;
						digits[copy2%10] = true;
					}
					copy2 = copy2 / 10;
				}
				mult++;
			}
			printf("Case #%d: %lld\n",numberCase,copy);
			count = 10;
			mult = 1;
			for(int i = 0;i<10;i++){
				digits[i] = false;
			}
		}
		cases--;
		numberCase++;
	}
	return 0;
}