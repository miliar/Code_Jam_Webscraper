//by Naciraa
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void generate_string_len_n(int n, vector < string> &v, string s ){
	if(n == 0){
		v.push_back(s+"1");
	}else {
		generate_string_len_n(n-1, v, s+"0" );
		generate_string_len_n(n-1, v, s+"1" );
	}
}

long long int transform_to_base(string s,  int b){
	long long int res = 0;
	long long int aux = 1;
	for(int i = s.length()-1; i>=0; i--){
		if(s[i]=='1'){
			res = res + aux;
		}
		aux = aux * b;
	}
	return res;
}

long long int divisores( long long int num){
	for(long long int i = 2; i*i<=num; i++){
		if(num % i == 0){
			return i;
		}
	}
	return -1;
}
void validate_strings( vector< string> &v ){
	int cant = 0;
	for(int i = 0; i<v.size(); i++){
		vector< long long int> divisores_por_base;
		for(int j = 2; j<11 ; j++){
			//cout << "base: " << j <<endl;
			long long int basej = transform_to_base(v[i], j);
			//cout << "nro: " << basej << endl;
			long long int divisor = divisores(basej);
			//cout << "divisor: " << divisor <<endl;
			if(divisor != -1){
				divisores_por_base.push_back(divisor);
			}else{
				break;
			}
		}
		if (divisores_por_base.size() == 9){
			cout << v[i] ;
			for(int k = 0; k <divisores_por_base.size(); k++ ){
				cout << " " << divisores_por_base[k];
			}
			cout << endl;
			cant++;
		}
		if(cant == 50){
			break;
		}
	}
	
}
int main(){
	int t;
	t = 1;
	int curr_case = 1;
	while(curr_case <= t){
		int j,n;
		j = 50;
		n = 16;
		cout << "Case #" << curr_case << ":" << endl;
		vector < string> candidates;
		generate_string_len_n(n-2, candidates, "1");
		validate_strings( candidates );
		curr_case++;
	}
	
	return 0;
}