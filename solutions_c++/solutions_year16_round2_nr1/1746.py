#include <iostream>
using namespace std;
 
int main() {
	string str;
	long x=0,a1,l;
	cin>>a1;
	for (int i=1;i<=a1;i++){
		long caci[100]{},abi[100]{};
		cin>>str;
		l=str.length();
		for (int j=0;j<l;j++){
			caci[int(str[j])]=caci[int(str[j])]+1;
 
			if (str[j]=='Z'){
				caci[69]--;
				caci[82]--;
				caci[79]--;
				abi[0]++;
			}
			if (str[j]=='W'){
 
				caci[84]--;
				caci[79]--; abi[2]++;
			}
			if (str[j]=='X'){
				caci[83]--;
				caci[73]--; abi[6]++;
			}
			if (str[j]=='G'){
				caci[69]--;
				caci[73]--;
				caci[84]--;
				caci[72]--; abi[8]++;
			}
		}
			while(caci[72]>0){
				caci[84]--; caci[72]--; caci[82]--; caci[69]-=2; abi[3]++;
			} 
			while (caci[82]>0){
				caci[70]--; caci[79]--; caci[85]--; caci[82]--; abi[4]++;
			} 
			while (caci[79]>0){
				caci[79]--; caci[69]--; caci[78]--; abi[1]++;
			} 
			while (caci[70]>0){
				caci[70]--; caci[73]--; caci[86]--; caci[69]--; abi[5]++; 
			} 
			while (caci[86]>0){
				caci[78]--; caci[86]--; caci[69]-=2; caci[83]--; abi[7]++;
			}
			while(caci[78]>0){
				caci[73]--; caci[69]--; caci[78]-=2; abi[9]++;
			}
			cout<<"Case #"<<i<<": ";
		for (int j=0;j<10;j++){
			while (abi[j]>0){
				cout<<j;
				abi[j]--;
			}
		}
		cout<<endl;
	}
	return 0;
}
