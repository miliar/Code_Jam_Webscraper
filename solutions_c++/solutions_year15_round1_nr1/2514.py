#include<iostream>
#include<fstream>
#include<climits>
using namespace std;
int main(){
	int n,tmp,dip,cas,t,a1,a2,tots;
	ifstream fin("a1.in");
	ofstream fout("res.out");
	ofstream rout("tmp.in");
	//cin>>t;
	fin>>t;
	cas=0;
	while(t--){
		cas++;
		//cin>>n;
		fin>>n;
		rout<<"case #"<<cas<<": "<<n<<"\n";
		int arr[1003];
		dip=0;
		for(int i=0;i<n;i++){
		//	cin>>arr[i];
			fin>>arr[i];
			if(i>0){
				if(arr[i]<arr[i-1]){
					dip=max(dip,arr[i-1]-arr[i]);
				}
			}
			rout<<arr[i]<<" ";
		}
		rout<<"\n";
		rout<<"dif: "<<dip<<"\n";
		//cal a1
		a1=0;
		for(int i=1;i<n;i++){
			if(arr[i]<arr[i-1])
				a1+=arr[i-1]-arr[i];
		}
		//cal a2
		tots=0;
		a2=0;
		if(dip==0)
			a2=0;
		else{
			tots=arr[0];
			for(int i=1;i<n;i++){
				if(tots<dip){
					a2+=tots;
					tots=arr[i];
				}
				else {
					a2+=dip;
					//tots-=dip;
					tots=arr[i];
				}
			}
		}
		//cout<<"Case #"<<cas<<": "<<a1<<" "<<a2<<"\n";
		fout<<"Case #"<<cas<<": "<<a1<<" "<<a2<<"\n";
	}
}
