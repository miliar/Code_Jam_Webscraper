#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<cstring>
#include<stdio.h>

using namespace std;

int main(){
	FILE* fp;
	FILE* fpo;
	fp = freopen("B-small-attempt0.in","r",stdin);
	fpo = freopen("output.txt","w",stdout);
	int a,b,k,t;
	cin >> t;

	for(int z =0;z<t;z++){
		int count = 0;
		cin >> a >> b >> k;
		for(int i =0 ; i < a ; i++)
			for(int j =0;j<b;j++){
				
				if ((i&j) < k)
					count += 1;
					
	//			cout << i << " " <<j << " " <<  (i&j)  << " " << count << endl;
			}
					
	cout << "Case #" << z+1 << ": " << count << endl;
		
	}
	
	fclose(fp);
	fclose(fpo);
	return 0;
}
