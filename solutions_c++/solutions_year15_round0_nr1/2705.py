#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[]){
	int n,t,count,ans,num;
	string s;
	cin>>t;
	for (int no = 1; no <= t; ++no)	{
		count=0; ans =0;
		cin>>n>>s;
		for (int i = 0; i <= n; ++i){
			num = s[i] - '0';
			if(count<i){
				ans +=  i-count;count += i-count;
			}
			count += num;
		}
		cout<<"Case #"<<no<<": "<<ans<<endl;
	}
	return 0;
}