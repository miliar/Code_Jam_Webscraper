#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define pb push_back
#define eps 1e-7

using namespace std;
typedef long long ll;

int r, c, m;
char mat[55][55];

void print_mat(){
	fr(i, 0, r){
		fr(j, 0, c){
			printf("%c", mat[i][j]);
		}
		printf("\n");
	}
}

void r1(){
	int resto = c-m;
	if(resto < 2){
		printf("Impossible\n");
	}else{
		fr(i, 0, m){
			mat[0][i] = '*';
		}
		print_mat();
	}
}

void c1(){
	int resto = r-m;
	if(resto < 2){
		printf("Impossible\n");
	}else{
		fr(i, 0, m){
			mat[i][0] = '*';
		}
		print_mat();
	}
}

void r2(){
	if(m%2 != 0){
		printf("Impossible\n");
	}else{
		int resto = r*c-m;
		if(resto < 4){
			printf("Impossible\n");
		}else{
			fr(i, 0, m/2){
				mat[0][i] = mat[1][i] = '*';
			}
			print_mat();
		}
	}
}

void c2(){
	if(m%2 != 0){
		printf("Impossible\n");
	}else{
		int resto = r*c-m;
		if(resto < 4){
			printf("Impossible\n");
		}else{
			fr(i, 0, m/2){
				mat[i][0] = mat[i][1] = '*';
			}
			print_mat();
		}
	}
}

int main(){
	int t, caso = 1;
	scanf("%d", &t);
	
	while(t--){
		scanf("%d%d%d", &r, &c, &m);
		printf("Case #%d:\n" , caso++);
		
		fr(i, 0, r) fr(j, 0, c) mat[i][j] = '.';
		
		mat[r-1][c-1] = 'c';
		
		if(m == r*c-1){
			fr(i, 0, r) fr(j, 0, c) mat[i][j] = '*';
			mat[r-1][c-1] = 'c';
			print_mat();
			continue;
		}
		
		if(r == 1){
			r1();
			continue;
		}else if(c == 1){
			c1();
			continue;
		}else if(r == 2){
			r2();
			continue;
		}else if(c == 2){
			c2();
			continue;
		}
		
		if(m <= (r-2)*(c-2)){
			int q = m/(r-2), rest = m%(r-2);
			fr(j, 0, q){
				fr(i, 0, r-2){
					mat[i][j] = '*';
				}
			}
			fr(i, 0, rest){
				mat[i][q] = '*';
			}
			
			print_mat();
		}else{
			int branco = r*c-m;
			if(branco < 4 || branco == 5 || branco == 7){
				printf("Impossible\n");
			}else{
				fr(i, 0, r-2){
					fr(j, 0, c-2){
						mat[i][j] = '*';
					}
				}
				int resto = m-(r-2)*(c-2);
				int pos = 0;
				while(pos < c-3 && resto >= 2){
					mat[r-2][pos] = mat[r-1][pos] = '*';
					resto -= 2;
					pos++;
				}
				
				if(resto == 0){
					print_mat();
					continue;
				}else if(resto == 1){
					if(pos < c-3){
						mat[r-2][pos] = mat[r-1][pos] = '*';
					}else{
						mat[0][c-2] = mat[0][c-1] = '*';
					}
					mat[r-3][c-3] = '.';
					print_mat();
					continue;
				}
				
				
				pos = 0;
				while(pos < r-3 && resto >= 2){
					mat[pos][c-2] = mat[pos][c-1] = '*';
					resto -= 2;
					pos++;
				}
				
				//printf(">>> %d\n", resto);
				
				if(resto == 0){
					print_mat();
					continue;
				}else if(resto == 1){
					mat[pos][c-2] = mat[pos][c-1] = '*';
					mat[r-3][c-3] = '.';
					print_mat();
					continue;
				}else if(resto == 4){
					mat[r-3][c-2] = mat[r-3][c-1] = '*';
					mat[r-2][c-3] = mat[r-1][c-3] = '*';
					print_mat();
					continue;
				}else if(resto == 2){
					mat[r-3][c-2] = mat[r-3][c-1] = '*';
					print_mat();
					continue;
				}
				
			}
		}
		
	}

	return 0;
}

