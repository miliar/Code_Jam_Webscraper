// Cookie Cliker Alpha.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

using namespace std;

//������������Ϊ 2 cookies/s
double C = 0.0;//ũ���ļ۸���cookie��������
double F = 0.0;//ũ���Ĳ�����cookies/s
double X = 0.0;//�ռ�Ŀ�꣬���ӵ�е�cookie����

double cookie_clicker_alpha();

//�����ȡ���룬�������
int _tmain(int argc, _TCHAR* argv[])
{
	int num = 0; //����test case������
	ifstream input("d:\\Code jam\\Cookie Cliker Alpha\\B-small-attempt0.in");
	ofstream output("d:\\Code jam\\Cookie Cliker Alpha\\B-small-attempt0.out");
	double result = -1.0;
	char buffer[100];
	
	if(!input) {
		cerr << "error: unable to read input!" << endl;
		return -1;
	}

	input >> num;

	for(int i = 1;i <= num;i++) {
		input >> C >> F >> X;
		result = cookie_clicker_alpha(); 
		sprintf(buffer, "%.7f", result);
		output << "Case #" << i << ": " << buffer << endl;
	}
	
	return 0;
}

//����������n��cookie farm����ʱ�� n>=0
//��Ϊ�󲻳����к͵�ͨ�ʽ������ֻ���õ�����
double t(int n) {
	
	double t = 0.0;

	for(int k = 0;k <= n-1;k++) {
		t += C / (2 + k * F);
	}

	return t;

}

//���㽨n��cookie farm�Ա����Ŀ���������ʱ��
double y(int n) {

	double y = 0.0;

	y = t(n) + X / (2 + n * F);
	return y;
}

//��������������
//��������������� C F X ����ռ���X��cookie��������ʱ��
//��ʱ��y�Ǹ��ȵ����ݼ����ٵ��������ĺ�������������ҵ���Сֵ��
//��Ϊ�޷����y����n�ı��ʽ������ֻ��ö��n��ֱ��y���ֵ���Ϊֹ
double cookie_clicker_alpha() {
	
	double min_y = -1.0;
	double tem_y = y(0);
	bool increased = false;
	int n = 1;
	
	while(!increased) {
		min_y = tem_y;
		tem_y = y(n);
		increased = (tem_y > min_y) ? true : false;
		n++;
	}

	return min_y;
}