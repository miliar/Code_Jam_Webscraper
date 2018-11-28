#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int testCase;
	double C,F,X,current,partOfPre,next,index;
	cin>>testCase;
	for(int i=1;i<=testCase;i++){
		cin>>C>>F>>X;
		partOfPre = C/2;
		index = 1;
		current = X/2;
		next = C/2 + X/(F+2);
		while(next<current){
			current = next;
			index++;
			partOfPre = partOfPre + C/((index-1)*F+2);
			next = partOfPre + X/(index*F+2);
		}
		cout<<"Case #"<<i<<": ";
		cout<< fixed << setprecision(7) <<current<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}