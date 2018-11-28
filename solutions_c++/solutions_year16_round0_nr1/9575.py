#include <bits/stdc++.h>

using namespace std;

bool mark[11];

bool finished (int x){
	
	stringstream ss;
	ss << x;
	string o;
	ss >> o;

	for (int i=0;i<o.size();++i){
		mark[o[i]-'0']=true;
	}
	
	int cont=0;
	
	for (int i=0;i<10;++i){
		if (mark[i]) cont++;
	}
	
	return cont == 10;
}

int main(){
	
	int t;
	scanf("%d",&t);
	int caso=1;
	while (t--){
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",caso++);
		memset(mark,0,sizeof(mark));
		if (n==0) printf("INSOMNIA\n");
		else{
			int k=1;
			n*=k;
			
			while (!finished(n*k)){
				k++;
			}
			printf("%d\n",n*k);
		}
		
		
	}

	return 0;
}
