#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int cases;
	cin>>cases;
	for(int i=1; i<=cases; i++){
		int maxS;
		cin>>maxS;
		char c=getchar(); //gets space
		int needed=0;
		int paradas=0;
		c=getchar();
		paradas=c-'0';//Las que se paran porque si
		for(int j=1;j<=maxS; j++){
			c=getchar(); // gets first digit
			int howM=c-'0'; //Las que necesitan j
			if(howM!=0){
				if(paradas<j){
					int newneed=j-paradas;
					needed+=newneed;
					paradas+=newneed+howM;
					//cout<<'j'<<j<<" p"<<paradas<<endl;

				}
				else
					paradas+=howM;
			}
			//cout<<"needed"<<needed<<endl;
			
		}
		cout<<"Case #"<<i<<": "<<needed<<endl;
	}

	return 0;
}