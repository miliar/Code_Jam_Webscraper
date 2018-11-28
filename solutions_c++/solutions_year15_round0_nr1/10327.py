#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream inp("A-small-attempt0.in");
	int t;	//number of cases
	
	inp>>t;
	
	int aud;	//audience
	
	ofstream out("out.txt");
	for(int k=0;k<t;++k){
			inp>>aud;
			int people[aud];
			char temp;
			for(int j=0;j<aud+1;++j){
				
				inp.get(temp);
				
				if(temp!=' '){
					cout<<temp<<"=";
					people[j]=temp - '0';
					cout<<people[j]<<endl;
				}
				else
					--j;
			}
	int need=0;
	
	int tot=0;
	int shy=0;
	for(int i=0; i<aud+1; ++i){
		
			tot=tot+people[i];
			cout<<"tot: "<<tot<<"<";
			shy=(i+1);
			cout<<shy<<" :shy"<<endl;
			if(people[shy]!=0 && shy>tot){
				need=need+shy-tot;
				tot+=shy;
				cout<<"need "<<need<<endl;
		}
		
		
		
		
	}
	cout<<endl;
	
	out<<"Case #"<<k+1<<": "<<need<<endl;
	
	}
	
	

	return 0;
}