#include "iostream"
#include "cstdio"

using namespace std ; 

int n ; 
int cnt , v[10]; 
int T , ts; 

bool check(int x){
	while(x){
		if(!v[x % 10]) cnt -- , v[x % 10] = 1 ; 
		x /= 10;
	}
	return cnt == 0 ; 
}

int main(int argc, char const *argv[])
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin >> ts ; 
	for(int T = 1 ; T <= ts ; ++ T){
		cin >> n ; 
		cout << "Case #" << T << ": " ; 
		if(!n){
			cout << "INSOMNIA" << endl; 
			continue ; 
		}
		cnt = 10 ; 
		memset(v , 0 , sizeof v);
		for(int i = 1 ; ; ++ i)
			if(check(i * n)){
				cout << i * n << endl;
				break ;
			}
	}

	return 0;
}