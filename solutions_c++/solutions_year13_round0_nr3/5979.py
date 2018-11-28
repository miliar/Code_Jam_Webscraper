#include<iostream>
#include<fstream>

using namespace std;
int squrt(int num);
bool isPal(int num);
int main() {
	ofstream myfile;
	myfile.open ("c.out");
	ifstream myReadFile;
	myReadFile.open("c.in");
	int T;
	int a,b,counter;
	myReadFile >> T;
	for(int x= 1 ;x<=T;x++){
		counter=0;
		myReadFile >> a>>b;
		for(int j=a;j<=b;j++){
			if(isPal(j))
				if(isPal(squrt(j)) && squrt(j) !=-1 )
					counter++;
		}
		myfile<<"Case #"<<x<<": "<<counter<<endl;
	}
	myfile.close();
	myReadFile.close();
	return 0;
}
int squrt(int num){
	int sqr=1,x=1;

	while(sqr<=num){
		sqr = x*x;
		if(sqr==num)return x;
		x++;
	}
	return -1;
}
bool isPal(int num){
	if(num<10)return true;
	else if(num<100){
		if((float)num/11==num/11)return true;
	}
	else{
		int a[3];
		a[0] = num/100;
		a[1] =  (num-a[0]*100)/10;
		a[2] = (num-a[0]*100-a[1]*10);
		if(a[0]==a[2])return true;
	}
	return false;
}