#include <cstring>
#include <set>
using namespace std;

int main(){
	int tc,num,digit,copy,counter;
	scanf("%d",&tc);
	for(int i=1; i<=tc; i++){
		scanf("%d",&num);
		printf("Case #%d: ",i);
		if(num==0) printf("INSOMNIA\n");
		else{
			set<int> digits;
			counter=1;
			copy = num;
			while(1){
				num*=counter;
				counter++;
				while(num!=0){
					digit=num%10;
					num/=10;
					digits.insert(digit);
				}
				num=copy;
				if(digits.size()==10) {printf("%d\n",num*(counter-1)); break;}
			}

		}
	}
}