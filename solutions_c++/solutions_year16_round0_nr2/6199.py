// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{
  char stack[200];
  int t;
  scanf("%d",&t);
  for(int k = 0 ; k < t ; k++) {
    scanf("%s",stack);
    char last = stack[0];
    int cnt = 0;
    int i = 1;
    for(; stack[i] != '\0' ; i++) {
    	if(last != stack[i]) {
    		cnt++;
    	}
    	last = stack[i];
    }
    if(stack[i-1] != '+') {
    	cnt++;
    }
    printf("Case #%d: %d\n",k+1, cnt);
  }

  return 0;
}
