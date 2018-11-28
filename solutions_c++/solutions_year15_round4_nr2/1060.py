#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>

using namespace std;

#define MAXN 128
#define	EPS 1e-12
double R[MAXN], C[MAXN];
double X, V;  

int main(){
	int T;
	cin >> T;
	for(int k=0; k<T; k++){
		int N;
		cin >> N;
		cin >> V >> X;
		for(int i=0; i<N; i++)
			cin >> R[i] >> C[i]; 

		cout << "Case #" << (k+1) << ": ";

		cout << std::fixed;
		cout.precision(7);
		if(N==1){
			if(abs(C[0]-X)> EPS)
				cout << "IMPOSSIBLE\n";
			else cout << (V/R[0]) << "\n";
		}else if(N==2){
			if(abs(C[1]-C[0])>EPS){
				double t1, t2;
				t2 = V*(X-C[0])/(R[1]*(C[1]-C[0]));
				t1 = (V-t2*R[1])/R[0];
				t1=t1+EPS;
				t2=t2+EPS;
				
				if( t1 < 0 || t2 < 0 ) 
					cout << "IMPOSSIBLE\n";
				else
					cout << max(t1,t2) << "\n";
			}else if(abs(X-C[0]) < EPS)
				cout << (V/(R[0]+R[1])) << "\n";
			else
				cout << "IMPOSSIBLE\n";
		}
			

	}
}
