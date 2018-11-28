#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ofstream fout;
	fout.open("d:\\ans.txt");
	cout.rdbuf(fout.rdbuf());

	ifstream fin;
	fin.open("d:\\1.in");
	cin.rdbuf(fin.rdbuf());
	int n,x,s[10000];
	int t,te;
	int i,j,k;
	cin>>t;
	for(te=1;te<=t;te++){

		cin>>n>>x;
		for(i=0;i<n;i++)
			cin>>s[i];
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if(s[i]>s[j])
					swap(s[i],s[j]);
		i=0;
		j=n-1;
		int c=0;
		while(i<=j){
			if(i==j){
				c++;
				i++;
			}
			else{
				if(s[i]+s[j]<=x){
					c++;
					i++;
					j--;
				}
				else
				{
					c++;
					j--;
				}
			}
		}
		cout<<"Case #"<<te<<": "<<c<<endl;


	}
	return 0;
}