// Fair and Square.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
using namespace std;

bool is_palindrome(int v);
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\C-small-attempt0.in");
	ofstream out("d:\\C-small-attempt0.out");
	int number_of_test_cases = 0;

	if(!in) {
		return 0;
	}
	//收集input文件中的数据
	in >> number_of_test_cases;
	for(int k=0;k<number_of_test_cases;k++) {
		int number_of_fair_and_square = 0;
		int A=0, B=0; //[A, B] 查询区间
		in >> A;
		in >> B;

		int sqrtA = ceil(sqrt((double)A));
		int sqrtB = floor(sqrt((double)B));
		for(int i=sqrtA; i<=sqrtB; ++i) {
			if(is_palindrome(i) && is_palindrome(i*i)) {
				number_of_fair_and_square++;
			}
		}
		out<< "Case #" << k+1 << ": " << number_of_fair_and_square << endl;
	}
	return 0;
}

bool is_palindrome(int v) {
	queue<int> q; //用来存储v的各个位的值
	int t = v;
	while(t > 0) {
		q.push(t%10);
		t /= 10;
	}
	t=0;//t即将变为v的逆序数
	while(!q.empty()) {
		t = t*10 + q.front();
		q.pop();
	}
	if(t == v)
		return true;
	else
		return false;
}