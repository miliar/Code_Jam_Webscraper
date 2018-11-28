#include <iostream>
using namespace std;
bool isDone(int freq[10]){
	for(int j=0;j<10;j++){
		if(freq[j]==0)
			return false;
	}
	return true;
}
void addFreq(int freq[10],int N){
	int a;
	while(N>=1){
		a = N%10;
		N = N/10;
		freq[a]++;
	}	
}
int main(){
	freopen("input_1.in","r",stdin);
	freopen("output_1.out","w",stdout);
	int t;
	int a=1;
	cin >> t;
	while(t--){
		long int N;
		int freq[10]={0},b=1;
		cin >> N;
		if(N==0) {
			cout << "Case #" << a++ <<": INSOMNIA"<< endl;
			continue;
		}
		while(!isDone(freq)){
			addFreq(freq,N*b);
//			cout << N*b << ":";
//			for(int i=0;i<10;i++) cout << freq[i] << " ";
//			cout << endl;
			b++;
		}
		cout << "Case #" << a++ <<": " << N*(b-1) << endl;
	}
	return 0;

}
