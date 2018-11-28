#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;
char daignol(char a[][4]) {
	bool flag = true;
	char c;
		for(int l = 0; l < 4; l++) {
		//	cout << " Right " << a[l][l] <<  " "  <<a[l+1][l+1] <<" l+1 = " << l+1 << endl;
			if((l+1 <  4) && a[l][l] != '.' && a[l+1][l+1] != '.' && a[l][l] == a[l+1][l+1]) {
				c = a[l][l];   			
			}else{
				if((l+1 < 4) && (a[l+1][l+1] == 'T' || a[l][l] == 'T')){	
				
				}else{
					if(l+1 != 4){
						flag = false;
						break;
					}
				}
		}
	}
	
	if(flag == true) {
		return c;
	}else{
		flag = true;
		for(int l = 3,i = 0; l >= 0; l--,i++) {
	//		cout << " Left " << a[i][l] <<  " "  <<a[i+1][l - 1] <<" l - 1 = " << l-1 << endl;
			if((l - 1 >=  0) && a[i+1][l - 1] != '.' && a[i][l] != '.' && a[i + 1][l - 1] == a[i][l]) {
				c = a[i][l];   			
			}else{
				if((l - 1 >= 0) && (a[i+1][l - 1] == 'T' || a[i][l  - 1] == 'T')){	
				}else{
					if(l - 1 > 0) {
						flag = false;
					    break;
					}
													
				}
		}
	}
	if(flag == true){
		return c;
	}
	else{
		return 'K';
	}
  }
}
char vertical(char a[][4],int i) {
	char d;
	bool flag = true;
   for(int l = 0; l < 4; l++) {
				//cout << " Line " << a[l][i] <<  " "  <<a[l+1][i] <<" l+1 = " << l+1 << endl;
					if((l+1 <  4) && (a[l][i] != '.') && (a[l+1][i] != '.') && (a[l][i] == a[l+1][i])) {
						//cout << " Line " << a[i][l] <<  " "  <<a[i][l+1] << endl;
						d = a[l][i];					   			
					}else{
						if((l+1 < 4) && (a[l+1][i] == 'T' || a[l][i] == 'T')){	
						}else{
							if(l + 1 != 4){
								flag = false;
								break;
						}
					}
				}
	  }
				  if(flag == true) {
             			return d; 
				  }else{
  					return 'K';
  				}
						
 }
bool comp(char a[][4])
{
	for(int i = 0 ; i < 4; i++) {
		for(int j = 0 ; j < 4; j++) {
			if(a[i][j] == '.'){
				return true;
			}
		}
	}
	return false;
}
int main()
{
	int t;
	cin >> t;
	char a[4][4];
	vector<char> c;
	int count;
	bool flag;
	int pl = 1;
	while(t--) {
		for(int i = 0 ; i < 4; i++) {
			for(int j = 0 ; j < 4; j++){
				cin >> a[i][j];
				if(j == 3) {
					count = 0;
					flag = true;
					char d;
					for(int l = 0; l < 4; l++) {
						//cout << " Line " << a[i][l] <<  " "  <<a[i][l+1] <<" l+1 = " << l+1 << endl;
						if((l+1 <  4) && (a[i][l] != '.') && (a[i][l+1] != '.') && (a[i][l] == a[i][l+1])) {
							//cout << " Line " << a[i][l] <<  " "  <<a[i][l+1] << endl;
							d = a[i][l];					   			
						}else{
							if((l+1 < 4) && (a[i][l+1] == 'T' || a[i][l] == 'T')){	
							}else{
								if(l + 1 != 4){
									flag = false;
									break;
								}
							}
						}
					}
					
					if(flag == true) {
						c.push_back(d);
					}
				}
			}
		}
	//	cout << c.size() << endl;
		for(int i = 0 ; i < 4; i++) {
			char n = vertical(a,i);
			if(n != 'K') {
				c.push_back(n);
				break;
			}
		}
	//	cout << c.size() << endl;
		if(c.size() == 0) {
			char  m,n;
			m = daignol(a);
			if(m != 'K'){
				cout << "Case #" << pl << ": " << m << " won\n";
			}else if(comp(a)){
				cout << "Case #" << pl << ": " << "Game has not completed\n";
			}else{
				cout << "Case #" << pl << ": " << "Draw\n";
			}
		}else{
				cout << "Case #" << pl << ": " << c[0] << " won\n";		
		}
		pl++;
		c.clear();
		 
	}
}