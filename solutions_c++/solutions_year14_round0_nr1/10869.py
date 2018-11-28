#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> leer(){
	int num,n;
	vector<int> v;

	scanf("%d", &num);
	for(int i=0; i<4; i++)
		for (int j=0; j<4; j++)
		{
			scanf("%d", &n);
			if(i==(num-1)) v.push_back(n);
		}

	return v;
}

int main(){
	freopen("A-small-attempt1.in","r",stdin);
    freopen("out","w",stdout);
	int cas, nu,k=1;
	vector<int> v1,v2;

	scanf("%d", &cas);

	while(cas--){
		v1=leer();
		v2=leer();

		sort(v1.begin(),v1.end());

		int c=0;
		for(int i=0;i<4;i++){
			if(binary_search(v1.begin(),v1.end(),v2[i])) c++, nu=v2[i];
		}
		
		printf("Case #%d: ", k++);
		if(c==0) printf("Volunteer cheated!\n");
		else if(c==1) printf("%d\n", nu);
		else if(c>1) printf("Bad magician!\n");
	}
}
