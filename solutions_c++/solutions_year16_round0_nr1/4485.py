#include <iostream>
#include <list>
#include <string>
using namespace std;
int main(){
	int input;
	string j;
	list<int> mylist;
	int found=0;
	/*list<int>::iterator it;
	for(it=mylist.begin();it!=mylist.end();++it){
		cout<<*it<<" \n";
	}*/
	cin>>input;
for (int i = 1; i <= input; ++i)
{
	mylist.push_front(0);
	mylist.push_back(1);
	for(int k=2;k<10;k++){
		mylist.push_back(k);
	}
	found=0;
	cin>>j;
	long long jI=stoll(j);
	if(j.size()==1){
		if(j=="0"){
			found=1;
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else if(found==0){
			for(int m=1;m<100;m++){
				j=to_string(jI*m);
				for(int l=0;l<j.size();++l){
			list<int>::iterator it;
	for(it=mylist.begin();it!=mylist.end();++it){
//		cout<<*it<<"::"<<(int) j[l] - 48 <<endl;
		if(*it==(int) j[l] - 48){
			mylist.remove((int)j[l] - 48);
			if(mylist.empty()){
				found=1;
				cout<<"Case #"<<i<<": "<<j<<endl;
			}
			break;
		}
	}
	if(found==1)
	break;
	}
		}
		}
	}else{
			for(int m=1;m<100;m++){
				j=to_string(jI*m) ;
	for(int l=0;l<j.size();++l){
		list<int>::iterator it;
	for(it=mylist.begin();it!=mylist.end();++it){
		if(*it==(int) j[l]-48){
			mylist.remove((int)j[l]-48);
			if(mylist.empty()){
				found=1;
				cout<<"Case #"<<i<<": "<<j<<endl;
			}
			break;
		}
	}
	if(found==1)
	break;
		}
	}
	}
}
return 0;
}