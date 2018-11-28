#include<iostream>
using namespace std;

char eval(char c1, char c2){
	if(c1 == '1'){
		return c2;
	}
	if(c2 == '1'){
		return c1;
	}
	if(c1 == c2){
		return '1';
	}
	if(c1 == 'i'){
		if(c2 == 'j'){
			return 'k';
		}
		if(c2 == 'k'){
			return 'j';
		}
	}
	if(c1 == 'j'){
		if(c2 == 'i'){
			return 'k';
		}
		if(c2 == 'k'){
			return 'i';
		}
	}
	if(c1 == 'k'){
		if(c2 == 'i'){
			return 'j';
		}
		if(c2 == 'j'){
			return 'i';
		}
	}
}

int evalSign(char c1, char c2){
	if(c1 == '1'){
		return 1;
	}
	if(c2 == '1'){
		return 1;
	}
	if(c1 == c2){
		return (-1);
	}
	if(c1 == 'i'){
		if(c2 == 'j'){
			return 1;
		}
		if(c2 == 'k'){
			return (-1);
		}
	}
	if(c1 == 'j'){
		if(c2 == 'i'){
			return (-1);
		}
		if(c2 == 'k'){
			return 1;
		}
	}
	if(c1 == 'k'){
		if(c2 == 'i'){
			return 1;
		}
		if(c2 == 'j'){
			return (-1);
		}
	}
}


int main(){
	ios_base::sync_with_stdio(false);	
	int t; cin>>t;
	for(unsigned int t1 = 1; t1 <= t; ++t1){
		cout<<"Case #"<<t1<<": ";
		long long int l,x;
		cin>>l>>x;
		char c[l];
		char result = '1'; int sign = 1;
		int pos1 = -1, pos2 = -1;
		for (unsigned int i = 0; i < l; i ++){
			cin>>c[i];
			
		}
		for (unsigned int i = 0; i < x; i ++){
			for (unsigned int j = 0; j < l; j ++){
				sign = sign * evalSign(result, c[j]);
				result = eval(result, c[j]);
				if(pos1 == -1){
					if(result == 'i' && sign == 1){
						pos1 = i*l + j;
					}
				}
			}
		}
		if(pos1 == -1){
			cout<<"NO"<<endl;
		}
		else if(result == '1' && sign == (-1)){
			//check for k from end
			sign = 1;
			for (int i = x-1; i >= 0; i --){
				for (int j = l-1; j >= 0; j --){
					sign = sign * evalSign(c[j], result);
					result = eval(c[j], result);
					if(result == 'k' && sign == 1){
						pos2 = i*l + j;
						break;
					}
				}
				if(pos2 != -1) break;
			}
			if(pos2 > pos1){
				cout<<"YES"<<endl;
			}
			else{
				cout<<"NO"<<endl;
			}
		}
		else {
			cout<<"NO"<<endl;	
		}
	}
	return 0;
}
