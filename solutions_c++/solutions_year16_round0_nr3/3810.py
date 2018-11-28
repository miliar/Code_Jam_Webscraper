#include <iostream>
#include <string>
#include <math.h>
#include <bitset>


using namespace std;
string convertToBase(int base,string mystr);
string checkForPrime(long sum);
int main(){
	int input;
	int j,k;
	int counter=0;
	string strArr[9];
	/*list<int>::iterator it;
	for(it=mylist.begin();it!=mylist.end();++it){
		cout<<*it<<" \n";
	}*/
	cin>>input;
for (int i = 1; i <= input; ++i)
{	cout<<"Case #"<<i<<":"<<endl;
	cin>>j;
	cin>>k;
	int m=0;
	int fal=0;
	string finalString="";
	long lowValue=pow(2,j-1)+1;
	long highValue=pow(2,j)-1;
	for(m=lowValue;m<=highValue;m+=2){
			if(k>0){

		bitset<32> x(m);
		//cout<<x<<endl;
		string mystr = x.to_string();
		mystr=mystr.substr (mystr.size()-j);
		finalString =mystr;
		//cout<<finalString<<endl;
		for(int base=2;base<=10;base++){
			string output=convertToBase(base,mystr);
			//cout<<output<<endl;
			if(output==""){
				//cout<<"here"<<endl;
				fal=1;
				break;
			}
			else 
				strArr[base-2]=output;
		}	
		if(fal==0){
			//cout<<"here"<<endl;
			for(int n=0;n<9;n++){
			//	cout<<finalString<<endl;
				finalString+=" "+strArr[n];
			}
						cout<<finalString<<endl;

			k--;
		}
	}
			//cout<<"hererere"<<endl;
			fal=0;
	//uint64_t y =(uint64_t)x;
	//	cout<<y<<endl;
}
}

return 0;
}
string convertToBase(int base,string mystr){
	int size = mystr.size();
	long sum=0;
	int counter=0;
	for(int i=size-1;i>=0;i--){
		sum+=(pow(base,counter)*((int) (mystr[i])-48));
		counter++;
	}
		//cout<<sum<<endl;
		return checkForPrime(sum);
}
string checkForPrime(long sum){
	for(int i=2;i<sqrt(sum);i++){
		if(sum%i==0){
			return to_string(i);
		}
	}
	return "";
}