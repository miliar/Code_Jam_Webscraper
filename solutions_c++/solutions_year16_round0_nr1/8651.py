#include <bits/stdc++.h>

using namespace std;

int t;
long long n,tmp,nn,x;
bool ind,proof;
int a[10];

int main(){
	int c;
	scanf("%d",&c);
	while(c--){
		cin>>n;
		memset(a,0,sizeof a);
		x = 1;
		ind = false;
		if(!n)
			ind = true;
		if(!ind){
			while(true){
				nn = n*x;			
				tmp = nn;
				while(tmp)
					a[tmp%10]++, tmp /= 10;
				proof = true;
				for(int i=0;i<10;i++)
					if(!a[i])
						proof = false;
				if(proof)
					break;
				x++;			
			}
		}
		if(ind)
			printf("Case #%d: INSOMNIA\n",++t);
		else
			cout<<"Case #"<<++t<<": "<<nn<<endl;
	}
	return(0);
}
