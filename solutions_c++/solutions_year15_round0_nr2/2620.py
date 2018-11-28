#include <iostream>
#include <math.h>
using namespace std;
int din[10];

int findMin(int i){
	if(i==0)
		return 0;

	if(din[i]==0)
		return findMin(i-1);

	if(i<4)
		return i;


	int op = i;

	int back[10];
	for(int in=0;in<10;in++){
		back[in] = din[in];
	}

	int b=i/2;
	int a=floor(sqrt(i));


	for(int in=a;in<=b;in++){
		din[in]+=din[i];
		din[i-in]+=din[i];
		int op2 = din[i] + findMin(i-1);
		if(op2<op)
			op=op2;
		for(int in=0;in<10;in++){
			din[in] = back[in];
		}
	}




	
	return op;
}

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<T+1; caso++){
		for(int i=0;i<10;i++)
			din[i]=0;
		int D;
		cin >> D;
		for(;D>0;D--){ //recibi el input
			int P;
			cin >> P;
			din[P]++;
		}
		int min;

		for(int i=9;i>0;i--){
			if(din[i]!=0){
				min=findMin(i);
				break;
			}
		}

		cout << "Case #" << caso << ": " << min << endl;
	}
}