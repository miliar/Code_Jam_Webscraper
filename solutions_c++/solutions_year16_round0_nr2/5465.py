#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

bool bin[101];
bool a[101];

bool verify(int s){
	for(int i=0; i<s; i++)
		if(!bin[i])
			return 0;
	return 1;
}

ll operations(int s){
	int temp,count = 0;
	while(!verify(s)){
		for(int i=s-1; i>=0; i--){
			if(!bin[i]){
				temp = i;
				break;
			}
		}
		//cout << temp << endl;
		if(bin[0]){
			for(int i=0; i<temp; i++)
				if(bin[i])
					bin[i] = !bin[i];
				else
					break;
		}
		else{
			for(int i=0; i<=temp; i++)
				a[temp-i] = !bin[i];
			for(int i=0; i<=temp; i++)
				bin[i] = a[i];
		}
		// for(int j=0; j<s; j++)
		// 	cout << bin[j] << " ";
		// cout << endl;
		count++;
	}
	return count;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out1.io","w",stdout);

	int test,len,i=1;
	string str;
	cin >> test;
	while(i<=test){
		cin >> str;
		len = str.size();
		for(int j=0; j<len; j++){
			if(str[j]=='-')
				bin[j]=0;
			else
				bin[j]=1;
		}
		if(verify(len))
			cout << "Case #" << i << ": 0" << endl;
		else
			cout << "Case #" << i << ": " << operations(len) << endl;
		i++;
	}
	return 0;
}