#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <valarray>

using namespace std;

#define ALL(v) (v).begin(),(v).end()
typedef pair<int,int> pii;

int num[1024];
int tam;
int to_base(long long int n,int b,int *num){
	
	if(n == 0){
		num[0] = 0;
		return 1;
	}
	
	int tam = 0;
	
	while(n){
		num[tam++] =n%b;
		n /=  b;
	}
	return tam;
}

bool isP(long long int x){
	int tam = to_base(x,10,num);
	for(int i=0;i<tam/2;i++)
		if(num[i] != num[tam-i-1]) return false;
	return true;
}

int main(){
	int teste,nteste;
	long long int a,b;
	vector<long long int> sfp;
	long long int inic;
	
	a = inic = 1;
	b = 100000000000000; // 10^14
	while(inic*inic <= b){
		if(isP(inic) && isP(inic*inic))
			sfp.push_back(inic*inic);
		inic++;
	}
	
	scanf("%d",&nteste);
	for(teste = 1; teste <= nteste; teste++){
		
		scanf("%lld %lld",&a,&b);
		
		int resp=0;
		for(int i=0;i<sfp.size();i++)
			if(sfp[i] >= a && sfp[i] <= b) resp++;
			
		printf("Case #%d: %d\n",teste,resp);
	}	
}
