#include <iostream>
#include <sstream>
using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int cases;
	int i = 0;
	int count = 0;
	int numberCase = 1;
	int res = 0;
	char ant;
	scanf("%d\n",&cases);
	string stack;
	while(cases > 0){
		cin >> stack;
		if(stack[0] == '+'){
			ant = '+';
			for(;i<stack.size();i++){
				if(stack[i] != ant){
					count++;
				}
				ant = stack[i];
			}
			if(count%2 != 0){
				count = count + count%2;
			}
			printf("Case #%d: %d\n",numberCase,count);
		}else{
			ant = '-';
			for(;i<stack.size();i++){
				if(stack[i] != ant){
					count++;
				}
				ant = stack[i];
			}
			if(count%2==0){
				count +=1;
			}
			printf("Case #%d: %d\n",numberCase,count);
		}
		count = 0;
		i = 0;
		cases--;
		numberCase++;
	}
	
	return 0;
}