#include <iostream>
#include <fstream>
#include <string>

using namespace std;
ifstream in("D-large.in");
ofstream out("o4BIG2.txt");
int gwarsc = 0;
int gdwarsc = 0;
void docase(){
	int size;
	in >> size;
	double N[size];
	double K[size];
	for(int i = 0;i<size;i++){
		in >> N[i];
	}
	for(int i = 0;i<size;i++){
		in >> K[i];
	}
	double slave = 0;
	//First sort the arrays with insertion sort.
	for (int i = 1; i < size; i++) {
 		int j = i;
		while (j > 0 && N[j - 1] > N[j]) {
 			slave = N[j];
			N[j] = N[j - 1];
			N[j - 1] = slave;
 			j--;
 		}
	}
	for (int i = 1; i < size; i++) {
 		int j = i;
		while (j > 0 && K[j - 1] > K[j]) {
 			slave = K[j];
			K[j] = K[j - 1];
			K[j - 1] = slave;
 			j--;
 		}
	}
	int warsc = 0;
	int dwarsc = 0;
	double NN[size];
	double KK[size];
	for(int i = 0;i<size;i++){
		NN[i] = N[i];
		KK[i] = K[i];
	}
	//for(int i = 0;i<size;i++){
	//	cout << NN[i] << endl;
	//}
	int index = 0;
	double least = 2;
	//Do war.
	for(int i = 0;i<size;i++){
		for(int j = 0;j<size;j++){
			if(K[j]>N[i] && K[j]<least){
				least = K[j];
				index = j;
			}
		}
		if(least ==2){
			warsc ++;
		}
		K[index] = 0;
		N[i] = 0;
		least = 2;
	}
	//Do dwar.
	int front = 0;
	int back = size-1;
	//Note that here we are iterating through Naomi's array.
	//Here is what I believe to be the winning strategy: Naomi essentially eats Ken from smallest to greatest. Start at the front (smallest). If Naomi's smallest is bigger than Ken's smallest, she says Ken+e to force him to use his
	//smallest. Therefore, she wins. However, if Ken's smallest is bigger than Naomi's smallest, she says largest-e to make him waste his largest. 
	for(int i = 0;i<size;i++){
		if(KK[front] > NN[i]){
			KK[back] = 0;
			NN[i] = 0;
			back--;
		}else{
			NN[i] = 0;
			KK[front] = 0;
			front++;
			dwarsc++;
		}
	}
	gdwarsc = dwarsc;
	gwarsc = warsc;
}
 
int main(){
	int T;
	in >> T;
	for(int i = 1;i<=T;i++){
		docase();
		out << "Case #" << i << ": " << gdwarsc << " " << gwarsc << "\n";
	}
	return 0;
}
