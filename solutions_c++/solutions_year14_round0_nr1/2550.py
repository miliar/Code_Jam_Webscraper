#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <math.h>
using namespace std;
int main()
{
	int i,j,k,l,m,n,t,A[105][105],B[105][105],C[20],count1,count2;
	freopen("a.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(k = 1; k <= t; k++){
		cin>>n;
		count1 = 0;
		count2 = 0;
		memset(C,0,sizeof(C));
		for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
		cin>>A[i][j];
		cin>>m;
		for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
		cin>>B[i][j];
		n--;
		m--;
		for(i = 0; i < 4; i++)
		C[A[n][i]]++;
		for(i = 0; i < 4; i++)
		C[B[m][i]]++;
		for(i = 1; i <= 16; i++){
			if(C[i] == 1)
			count1++;
			if(C[i] == 2)
			count2++;
		}
		if(count1 == 8)
		cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		else if(count2 == 1){
			for(i = 1; i <= 16; i++){
				if(C[i] == 2)
				break;
			}
			cout<<"Case #"<<k<<": "<<i<<endl;
		}
		else if(count2 > 1)
		cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		
	}
	return 0;
}

