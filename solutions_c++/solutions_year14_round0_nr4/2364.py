#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <math.h>
using namespace std;
int main()
{
	long long i,j,k,l,m,n,t,count,reach[1005],count1;
	double A[1005],B[1005];
	freopen("d1.in","r",stdin);
	freopen("output5.txt","w",stdout);
	cin>>t;
	for(i = 1; i <= t; i++){
		cin>>n;
		count = 0;
		count1 = 0;
		for(j = 0; j < n; j++)
		cin>>A[j];
		for(j = 0; j < n; j++)
		cin>>B[j];
		sort(A,A+n);
		sort(B,B+n);
		for(j = 0; j < n; j++)
		reach[j] = 0;
		l = n;
		for(j = 0; j < n; j++){
			for(k = 0; k < n; k++){
				if(A[j] < B[k] && reach[k] == 0){
					reach[l-1] = 1;
					count++;
					l--;
					break;
				}
				else if(A[j] > B[k] && reach[k] == 0){
					reach[k] = 1;
					break;
				}
			}
		}
		memset(reach,0,sizeof(reach));
		for(j = 0; j < n; j++){
			for(k = 0; k < n; k++){
				if(A[j] < B[k] && reach[k] == 0){
					reach[k] = 1;
					count1++;
					break;
				}
				
			}
		}
		cout<<"Case #"<<i<<": "<<n-count<<" "<<n-count1<<endl;
		
	}
	return 0;
}

