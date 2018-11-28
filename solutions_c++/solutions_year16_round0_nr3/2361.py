#include <bits/stdc++.h>
using namespace std;
int a, b;
long long int value;
char entrada[1000];
char * pEnd;
vector<long long int> v;


void bt(int i, int tam){
	if(i == tam){
		if(b==0) return;
		for(int j=2; j<=10; j++){
			value = strtol (entrada,&pEnd,j);
			int flag = 1;
			for(int k=2; k <= sqrt(value); k++){
				if(value%k == 0){v.push_back(k); flag = 0; break;}
			}
			if(flag){v.clear(); return;}
		}
		printf("%s", entrada);
		for(int j=0; j<v.size(); j++){
			printf(" %lld", v[j]);
		}
		puts("");
		v.clear();
		b--;
	}else{
		if(i==0){
			entrada[i] = '1';
			bt(i+1,tam);
		}else if(i==tam-1){
			entrada[i] = '1';
			bt(i+1,tam);
		}else{
			entrada[i] = '0';
			bt(i+1,tam);
			entrada[i] = '1';
			bt(i+1,tam);
		}
	}
}

int main()
{
	int n, cont=0;
	scanf("%d", &n);
	while(++cont <= n){
		scanf("%d %d", &a, &b);
		printf("Case #%d:\n", cont);
		bt(0,a);
	}
    
    return 0;
}