#include <iostream>
#include <fstream>

using namespace std;

int *N,T;
bool test[10];

void ghiFile(int h,int cas){
	ofstream fg;
	fg.open("output.out", ios::app);
	fg << "Case #"<<cas<<": "<<h<<endl;
	fg.close();
}
void ghiFile2(int cas){
	ofstream fg;
	fg.open("output.out", ios::app);
	fg << "Case #"<<cas<<": "<<"INSOMNIA"<<endl;
	fg.close();
}
void read(){
	ifstream fd;
	fd.open("A-large.in",ios::in);
	fd >> T;
	N=new int[T];
	for(int g=1;g<=T;g++){
		fd>>N[g];
	}
}
void Init(){
	for(int i=0;i<10;i++){
		test[i]=false;
	}
}
void hienThi(){
	cout <<T<<endl;
	for(int g=1;g<=T;g++){
		cout <<N[g]<<endl;
	}
}
void digit(int a){
	int temp;
	while(a>=10){
		temp=a%10;
		a=a/10;
		test[temp]=true;
	}
	test[a]=true;
}
bool testN(){
	for(int i=0;i<10;i++){
		if(test[i]==false) return false;
	}
	return true;
}
void xuLy(){
	int dem,temp;
	for(int i=1;i<=T;i++){
		dem=1;
		if(N[i]==0){
			ghiFile2(i);
			continue;
		}
		temp = N[i]*dem;
		digit(temp);
		while(testN()==false){
			temp = N[i]*dem;
			dem++;
			digit(temp);
		}
		Init();
		ghiFile(temp,i);
	}
}
int main(){
	Init();
	read();
	xuLy();
	system("pause");
}
