#include <vector>
#include <string>
#include <iostream>

using namespace std;

//index 0: top
void convert(string data, vector<bool> &ps){
	ps.resize(data.size(),false);
	for(int i=0;i<data.size();i++){
		ps[i] = (data[i]=='+');
	}
}

void flipAllNeg(vector<bool> &ps, int i){
	for(int j=0; j<i; j++){
		ps[j] = !ps[j];
	}
}

int minNum(vector<bool> &ps){
	int nroFlips = 0;
	int n = ps.size();
	int index = 1;
	bool pos = ps[0];
	while(true){
		if(pos){
			while(index<n && ps[index]){
				index++;
			}
			if(index==n){
				break;
			}
			flipAllNeg(ps, index);
			nroFlips++;
			pos = false;
		}else{
			while(index<n && !ps[index]){
				index++;
			}
			flipAllNeg(ps, index);
			nroFlips++;
			pos = true;
		}
	}
	return nroFlips;
}

int main(){
	int T;
	cin >> T;
	vector<int> res(T);
	for(int i=0;i<T;i++){
		string data;
		cin >> data;
		vector<bool> bData;
		convert(data, bData);
		res[i] = minNum(bData);
	}
	for(int i=0; i<T;i++){
		cout << "Case #" << i+1 << ": " << res[i] <<endl;
	}

	return 0;
}