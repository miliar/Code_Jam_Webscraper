

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <list>
//#include <unordered_map>



using namespace std;

typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;

//#define MIN = -1000000000;
template<typename T>
void display(T a[], int size){
	for(int i = 0; i < size; i++){
		cout<<a[i]<<" ";
	}
	cout<<endl;
}

void display(vector<PII> a){
	for(int i = 0; i < a.size(); i++){
		cout<<"("<<a[i].first<<","<<a[i].second<<")"<<" ";
	}
	cout<<endl;
}

void display(vector<int> a){
	for(int i = 0; i < a.size(); i++){
		cout<<a[i];
		if(i == a.size() - 1) cout<<endl;
		else cout<<" ";
	}
}

template<typename T>
void initialise(T a[], T value, int length){
        for(int i = 0; i < length; i++) a[i] = value;
}

template<typename T>
void initialise(vector<T>& a, T value){
    for(int i = 0; i < a.size(); i++) a[i] = value;
}


bool compare(PII a, PII b){
	if(a.first != b.first) return a.first < b.first;
	else return a.second < b.second;
}

int max(int a[], int n){
	int max = -1000000000;
	for(int i = 0; i < n; i++){
		if(a[i] > max) max = a[i];
	}
	return max;
}

bool find(string a[], string s, int n){
	int left = 0;
	int right = n -1;
	while(left < right){
		int mid = (left+right)/2;
		if(s.compare(a[mid]) == 0) return true;
		else if(s.compare(a[mid]) < 0){
			right = mid;
		}
		else{
			left = mid + 1;
		}
	}
	return false;
}

void factor(int a[], int base, int num, int n){
	for(int i = n - 1; i >= 0; i--){
		a[i] = num % base;
		num = num/base;
	}
}


int findLength(int n, int base){
	int i = 0;
	while(n > 0){
		i++;
		n = n/base;
	}
	return i;
}

int gcd(int a, int b){
	while( a % b != 0 && b % a != 0){
		if(b > a){
			b = b % a;
		}
		else if(a > b){
			a = a % b;
		}
	}

	if(a <= b) return a;
	else return b;
}





int main(){
	ofstream fout("A.out");
	int test; cin>>test;
	for(int t = 0; t < test; t++){
		string s; cin>>s;
		map<char, int> count;
		int phone[10];
		for(char a = 'A'; a <= 'Z'; a++){
			count[a] = 0;
		}
		for(int i = 0; i < s.length(); i++){
			count[s[i]]++;
		}
		// for(char a = 'A'; a <= 'Z'; a++){
		// 	cout<<a<<": "<<count[a]<<endl;
		// }
		// cout<<endl;
		phone[0] = count['Z'];
		count['Z'] -= phone[0];
		count['E'] -= phone[0];
		count['R'] -= phone[0];
		count['O'] -= phone[0];
		phone[2] = count['W'];
		count['T'] -= phone[2];
		count['W'] -= phone[2];
		count['O'] -= phone[2];
		phone[6] = count['X'];
		count['S'] -= phone[6];
		count['I'] -= phone[6];
		count['X'] -= phone[6];
		phone[4] = count['U'];
		count['F'] -= phone[4];
		count['O'] -= phone[4];
		count['U'] -= phone[4];
		count['R'] -= phone[4];
		phone[7] = count['S'];
		count['S'] -= phone[7];
		count['E'] -= phone[7];
		count['V'] -= phone[7];
		count['E'] -= phone[7];
		count['N'] -= phone[7];
		phone[5] = count['V'];
		count['F'] -= phone[5];
		count['I'] -= phone[5];
		count['V'] -= phone[5];
		count['E'] -= phone[5];
		phone[1] = count['O'];
		count['O'] -= phone[1];
		count['N'] -= phone[1];
		count['E'] -= phone[1];
		phone[9] = count['N']/2;
		count['N'] -= phone[9];
		count['I'] -= phone[9];
		count['N'] -= phone[9];
		count['E'] -= phone[9];
		phone[3] = count['R'];
		count['T'] -= phone[3];
		count['H'] -= phone[3];
		count['R'] -= phone[3];
		count['E'] -= phone[3];
		count['E'] -= phone[3];
		phone[8] = count['E'];

		cout<<"Case #"<<t+1<<": ";
		for(int i = 0; i < 10; i++){
			for(int j = 0; j < phone[i]; j++) cout<<i;
		}
		cout<<endl;


	} 


	return 0;

}
