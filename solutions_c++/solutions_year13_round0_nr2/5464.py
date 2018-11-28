#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	long long int a,i,b,c,count1,d,j,k,count,r,l;
	cin >> a;
	freopen ("myfile.txt","w",stdout);
	for(i=0;i<a;i++){
		cin >> b >> c;
		long long int arr[11][11],arr2[100];
		count1 = 0;
		for(j=0;j<b;j++){
			count = -1;
			for(k=0;k<c;k++){
				cin >> d;
				arr[j][k] = d;
				if(d > count){
					count = d;
				}
			}
			arr2[j] = count;
		}
		for(j=0;j<b;j++){
			r = arr2[j];
			for(k=0;k<c;k++){
				if(arr[j][k] != r){
					for(l=0;l<=b-2;l++){
						if(arr[l][k] != arr[l+1][k]){
							count1 = 1;
							break;
						}
					}
				}
				if(count1 == 1){
					break;
				}
			}
			if(count1 == 1){
				break;
			}
		}
		if(count1 == 1){
			cout << "Case #"<<(i+1) << ": NO" <<endl;
		}
		else{
			cout << "Case #"<<(i+1) << ": YES" <<endl;
		}
	}
	return 0;	
}
