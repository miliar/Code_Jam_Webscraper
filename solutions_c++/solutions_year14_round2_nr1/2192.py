#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void one_case(int no,ofstream& fout){
	int ans=0;
	int num;
	string a,b;
	cin>>num;
	cin>>a>>b;
	
	bool af=false,bf=false;
	string ac,bc;
	vector<int> av,bv;
	int an=-1,bn=-1;
	
	//get original of string a
	for(int i=0;i<a.size();i++){
		if(a[i]==a[i+1]){
			if(!af){
				ac+=a[i];
				af=true;
				an++;
				av.push_back(1);
			}
			else{
				av[an]++;
			}
		}
		else{
			if(!af){
				ac+=a[i];
				an++;
				av.push_back(1);
			}
			else{
				af=false;
				av[an]++;
			}
		}
	}
	
	//get original of string b
	for(int i=0;i<b.size();i++){
		if(b[i]==b[i+1]){
			if(!bf){
				bc+=b[i];
				bf=true;
				bn++;
				bv.push_back(1);
			}
			else bv[bn]++;
		}
		else{
			if(!bf){
				bc+=b[i];
				bn++;
				bv.push_back(1);
			}
			else{
				bf=false;
				bv[bn]++;
			}
		}
	}
	
	//cout<<a<<" "<<ac<<endl;
	//cout<<b<<" "<<bc<<endl;
	


	fout<<"Case #"<<no<<": ";
	if(ac==bc){
		//for(int i=0;i<av.size();i++){cout<<av[i];}cout<<endl;
		//for(int i=0;i<bv.size();i++){cout<<bv[i];}cout<<endl;
		for(int i=0;i<av.size();i++){
			if(av[i]>=bv[i])ans+=av[i]-bv[i];
			else ans+=bv[i]-av[i];
		}
		fout<<ans<<endl;
	}
	else
	fout<<"Fegla Won"<<endl;
}

int main(){
	ofstream fout;
	fout.open("1.out");
	int t=0;
	cin>>t;
	for(int i=0;i<t;i++){
		one_case(i+1,fout);
	}
}