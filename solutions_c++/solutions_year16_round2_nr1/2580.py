#include<bits/stdc++.h>
using namespace std;
#define Int long long
#define p 1000000007
int main(){
	char S[2005];Int i,j,t,T,arr[2005],hash[500],Min;
	cin>>T;
	for(t=1;t<=T;t++){
		cin>>S;
		memset(hash,0,sizeof(hash));
		for(i=0;S[i]!='\0';i++){
			hash[S[i]]++;
		}
		for(i=0,j=0;i<hash['Z'];i++)arr[j++] = 0;
		hash['E'] -= hash['Z'];hash['R'] -= hash['Z'];hash['O'] -= hash['Z'];
		for(i=0;i<hash['X'];i++)arr[j++] = 6;
		hash['S']-=hash['X'];hash['I']-=hash['X'];
		for(i=0;i<hash['U'];i++)arr[j++] = 4;
		hash['F'] -= hash['U'];hash['O'] -= hash['U'];hash['R'] -= hash['U'];
		for(i=0;i<hash['W'];i++)arr[j++] = 2;
		hash['T'] -= hash['W'];hash['O'] -= hash['W'];
		for(i=0;i<hash['G'];i++)arr[j++] = 8;
		hash['E'] -= hash['G'];hash['I'] -= hash['G'];hash['H'] -= hash['G'];hash['T'] -= hash['G'];
		for(i=0;i<hash['O'];i++)arr[j++] = 1;
		hash['N'] -= hash['O'];hash['E'] -= hash['O'];
		for(i=0;i<hash['S'];i++)arr[j++] = 7;
		hash['E'] -= hash['S'];hash['E'] -= hash['S'];hash['V'] -= hash['S'];hash['N'] -= hash['S'];
		for(i=0;i<hash['V'];i++)arr[j++] = 5;
		hash['F'] -= hash['V'];hash['I'] -= hash['V'];hash['E'] -= hash['V'];
		for(i=0;i<hash['I'];i++)arr[j++] = 9;
		hash['N'] -= hash['I'];hash['N'] -= hash['I'];hash['E'] -= hash['I'];
		for(i=0;i<hash['T'];i++)arr[j++] = 3;
		sort(arr,arr+j);
		printf("Case #%lld: ",t);
		for(i=0;i<j;i++)cout<<arr[i];
		cout<<endl;
	}
	return 0;
}