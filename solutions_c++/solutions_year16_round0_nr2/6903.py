#include<iostream>
#include<vector>
using namespace std;

void reverse(vector<int> &list, int begin, int end){
	int tmp;
	for (int i = 0; i < (end-begin)/2; ++i){
		tmp = list.at(i+begin);
		list.at(i) = 1-list.at(end - i-1);
		list.at(end - i - 1) =1-tmp;
	}
	if ((end - begin) % 2 != 0){
		list.at((begin + end) / 2) = 1 - list.at((begin + end) / 2);
	}
}
int flip(vector<int> &list, int begin, int end){
	int fliptimes = 0;
	if (begin >= end){
		return 0;
	}
	int i = end - 1;
	if (list.at(end - 1) == 1){
		while(i>=begin&&list.at(i) == 1){
			--i;
		}
		return flip(list, begin, i + 1);
	}
	else if (list.at(end - 1) == 0 && list.at(begin)==0){
		reverse(list, begin, end);
		++fliptimes;
		return fliptimes + flip(list, begin, end);
	}
	else if (list.at(end - 1) == 0 && list.at(begin) == 1){
		int k = begin;
		while (k<(end-1)&&list.at(k) == 1){
			list.at(k) = 0;
			++k;
		}
		++fliptimes;
		return fliptimes + flip(list, begin, end);
	}
}
int main(){
	int t;
	char pan[100];
	char happy = '+'; 
	char blank = '-';
	cin >> t;
	for (int i = 0; i < t; ++i){
		vector<int> list;
		cin >> pan;
		for (unsigned int j = 0; j < strlen(pan);++j){
			if (pan[j]==happy){
				list.push_back(1);
			}
			else if (pan[j] == blank){
				list.push_back(0);
			}
		}
		int count = flip(list, 0, list.size());
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	
	system("pause");
	return 0;
}