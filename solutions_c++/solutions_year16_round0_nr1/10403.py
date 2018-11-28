#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void extract_digits(int n,map<int,int> &arr,int &count){
	int last_digit;
	while(n){
		last_digit = n%10;
		n /=10;
		if(arr[last_digit] == 0){
			arr[last_digit] = 1;
			count++;
		}
	}
}

void last_number(int &n){
	map<int,int> arr;
	int temp = n,i=1,count = 0;
	while(1){
		n = temp*i;
		extract_digits(n,arr,count);
		if(count == 10)
			break;
		i++;
	}
}

int main(int argc, char const *argv[]){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,n;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>n;
		if(n == 0)
		printf("Case #%d: INSOMNIA\n",t);
		else{
			last_number(n);
			printf("Case #%d: %d\n",t,n);
		}
	}
    
	return 0;
}