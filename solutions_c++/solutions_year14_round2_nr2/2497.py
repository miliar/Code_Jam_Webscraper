#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int numOfCases = 0;
vector <string> dataString;
string tmp;
int main(){
	freopen("C:\\input.in","r",stdin);
	freopen("C:\\output.out","w",stdout);
	cin >> numOfCases;
	for(int n=0;n<numOfCases;n++){
	int a,b,k,sum=0;
	cin >> a >> b >> k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				sum++;
	cout<<"Case #"<<n+1<<": "<<sum<<endl;
	}
	getchar();
	return 0;
}