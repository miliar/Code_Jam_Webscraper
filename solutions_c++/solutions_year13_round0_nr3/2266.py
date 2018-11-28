#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <string.h>
#include <stdlib.h>
#include <queue>

#define writeFile(name) freopen(name,"w",stdout)
#define readFile(name) freopen(name,"r",stdin)

using namespace std;

long long arr[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main(){
	readFile("in.in");
	writeFile("out.out");
	int T;
	cin >> T;
	for (int Z = 0; Z < T; Z++)
	{
		long long A,B;
		cin >> A >> B;
		long long c = 0;
		for (int i = 0; i < 39; i++)
		{
			if(arr[i] >= A && arr[i] <= B){
				c++;
			}
		}
		printf("Case #%d: %d\n",Z+1,c);
	}
}
/*
bool isFair(long long i){
	long long num = 0,num2 = i;
	while (num2)
	{
		num += num2 % 10;
		num2 /= 10;
		if(num2 > 0){
			num *= 10;
		}
	}
	return num == i;
}

int main(){
	readFile("in.in");
	writeFile("out.out");
	cout << "{";
	for (long long i = 1; i < 10000000; i++)
	{
		if(isFair(i)){
			if(isFair(i*i)){
				cout << i*i << ",";
			}
		}
	}
	cout << "}";
}
*/