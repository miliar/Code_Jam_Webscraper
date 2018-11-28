#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream i("A.txt");
	ofstream o;
	o.open("Aout.txt");
	
	string S;
	string s[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	unsigned int T, pi, pj;
	
	i>>T;
	for(int cnt=0; cnt<T; cnt++){
		string str;
		int a[26] = {0};
		int b[10] = {0};
		i>>str;
		for(int si=0; si< str.length(); si++){
			a[str[si]-'A']++;
		}
		
		string number = "";
		if(a[25]){
			while(a[25]!=0){
				b[0]++;
				a[25]--;a[4]--;a[17]--;a[14]--;
			}
		}
		if(a[22]){
			while(a[22]!=0){
				b[2]++;
				a[19]--;a[22]--;a[14]--;
			}
		}
		if(a[20]){
			while(a[20]!=0){
				b[4]++;
				a[5]--;a[14]--;a[20]--;a[17]--;
			}
		}
		if(a[23]){
			while(a[23]!=0){
				b[6]++;
				a[18]--;a[8]--;a[23]--;
			}
		}
		if(a[6]){
			while(a[6]!=0){
				b[8]++;
				a[4]--;a[8]--;a[6]--;a[7]--;a[19]--;
			}
		}
		if(a[14]){
			while(a[14]!=0){
				b[1]++;
				a[14]--;a[13]--;a[4]--;
			}
		}if(a[19]){
			while(a[19]!=0){
				b[3]++;
				a[19]--;a[7]--;a[17]--;a[4]--;a[4]--;
			}
		}if(a[5]){
			while(a[5]!=0){
				b[5]++;
				a[5]--;a[8]--;a[21]--;a[4]--;
			}
		}if(a[18]){
			while(a[18]!=0){
				b[7]++;
				a[18]--;a[4]--;a[21]--;a[4]--;a[13]--;
			}
		}if(a[13]){
			while(a[13]!=0){
				b[9]++;
				a[13]--;a[8]--;a[13]--;a[4]--;
			}
		}
		for(int j=0; j<10; j++){
			while(b[j]!=0){
				number+='0'+j;
				b[j]--;
			}
		}
		
		
		o<<"Case #"<<cnt+1<<": "<<number<<endl;
	}	
	
	i.close();
	o.close();
	return 0;
}
