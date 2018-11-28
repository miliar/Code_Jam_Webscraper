#include<iostream>
	#include<iomanip>
using namespace std;
int main(){
	int T;
	double C,F,X;
	double min_ans,current_ans;
	cin >> T;
	
	for(int i=0;i<T;i++){
		cin >> C >> F >> X;
		//cout << C <<" "<<F<<" "<<X<<endl;
		min_ans = 1.0*X/2;
		int iter=1;
		while(1){
			current_ans = 0;
			for(int j=0;j<iter;j++){
				current_ans += 1.0*C/(2+F*j);
			}
			current_ans += 1.0*X/(2+F*iter);
			if(current_ans < min_ans){
				 min_ans = current_ans;
				 iter++;
			}
			else
				break;
		}
		cout << "Case #" << i+1 << ": ";
		cout << fixed << setprecision(7) << min_ans << endl;

	}
	return 0;
}
