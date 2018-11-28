#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;



char table[128][128];
bool neg[128][128];

char prefix[10001];
bool prefix_neg[10001];

vector <int> i_pos;

void init(){
	char i = 'i', j = 'j', k = 'k';
	
	table[i][i] = 1;
	table[j][j] = 1;
	table[k][k] = 1;
	table[i][j] = table[j][i] = k;
	table[i][k] = table[k][i] = j;
	table[k][j] = table[j][k] = i;
	table[i][1] = table[1][i] = i;
	table[j][1] = table[1][j] = j;
	table[k][1] = table[1][k] = k;

	neg[i][i] = neg[j][j] = neg[k][k] = true;
	neg[i][k] = neg[j][i] = neg[k][j] = true;
}

void prefix_cal(const string &str){
	prefix[0] = str[0];
	if(prefix[0] == 'i') 
		i_pos.push_back(0);
	
	int len = str.length();
	for(int i = 1; i < len; ++i){
		char a = prefix[i-1];
		char b = str[i];
		
		prefix[i] = table[a][b];
		prefix_neg[i] = prefix_neg[i-1] ^ neg[a][b];
		//printf("%d -> %d , %d\n", i, prefix_neg[i-1], neg[a][b]);	
		if(prefix[i] == 'i'  && !prefix_neg[i])
			i_pos.push_back(i); 
	}
/*
	printf("prefix = ");
	for(int i = 0; i < len; ++i)
		if(prefix[i] == 1)	printf(" 1");
		else	printf("%2c", prefix[i]);
	printf("\n");
	printf("prefix = ");
	for(int i = 0; i < len; ++i)
		printf("%2d", prefix_neg[i]);
	printf("\n");
		
	for(int i = 0; i < i_pos.size(); ++i){
		printf("pos[%d] = %d\n", i, i_pos[i]);
	}
*/
}

bool is_one(char x, char y){
	return x == 1 || y == 1;
}

bool check_ijk(int len){
	int n = i_pos.size();
	for(int i = 0; i < n; ++i){
		int a = i_pos[i];
		for(int b = a + 1; b < len - 1; ++b){
			int c = len-1;
			
			char j, k;
			bool neg_j, neg_k;

			char p_a = prefix[a];
			char p_b = prefix[b];
			char p_c = prefix[c];

			j = table[p_a][p_b];
			neg_j = prefix_neg[a] ^ prefix_neg[b] ^ 
					neg[p_a][p_b] ^ 1;
			if( is_one(p_a, p_b))
				neg_j ^= 1;

			if( neg_j != 0 || j != 'j' )	continue;
			
			//printf("%d pa %c->%d, pb %c->%d here!!\n", b, p_a, prefix_neg[p_a], p_b, prefix_neg[p_b]);
				
			k = table[p_b][p_c];

			if( k == 1 && prefix[c] == 1){
				neg_k = prefix_neg[b] ^ prefix_neg[c] ^
						neg[p_b][p_c] ;
			}
			else{
				neg_k = prefix_neg[b] ^ prefix_neg[c] ^
						neg[p_b][p_c] ^ 1 ;
			}
//			printf("k = %d, neg_k = %d\n", k, neg_k);

			if( neg_k != 0 || k != 'k' )	continue;
			return true;	
		}
	}
	return false;
}

int CASE = 0;

int main(){

	init();

	int T;
	cin >> T;
	while( T-- ){
		memset(prefix , 0, sizeof(prefix));
		memset(prefix_neg, 0 ,sizeof(prefix_neg));
		i_pos.clear();

		int X, L;
		string str, in;
		cin >> L >> X;
		cin >> in;

		str = "";
		for(int i = 0; i < X; ++i){
			str.append(in);
		}
		
//		cout << "-----" << str << endl;

		prefix_cal(str);
		cout << "Case #" << ++CASE << ": ";
		if( check_ijk(str.length()) ){
			cout << "YES" << endl;
		}
		else{
			cout << "NO" << endl;
		}
	}

	return 0;
}
