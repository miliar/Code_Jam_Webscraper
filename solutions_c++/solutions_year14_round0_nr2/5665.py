#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <memory.h>
#include <fstream>
using namespace std;

int order1[4][4];
int order2[4][4];
//char filename[] = "D:\\Users\\lenovo\\Desktop\\test.txt";
//ofstream fout(filename,ios::app);
int main(){
	int N;
	cin>>N;
	for(int n=1;n<=N;n++){
		double C;//农场价格 500 10000
		double F;//额外收入 4 100
		double X;//获胜条件 2000 100000
		cin>>C>>F>>X;
		double money=0;
		double time=0;
		double speed=2;
		while(true){
			if(X/speed<=(C/speed)+(X/(speed+F))){
				time+=X/speed;
				break;
			}else{
				time+=C/speed;
				speed+=F;
			}
		}
		cout<<"Case #"<<n<<": ";
		//fout<<"Case #"<<n<<": ";
		cout<<fixed<<setprecision(7)<<time<<endl;
		//fout<<fixed<<setprecision(7)<<time<<endl;
	}
	return 0;
}
