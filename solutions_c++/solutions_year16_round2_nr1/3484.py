#include <bits/stdc++.h>
using namespace std;
string nums[]={
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
char cnt[256];
void sub(int x,int d){
	for(int i=0;i<nums[x].length();++i)
		cnt[nums[x][i]]-=d;
}
void print(int d,int n){
	for(int i=0;i<n;++i){
		putchar('0'+d);
	}
}
int main(){
	int t;
	cin>>t;
	for(int z=1;z<=t;++z){
		string str;
		cin>>str;
		memset(cnt,0,sizeof cnt);
		for(int i=0;i<str.length();++i){
			++cnt[str[i]];
		}
		int n8=cnt['G'];
		sub(8,n8);
		int n6=cnt['X'];
		sub(6,n6);
		int n7=cnt['S'];
		sub(7,n7);
		int n4=cnt['U'];
		sub(4,n4);
		int n5=cnt['V'];
		sub(5,n5);
		int n9=cnt['I'];
		sub(9,n9);
		int n3=cnt['H'];
		sub(3,n3);
		int n2=cnt['T'];
		sub(2,n2);
		int n1=cnt['N'];
		sub(1,n1);
		int n0=cnt['Z'];
		sub(0,n0);
		printf("Case #%d: ",z);
		print(0,n0);
		print(1,n1);
		print(2,n2);
		print(3,n3);
		print(4,n4);
		print(5,n5);
		print(6,n6);
		print(7,n7);
		print(8,n8);
		print(9,n9);
		printf("\n");
	}
}