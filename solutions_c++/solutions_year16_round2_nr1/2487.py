#include <iostream>
#include <string>
#define loop(a,b) for(int i=a;i<b;i++)
using namespace std;
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	int c=1;
	while(t--){
		string str;
		int freq[26]={0};
		int count[10]={0};
		cin >> str;
		for(int i=0;i<str.length();i++){
			freq[str[i]-'A']++;
		}
		///       /ZERO
		if(freq[25]){
			count[0]=freq[25];
			freq[25]-=count[0];
			freq[4]-=count[0];
			freq[17]-=count[0];
			freq[14]-=count[0];
		}
		///   TWO
		if(freq[22]){
			count[2]=freq[22];
			freq[19]-=count[2];
			freq[22]-=count[2];
			freq[14]-=count[2];
		}
		/// FOUR
		if(freq[20]){
			count[4]=freq[20];
			freq[5]-=count[4];
			freq[14]-=count[4];
			freq[20]-=count[4];
			freq[17]-=count[4];
		}
		// FIVE
		if(freq[5]){
			count[5]=freq[5];
			freq[5]-=count[5];
			freq[8]-=count[5];
			freq[21]-=count[5];
			freq[4]-=count[5];
		}
		// SIX
		if(freq[23]){
			count[6]=freq[23];
			freq[23]-=count[6];
			freq[8]-=count[6];
			freq[18]-=count[6];
		}
		// ONE
		if(freq[14]){
			count[1]=freq[14];
			freq[14]-=count[1];
			freq[13]-=count[1];
			freq[4]-=count[1];
		}
		//THREE
		if(freq[17]){
			count[3]=freq[17];
			freq[19]-=count[3];
			freq[7]-=count[3];
			freq[17]-=count[3];
			freq[4]-=count[3];
			freq[4]-=count[3];
		}
		//SEVEN
		if(freq[21]){
			count[7]=freq[21];
			freq[18]-=count[7];
			freq[4]-=count[7];
			freq[21]-=count[7];
			freq[4]-=count[7];
			freq[13]-=count[7];
		}
		// EIGHT
		if(freq[6]){
			count[8]=freq[6];
			freq[4]-=count[8];
			freq[8]-=count[8];
			freq[6]-=count[8];
			freq[7]-=count[8];
			freq[19]-=count[8];
		}
		// NINE
		if(freq[8]){
			count[9]=freq[8];
			freq[13]-=count[9];
			freq[8]-=count[9];
			freq[13]-=count[9];
			freq[4]-=count[9];
		}
		cout << "Case #" << c++ << ": ";
		for(int i=0;i<10;i++)
			while(count[i]--)
				cout << i;
		cout << endl;
	}
	return 0;
}
