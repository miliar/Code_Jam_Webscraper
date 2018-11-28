#include <bits/stdc++.h>
using namespace std;
ifstream fin("testin.txt");
ofstream fout("testout.txt");
int main(){
	int t,remainder,k=1;
	long long n;
	fin>>t;
	while(t--){
		int i=1,temp2;
		fin>>n;
		int a[10]={0};
		if(n==0){
			fout<<"case #"<<k<<": "<<"INSOMNIA"<<endl;
			k++;
			continue;

		}
		temp2=n;
		//cout<<"rohit"<<endl;
		while(1){
			int temp=temp2,j=0,count=0;
			while(temp>0){
                remainder=temp%10;
                a[remainder]=1;
                temp=temp/10;
			}
			//cout<<"hi"<<endl;
			while(a[j]!=0 and j<10){
				count++;
				j++;
			}
			//cout<<"hello"<<endl;
           if(count==10){
           	fout<<"case #"<<k<<": "<<temp2<<endl;
           	break;
           }else{
           	i++;
           	temp2=i*n;
           //	cout<<temp2<<endl;
           }
          
		}
		k++;
	}
}
