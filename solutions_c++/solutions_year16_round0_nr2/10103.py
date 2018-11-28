#include<iostream>
#include<vector>
using namespace std;
int main(){
	
	freopen("sub-4.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	long int n;
	
	cin>>n;
	
	long int ress=1;
	
	while(n--){
		
		long int count=0;
		vector<int> v;
		vector<int>::iterator it;
		vector<int>::iterator it2;
		
		string k;
		cin>>k;
		
		for(int i=0;i!=k.size();i++){
			if(k[i]=='+')
				v.push_back(1);
			else
				v.push_back(0);
		}
		
		it=v.begin();
		it2=v.begin();
		
		if(v.size()==1){
			
			if(*it==0)
			++count;
			
			cout<<"Case #"<<ress<<": "<<count<<endl;
			++ress;
			
			continue;
		
		}else if(v.size()==2){
			
			it=(v.begin()+1);
			if( *it==0 && *it2==1 ){
				count+=2;
				cout<<"Case #"<<ress<<": "<<count<<endl;
				++ress;
				continue;
			
			}else{
				++count;
				cout<<"Case #"<<ress<<": "<<count<<endl;
				++ress;
				continue;
			}
		}else{
			
			int len=v.size();
			it=v.end();
			
			len=(v.size());
			for(int i=1;i<len;i++)
				if(v[i-1]!=v[i])
				++count;
				
			if(v[len-1] == 0)
				++count;
		}
		cout<<"Case #"<<ress<<": "<<count<<endl;
		++ress;
	}
	return 0;
}
