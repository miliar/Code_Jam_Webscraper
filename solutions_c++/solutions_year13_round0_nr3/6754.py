#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>
#include<map>
using namespace std;
int arr[10000002] = {0};
int main()
{
	int t;
	scanf("%d",&t);
	arr[1] = 1;
	arr[2] = arr[4] = 1;
	arr[3] = arr[9] = 1;
	arr[11] = arr[22] = arr[33] = arr[44] = arr[55] = arr[66] = arr[77] = arr[88] = arr[99] = arr[101] =1;
	string s = "";
	int i,k;
	k = 11;
	string sk;
	for(i =  110;i < 10000002;i++){
		s += i;
		sk = string(s.rbegin(),s.rend());
		if(s == sk){
			arr[i] = 1;
		}
		s ="";
	}
	//map<long long int,long long int>m;
	map<double,double>m;
	//map<double, double>::reverse_iterator it;
	map<double, double>::iterator it;
	for(int i = 0;i < 10000002;i++){
		if(arr[i] == 1){
			int j = sqrt(i);
			if(arr[j] == 1 && j*j == i){
				m.insert(pair<double,double>(i,j));
				//m.insert(pair<int,int>(i,j));
			}
		}
	}
	int g = 1;
	while(t--){
		int n,mm;
		int count = 0;
		scanf("%d%d",&n,&mm);
		it = m.begin();
		while( it != m.end()){
			if(it->first <= mm && it->first >= n){
				count++;
			}
			it++;
		}
		cout<<"Case #"<<g++<<": "<<count<<endl;
	}
}

