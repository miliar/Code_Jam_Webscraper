#include <iostream>
#include <cstdio>
#include <set>
using namespace std;


int main(){
	freopen("A-large.in","r",stdin);
	freopen("output-large.in","w",stdout);
	int testcases;
	scanf("%d",&testcases);
	for(int i=0;i<testcases;i++){
	int N,dN;
	set<int> s;
	scanf("%d",&N);
		if(N==0)
			printf("Case #%d: INSOMNIA\n",i+1);
		else{
			int j=1;
			while(s.size()!=10){
                dN=N*j;
				int lN=dN;
				j++;
				while(lN/10!=0){
					s.insert(lN%10);
					lN/=10;
				}
				s.insert(lN%10);
			}
			printf("Case #%d: %d\n",i+1,dN);


		}
	}




	return 0;
}
