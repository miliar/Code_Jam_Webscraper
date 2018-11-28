#include <iostream>
#include <string>

using namespace std;

int table_n [4][4] = {{1,2,3,4},
				      {2,1,4,3},
                      {3,4,1,2},
                      {4,3,2,1}};

int table_sign [4][4] = {{1,1,1,1},
				         {1,-1,1,-1},
                         {1,-1,-1,1},
                         {1,1,-1,-1}};


struct quat{
	int n;
	int sign;
};	

quat multiply(quat x,quat y){
	quat res;
	res.n = table_n[x.n-1][y.n-1];
	res.sign = x.sign*y.sign*table_sign[x.n-1][y.n-1];
	return res; 
}

int main(){

	int T;
    cin >> T;
    for(int i = 1; i<= T; i++){
		int L,X;
		string str;
		cin >> L >> X;
		cin >> str;
		quat value;
		value.n=1;
		value.sign=1;
		for (int j=0; j<L; j++){
			quat aux;
			aux.sign = 1;
			char c = str[j];
			if (c == '1') aux.n=1;
			else if (c == 'i') aux.n=2;
			else if (c == 'j') aux.n=3;
			else if (c == 'k') aux.n=4;
			value = multiply(value,aux);
			//cout << value.n << endl;
			//cout << value.sign << endl << endl;
		}

		//cout << endl;
		quat value_copy = value;
		for (int j=1; j<X; j++){
			value = multiply(value,value_copy);
			//cout << value.n << endl;
			//cout << value.sign << endl << endl;
		}

		if (value.n!=1 || value.sign!=-1 || L*X<3){
			cout << "Case #" << i << ": NO" << endl;
			continue;
		}

		else{
			//Get i
			int iter=0;
			quat q_1;
			q_1.n = 1;
			q_1.sign = 1;
			while(iter<L*X){
				//cout << "iter= " << iter << endl;
				//cout << q_1.n << endl;
				//cout << q_1.sign << endl << endl;
				
				quat aux;
				aux.sign = 1;
				char c = str[iter%L];
				if (c == '1') aux.n=1;
				else if (c == 'i') aux.n=2;
				else if (c == 'j') aux.n=3;
				else if (c == 'k') aux.n=4;
				q_1 = multiply(q_1,aux);

				if (q_1.n==2 && q_1.sign==1) break; //If q_1=i
				else iter++;
			}
			if (L*X-iter < 2){
				cout << "Case #" << i << ": NO" << endl;
				continue;				
			}
			//Get k
			//cout << "i found" << endl;
			int kter=L*X-1;
			quat q_2;
			q_2.n = 1;
			q_2.sign = 1;
			while(kter>iter){
				//cout << "kter= " << kter << endl;
				//cout << q_2.n << endl;
				//cout << q_2.sign << endl << endl;
				
				quat aux;
				aux.sign = 1;
				char c = str[kter%L];
				if (c == '1') aux.n=1;
				else if (c == 'i') aux.n=2;
				else if (c == 'j') aux.n=3;
				else if (c == 'k') aux.n=4;
				q_2 = multiply(aux,q_2); //Multiply on the left
			
				if (q_2.n==4 && q_2.sign==1) break;
				else kter--;
			}
			if (kter-iter<1){
				cout << "Case #" << i << ": NO" << endl;
				continue;				
			}
			cout << "Case #" << i << ": YES" << endl;
		}		
	}
	return 0;
}
