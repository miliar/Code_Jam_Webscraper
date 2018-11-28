#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#define ll long long int

using namespace std;

int main(){
	int t,len,i,head,tail,j;
	string S;
	char ans[4003];
	scanf("%d",&t);
	for(j=1;j<=t;j++){
		cin>>S;
		len = S.length();
		head = tail = 2000;
		ans[head] = S[0];
		for(i=1;i<len;i++){
			if(head == tail){
				if(S[i] >= ans[head]){
					head--;
					ans[head] = S[i];
				}
				else{
					tail++;
					ans[tail] = S[i];
				}
			}
			else if(S[i] >= ans[head]){
				head--;
				ans[head] = S[i];
			}
			else if(S[i] <= ans[tail]){
				tail++;
				ans[tail] = S[i];
			}
			else{
				tail++;
				ans[tail] = S[i];
			}
		}
		printf("Case #%d: ",j);
		for(i=head;i!=(tail+1);i++){
			printf("%c",ans[i]);
		}
		printf("\n");
	}
	return 0;
}