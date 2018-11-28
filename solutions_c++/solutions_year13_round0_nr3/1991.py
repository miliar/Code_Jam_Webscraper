#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

long long ar[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	long long a,b;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int count=0;
		cin>>a>>b;
		for (int j = 0; j < 39; j++)
		{
			if(ar[j]>=a&&ar[j]<=b){
				count++;
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	

}

/*
bool isIntPalindrome(long long a){
	long long b=a,c=0;
	while(b>0){
		c*=10;
		c+=b%10;
		b/=10;
	}
	if(a==c)return true;
	return false;
}



int main(){
	freopen("in.txt","r",stdin);
	freopen("outTmp.txt","w",stdout);
	cout<<"{";
	for (long long i = 1; i <= 10000000; i++)
	{
		if(isIntPalindrome(i)){
			if(isIntPalindrome(i*i)){
				cout << i*i <<",";
			}
		}
	}
	cout<<"}";
}
*/