// Cookie Cliker Alpha.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

using namespace std;

//基本经济收入为 2 cookies/s
double C = 0.0;//农场的价格，以cookie的数量记
double F = 0.0;//农场的产量，cookies/s
double X = 0.0;//收集目标，最后拥有的cookie数量

double cookie_clicker_alpha();

//负责读取输入，产生输出
int _tmain(int argc, _TCHAR* argv[])
{
	int num = 0; //保存test case的数量
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

//计算连续建n个cookie farm所需时间 n>=0
//因为求不出数列和的通项公式，所以只好用迭代法
double t(int n) {
	
	double t = 0.0;

	for(int k = 0;k <= n-1;k++) {
		t += C / (2 + k * F);
	}

	return t;

}

//计算建n个cookie farm以便完成目标所需的总时间
double y(int n) {

	double y = 0.0;

	y = t(n) + X / (2 + n * F);
	return y;
}

//求解问题的主程序
//根据三个输入参数 C F X 求出收集到X个cookie所需的最短时间
//总时间y是个先单调递减，再单调递增的函数，任务就是找到最小值点
//因为无法算出y关于n的表达式，所以只能枚举n，直到y出现递增为止
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