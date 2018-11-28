#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int N,n,i,j,k,m;
int cou=0;
vector<int> is(10);

void get_count(){
	j=n;
	while(j>0){
		i=j%10;
		if(is[i]==0){
			is[i]=1;
			cou++;
		}
		j=j/10;
	}
	return;
}

int main(int argc, char const *argv[])
{
	cin>>N;
	for (int ii = 1; ii <= N; ++ii)
	{
		scanf("%d",&m);
		if(m!=0){
			k=1;
			while(1){
				n=m*k;
				get_count();
				if(cou==10)
					break;
				k++;
			}
			printf("Case #%d: %d\n",ii,n);
			for (int i = 0; i < 10; ++i){
				cou=0;
				is[i]=0;
			}
		}
		else{
			printf("Case #%d: INSOMNIA\n",ii);
		}
	}
	return 0;
}