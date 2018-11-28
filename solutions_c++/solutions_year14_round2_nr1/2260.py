#include<iostream>
#include<string>
#include<fstream>
#include<cmath>

using namespace std;

string reduce(string a){
	for (int i=0; i<a.length()-1; i++) {
		while (a[i]==a[i+1]) {
			a=a.substr(0,i+1)+a.substr(i+2,a.length()-i-2);
		}
	}
	return a;
}
int sign(string str, int arr[]){
	int res=0, count=1, letter=0;
	for (int i=0; i<str.length()-1; i++) {
		if (str[i]!=str[i+1]) {
			arr[letter]=count;
			count=1;
			letter++;
			continue;
		}
		else count++;
	}
	arr[letter]=count;
	letter++;
	
	return letter;
}

int main(int argc, char* argv[ ]) {
	/*string s;
	cin>>s;
	int a[100];
	for (int i=0; i<100; i++) {
		a[i]=0;
	}
	cout<<reduce(s)<<sign(s,a)<<endl;
	for (int i=0; i<sign(s,a); i++) {
		cout<<a[i]<<" ";
	}
	cout<<endl;*/
	int T, N, a1[100], a2[100], L, ans;
	string str1, str2;
	cin>>T;
	for (int t=1; t<=T; t++) {
		//bool FEGLA=0;
		ans=0;
		cin>>N;
		cin>>str1>>str2;
		if (reduce(str1)!=reduce(str2)) {
			cout<<"Case #"<<t<<": Fegla Won"<<endl;
			continue;
		}
		L=sign(str1, a1);
		L=sign(str2, a2);
		for (int i=0; i<L; i++) {
			ans+=abs(a1[i]-a2[i]);
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
		/*for (int i=0; i<L; i++) {
			cout<<a1[i]<<" ";
		}
		cout<<endl;
		for (int i=0; i<L; i++) {
			cout<<a2[i]<<" ";
		}
		cout<<endl;*/
	}
}

//cout<<"Case #"<<t<<": "<<score1<<" "<<N-score2<<endl;