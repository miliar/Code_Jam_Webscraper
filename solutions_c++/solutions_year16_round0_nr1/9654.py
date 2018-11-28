#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("result.txt");

	int T;
	fin>>T;

	for(int t=1;t<=T;t++){
		int n;
		fin>>n;
		vector<int> arr(10,0);

		if(n == 0){
			fout<<"Case #"<<t<<": INSOMNIA"<<endl;
			continue;
		}
		int c;
		int rrr = 0;
		int temp;
		while(1){
			rrr += n;
			temp = rrr;
			while(temp){
				arr[temp%10] = 1;
				temp/=10;
			}
			for(c=0;c<10;c++) if(arr[c] == 0) break;
			if(c==10)
				break;
		}
		fout<<"Case #"<<t<<": "<<rrr<<endl;

	}
	return 0;
}