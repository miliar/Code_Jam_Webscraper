#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
ifstream in("input.txt");
int T,A,B;

int isPal(int n){
    int temp=n,r,sum = 0;
    while(n){
         r=n%10;
         n=n/10;
         sum=sum*10+r;
    }
    return temp == sum;
}

int main(){
	in >> T;
	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		in >> A >> B;
		int s = 0;
		for(int i = 0;i <= 1000; i++)
			if(isPal(i) && isPal(i*i) && i*i>=A && i*i <=B ){
				s++;
			}
		cout << s << endl;
	}
	return 0;
}
