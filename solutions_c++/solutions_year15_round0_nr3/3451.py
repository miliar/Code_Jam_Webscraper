#include <iostream>
#include <utility>

using namespace std;
typedef unsigned long long int ull;
pair<int, char> quatern(char row, char column){
	if(row == '1'){
		if(column == '1') return make_pair<int, char>(1, '1');
		else if(column == 'i') return make_pair<int, char>(1, 'i');
		else if(column == 'j') return make_pair<int, char>(1, 'j');
		else return make_pair<int, char>(1, 'k');
	}else if(row == 'i'){
		if(column == '1') return make_pair<int, char>(1, 'i');
		else if(column == 'i') return make_pair<int, char>(-1, '1');
		else if(column == 'j') return make_pair<int, char>(1, 'k');
		else return make_pair<int, char>(-1, 'j');
	}else if(row == 'j'){
		if(column == '1') return make_pair<int, char>(1, 'j');
		else if(column == 'i') return make_pair<int, char>(-1, 'k');
		else if(column == 'j') return make_pair<int, char>(-1, '1');
		else return make_pair<int, char>(1, 'i');
	}else{
		if(column == '1') return make_pair<int, char>(1, 'k');
		else if(column == 'i') return make_pair<int, char>(1, 'j');
		else if(column == 'j') return make_pair<int, char>(-1, 'i');
		else return make_pair<int, char>(-1, '1');
	}
}


pair<int, char> operator*(pair<int, char>& oh, const char um){
	pair<int, char> ya = quatern(oh.second, um);
	ya.first *= oh.first;
	return ya;
}
bool possible_k(char str[], ull L, ull X, ull left){
	pair<int, char> ans = make_pair<int, char>(1, 'k');
	pair<int, char> now = make_pair<int, char>(1, str[left % L]);
	while(left < L*X){
		if(now == ans){
			left++;
			if(left == L*X)
				return true;
			else{
				ans.second = '1';
				now = make_pair(1, str[left % L]);
			}
		}else{
			left++;
			now = now * str[left % L];
		}
	}
	return false;
}
bool possible_j(char str[], ull L, ull X, ull left){
	pair<int, char> ans = make_pair<int, char>(1, 'j');
	pair<int, char> now = make_pair<int, char>(1, str[left % L]);
	while(left < L*X){
		if(now == ans){
			left++;
			return possible_k(str, L, X, left);
		}else{
			left++;
			now = now * str[left % L];
		}
	}
	return false;
}
bool possible(char str[], ull L, ull X){
	ull left = 0;
	pair<int, char> ans = make_pair<int, char>(1, 'i');
	pair<int, char> now = make_pair<int, char>(1, str[0]);
	while(left < L*X){
		if(now == ans){
			left++;
			return possible_j(str, L, X, left);
		}else{
			left++;
			now = now * str[left % L];
		}
	}
	return false;
}
int main(void){
	int times;
	ull L, X;
	char str[10001];
	cin >> times;
	for(int i = 0; i < times; i++){
		cin >> L >> X;
		cin >> str;
		if(L*X < 3){
			cout << "Case #" << i + 1 << ": NO" << endl;
		}else{
			if(possible(str, L, X))
				cout << "Case #" << i + 1 << ": YES" << endl;
			else
				cout << "Case #" << i + 1 << ": NO" << endl;
		}
	}
}
