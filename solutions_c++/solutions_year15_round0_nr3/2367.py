#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

///////////////////////////////////////////////////
int do_eval(int a, int b, int product[5][5]){
	int sign = (a*b)/abs(a*b);
	return product[abs(a)][abs(b)]*sign;
}

///////////////////////////////////////////////////
int firstfirst(int a, int b, int product[5][5]){
	if (a==1 || a==-1) return b*a;
	else return do_eval(b, -a, product);  
}

///////////////////////////////////////////////////
int pow_func(int a1, int m){
	if (m == 0) return 1;
	else if (m == 1) return a1;
	else if (m == 2) return ((a1==1 || a1==-1) ? 1 : -1);
	else if (m == 3) return ((a1==1 || a1==-1) ? a1 : -a1);
}

///////////////////////////////////////////////////
int firstsecond(int a, int b, int product[5][5]){
	if (a == 1 || a == -1) return b*a;
	else return do_eval(-a, b, product);
}

int main(){
	int test;
	cin>>test;
	for(int tc=1; tc<=test; tc++){
		int l;
		long long c;
		cin>>l>>c;
		char buffer[10005];
		scanf("%s", buffer); 
		vector<int> inp(l,1);
		int product[5][5] = {{1, 1, 1, 1, 1},
						{1, 1, 2, 3, 4}, 
						{1, 2, -1, 4, -3}, 
						{1, 3, -4, -1, 2}, 
						{1, 4, 3, -2, -1}};
						
		for(int i=0; i<l; i++) inp[i] += buffer[i] - 'i' + 1;
    
		vector<int> rem_val(l + 1, 0);
		rem_val[0] = 1;
		for(int i=0; i<l; i++){
			int sign = rem_val[i] / abs(rem_val[i]);
			rem_val[i + 1] = product[abs(rem_val[i])][inp[i]] * sign;
		}
    
		vector<int> rem_back(l+1, 0);
		rem_back[l] = 1;
		
		///////////////////////////////////////////////////
		for(int i = l-1; i > -1; i--){
			int sign = rem_back[i + 1] / abs(rem_back[i + 1]);
			rem_back[i] = product[inp[i]][abs(rem_back[i + 1])] * sign;
		}    
    
		int check_var = 0;
		int ttal = rem_val[l];
		int rem = ((c - 1) % 4);

		///////////////////////////////////////////////////
		// Case 1 : Splits twice
		for(int n1=0; n1<4; n1++){
			for(int n2=0; n2<4; n2++){
				if((n1 + n2)<=(c - 1) && (n1 + n2) % 4 == rem){
					int v1 = pow_func(ttal, n1);
					int v2 = pow_func(ttal, n2);
					v1 = firstsecond(v1, 2, product);
					v2 = firstfirst(v2, 4, product);
					int pos1 = l, pos2 = 0;
					for(int i=0; i<=l; i++){
						if (rem_val[i] == v1){
							pos1 = i;
							break;
						}
					}
					
					for(int i=l; i > -1; i--){
						if (rem_back[i] == v2){
							pos2 = i;
							break;
						}
					}
	  
					if (pos1 < pos2){
						int y = firstfirst(v2, ttal, product);
						y = firstsecond(v1, y, product);
						if (y == 3){
							check_var = 1;
							break;
						}
					}
				}
			}
			
			if (check_var) break;
		}
		///////////////////////////////////////////////////
		// Case 2: Different blocks split
		if (!check_var && c >= 2){

			rem = ((c - 2) % 4);
			for(int n1=0; n1<4; n1++){
				for(int n2=0; n2<4; n2++){
					for(int n3=0; n3<4; n3++){
						if ((n1 + n2 + n3) <= c - 2 && (n1 + n2 + n3) % 4 == rem){
							
							int v1 = pow_func(ttal, n1);
							int v2 = pow_func(ttal, n2);
							int v3 = pow_func(ttal, n3);
							
							v1 = firstsecond(v1, 2, product);
							v3 = firstfirst(v3, 4, product);
							
							int pos1 = -1, pos2 = -1;
							for(int i=0; i<=l; i++){
								if (rem_val[i] == v1){
									pos1 = i;
									break;
								}
							}
							for(int i=0; i<=l; i++){
								if (rem_back[i] == v3){
									pos2 = i;
									break;
								}
							}
							
							if (pos1>-1 && pos2>-1){
								v1 = firstsecond(v1, ttal, product);
								v3 = firstfirst(v3, ttal, product);
		
								if(do_eval(v1, do_eval(v2, v3, product), product) == 3){
									check_var = 1;
									break;
								}
							}
						}
					}
					if (check_var) break;
				}
				if (check_var) break;
			}
		}

		if(check_var) cout<<"Case #"<<tc<<": YES\n";
		else cout<<"Case #"<<tc<<": NO\n";
	}
}
