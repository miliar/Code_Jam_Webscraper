#include<iostream>
using namespace std;
__int64 a, b;
__int64 i;
__int64 temp, ans = 0;
char number[1000];
int main(void)
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	bool flag1 = true, flag2 = true;
	cin>>n;
	for(int t = 1; t <=n; t++){
		ans = 0;
		cin>>a>>b;
		i = sqrt(a);
		temp = i * i;
		if(temp < a)i++;
		for(; i*i <= b; i++){
			temp = i * i;
			flag1 = true;
			flag2 = true;
			memset(number, 0, sizeof(char) * strlen(number));
			itoa(i, number, 10);
			for(int j = 0, k = strlen(number) - 1; j<strlen(number); j++, k--){
				if(number[j] != number[k]){
					flag1 = false;
					break;
				}
			}

			memset(number, 0, sizeof(char) * strlen(number));
			itoa(temp, number, 10);
			for(int j = 0, k = strlen(number) - 1; j<strlen(number); j++, k--){
				if(number[j] != number[k]){
					flag2 = false;
					break;
				}
			}
			if(flag1 && flag2)ans++;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}