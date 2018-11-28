#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,n,size_n,flag;
	set<int> count_n;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>n;
		int copy_n=n;
		int i=0;
		flag=1;
		if(n==0){
			flag=0;
		}
		if(n<10)
			count_n.insert(n);
		while(count_n.size()!=10 && flag!=0){
			i++;
			n=i*copy_n;
			if(n<10)
				count_n.insert(n);
			else{
				int aux=n;
				while(aux>0){
					int tmp=aux%10;
					count_n.insert(tmp);
					aux/=10;
				}
			}
			
			//printf("%d\n", n);
		}
		if(flag==1)
			printf("Case #%d: %d\n",j,n );
		else
			printf("Case #%d: INSOMNIA\n",j);
		count_n.clear();
	}


	return 0;
}