#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#include<iomanip>
#define ll long long int
#define eps 1e-9

using namespace std;

int main(){
	int t,cases = 1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cases++<<": ";
		int ret = 0;
		string arr;
		cin>>arr;
		int n = arr.size();
		for(int i = n-1; i >= 0; i--){
			if(arr[i]=='-'){
				arr[i]='+';
				ret++;
				int j;
				for( j = i-1; j >= 1; j--){
					if(arr[j]=='-'){
						arr[j]='+';
					}
					else
					break;
			    }
				i = j;
				for(int k = i; k >= 0; k--)
					arr[k] == '+' ? arr[k] = '-' : arr[k] = '+';
				i++;
			}
		}
		cout<<ret<<endl;
	}
	return 0;
}
