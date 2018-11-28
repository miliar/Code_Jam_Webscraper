#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main(){
	//freopen("largein.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T,Smax,A[1003],cont = 1;
	scanf("%d",&T);
	string S;
	while(T--){
		scanf("%d",&Smax);
		cin>>S;
		for(int i = 0; i < S.size(); i++)
			A[i] = S[i] - '0';
		int Sac = 0, numfriends = 0;
		for(int shyness = 0; shyness <= Smax; shyness++){
			if(Sac >= shyness || A[shyness] == 0)
				Sac += A[shyness];
			else{
				numfriends += shyness - Sac;
				Sac += A[shyness] + (shyness -Sac);
			}
		}
		printf("Case #%d: %d\n",cont,numfriends);cont++;
	}
	return 0;
}