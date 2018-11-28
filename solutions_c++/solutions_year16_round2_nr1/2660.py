#include <iostream>
using namespace std;

void solve(){
	string phno;
	cin>>phno;
	int phno_size = phno.size();
	int alpha_count[26];
	for (int i = 0; i < 26; ++i)
	{
		alpha_count[i] = 0;
	}
	for (int i = 0; i < phno_size; ++i)
	{
		alpha_count[phno[i]-'A']++;
	}

	int dig_count[10];
	for (int i = 0; i < 10; ++i)
	{
		dig_count[i] = 0;
	}
	dig_count[0] = alpha_count[25];
	dig_count[6] = alpha_count[23];
	dig_count[8] = alpha_count[6];
	dig_count[2] = alpha_count[22];
	dig_count[4] = alpha_count[20];
	dig_count[3] = max(0,alpha_count[17]-dig_count[0]-dig_count[4]);
	dig_count[1] = max(0,alpha_count[14]-dig_count[4]-dig_count[2]-dig_count[0]);
	dig_count[7] = max(alpha_count[18]-dig_count[6],0);
	dig_count[9] = max(0,alpha_count[13]-dig_count[1]-dig_count[7])/2;

	int let4 = dig_count[0] + dig_count[4] + dig_count[9];
	int let3 = dig_count[1] + dig_count[2] + dig_count[6];
	int let5 = dig_count[3] + dig_count[7] + dig_count[8];
	dig_count[5] = (max(0,phno_size - let5*5 - let4*4 - let3*3))/4;

	for (int i = 0; i < 10; ++i)
	{
		//cout<<dig_count[i]<<endl;
		while(dig_count[i]>0){
			dig_count[i]--;
			
			cout<<i;
		}
	}
} 


int main(){
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		cout<<"Case #"<<t+1<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}