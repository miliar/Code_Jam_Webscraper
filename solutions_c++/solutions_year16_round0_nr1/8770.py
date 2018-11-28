#include <iostream>
#include <string>
#include <cmath>
#include <unordered_map>
using namespace std;

class solution{
	int n;
	unordered_map<int,int> map;
public:
	solution(int in) : n(in){
		int ans = getAns();
		if(ans==0)cout << "INSOMNIA" << endl; 
		else cout << ans << endl;
	}

	int getAns(){
		if(n<=0) return 0;
		extract(n);
		int count=0,i=1,tmp;
		while(!isAllDigitTook() || count==100){
			tmp = n*i;
			count++; 
			i++;
			extract(tmp);
		}
		if(count==100) return 0;
		else return tmp;
	}

	void extract(int a){
		string tmp=to_string(a);
		for(int i=0;i<tmp.size();i++){
			map[int(tmp[i])-48] = 1;
		}
	}

	bool isAllDigitTook(){
		for(int i=0;i<=9;i++)
			if(map[i]==0)return false;
		return true;
	}


	int getDigit(){
		if(n==0) return 0;
		if(n<0) n *= -1;
		int out=0;
		while(n!=0){
			n /= 10;
			out++;
		}
		return out;
	}
};


int main(){
	int count;
	cin >> count;
	int aa;
	for(int i=0;i<count;i++){
		cin >> aa;
		cout << "Case #" << i+1 << ": ";
		solution a(aa);
	}
	return 0;
}