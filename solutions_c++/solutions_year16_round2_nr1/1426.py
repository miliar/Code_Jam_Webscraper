#include<iostream>

#include<memory.h>

using namespace std;



int main(){
	
	int t;
	cin >> t;
	int a[26];
	
	for(int iter = 0; iter < t; iter++){
		string s;
		cin >> s;
		memset(a,0,sizeof(a));
		
		for(int j = 0; j < s.length(); j++){
			int t = s[j] - 'A';
			//cout<<t<<endl;
			a[t]++;
		}
		
		int i0,i1,i2,i3,i4,i5,i6,i7,i8,i9;
		
		i4=a['U'-'A'];
		
		i0=a['Z'-'A'];
		i8=a['G'-'A'];
		i2=a['W'-'A'];
		i6=a['X'-'A'];
		i3=a['R'-'A']-i4-i0;
		i5=a['F'-'A']-i4;
		i7=a['S'-'A']-i6;
		i9=a['I'-'A']-i5-i6-i8;
		i1=a['N'-'A']-i9*2-i7;
		
		//cout<<i4<<endl;
		cout << "Case #" << iter + 1 << ": ";
		for(int i = 0; i<i0;i++)cout<<0;
		for(int i = 0; i<i1;i++)cout<<1;
		for(int i = 0; i<i2;i++)cout<<2;
		for(int i = 0; i<i3;i++)cout<<3;
		for(int i = 0; i<i4;i++)cout<<4;
		for(int i = 0; i<i5;i++)cout<<5;
		for(int i = 0; i<i6;i++)cout<<6;
		for(int i = 0; i<i7;i++)cout<<7;
		for(int i = 0; i<i8;i++)cout<<8;
		for(int i = 0; i<i9;i++)cout<<9;
		cout<<endl;
		
		
	}

	
	return 0;
}
