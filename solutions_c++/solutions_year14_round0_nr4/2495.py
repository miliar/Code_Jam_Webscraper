#include<iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#include <string>
#include <set>
#include <sstream>
#include<fstream>
using namespace std;
int main() {
	freopen("D-large.in","r",stdin);
freopen("out234.out","w",stdout);
long long 	int t, n, test,i, j, War, DW;
	float array1[1000], array2[1000];
	cin>>t;
for(long long int test=1;test<=t;test++){
		cin>>n;
		for(i=0;i<n;++i)
		cin>>array1[i];
		for(i=0;i<n;++i)
		cin>>array2[i];
		sort(array1,array1+n);
		sort(array2,array2+n);
		i=0,j=0;
		DW=0;
		while(i<n){
			if(array1[i]>array2[j]){
				j++;
				DW++;
			}
			i++;
		}
		i=0,j=0;
		War=0;
		while(i<n){
			if(j==n) 
			break;
			if(array1[i]<array2[j]){
				War--;
				i++;
			}
			j++;
		}
		War+=n;
		cout<<"Case #"<<test<<": "<<DW<<" "<<War<<endl;
	}
	return 0;
}
