#include <iostream>
#include <string>
using namespace std;
int main(){
	int input;
	string j;
	int counter=0;
	/*list<int>::iterator it;
	for(it=mylist.begin();it!=mylist.end();++it){
		cout<<*it<<" \n";
	}*/
	cin>>input;
for (int i = 1; i <= input; ++i)
{
	
	counter=0;
	cin>>j;

if(j.size()>1){
			for(int l=0;l<j.size()-1;++l){
					if(j[l]!=j[l+1])
						counter++;
	
	}
}
				if(j[j.size()-1]=='-'){
					counter++;
				}
				cout<<"Case #"<<i<<": "<<counter<<endl;
	}
return 0;
}