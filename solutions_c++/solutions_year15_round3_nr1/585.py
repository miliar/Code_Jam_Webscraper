/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;
typedef long long LL;
/*
 * ����Ǹ�����
 * ֧��short��int��long��long long������(�޸�typec����)��
 * �÷�typec a = get_int();����-1��ʾ�������
 */
typedef int typec;
typec get_int() {
	typec res = 0, ch;
	while (!((ch = getchar()) >= '0' && ch <= '9')) {
		if (ch == EOF)
			return -1;
	}
	res = ch - '0';
	while ((ch = getchar()) >= '0' && ch <= '9')
		res = res * 10 + (ch - '0');
	return res;
}
//��������(�������������ʲ���ͨ������ֵ�ж��Ƿ����뵽EOF�������������뵽EOFʱ������-1)���÷�int a = get_int2();
int get_int2() {
	int res = 0, ch, flag = 0;
	while (!((ch = getchar()) >= '0' && ch <= '9')) {
		if (ch == '-')
			flag = 1;
		if (ch == EOF)
			return -1;
	}
	res = ch - '0';
	while ((ch = getchar()) >= '0' && ch <= '9')
		res = res * 10 + (ch - '0');
	if (flag == 1)
		res = -res;
	return res;
}
/**
 * ����һ���ַ�����str�У���scanf("%s", str)���ƣ�
 * ����Ե��������еĿհ��ַ�������ֵΪ�����ַ���
 * �ĳ��ȣ�����-1��ʾ���������
 */
int get_str(char *str) {
	char c;
	while ((c = getchar()) <= ' ') {
		if(c == EOF) {
			return -1;
		}
	}
	int I = 0;
	while (c > ' ') {
		str[I++] = c; c = getchar();
	}
	str[I] = 0;
	return I;
}

int main() {
	int T = get_int();
	int r, c, w;
	for (int t = 1; t <= T; t++) {
		r = get_int();
		c = get_int();
		w = get_int();
		int ret = c / w * r + w - 1;
		if (c % w != 0) {
			ret++;
		}
		printf("Case #%d: %d\n", t, ret); 
	}
	return 0;
}


