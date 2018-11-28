#include <iostream>
#include <string>
using namespace std;
string multpos(string c1, string c2){
	if (c1 == "1")
		return c2;
	if (c2 == "1")
		return c1;
	if (c1 ==  c2)
		return "-1";
	if (c1 == "i" && c2== "j")
		return "k";
	if (c1 == "j" && c2== "k")
		return "i";
	if (c1 == "k" && c2== "i")
		return "j";
			
	if (c1 == "j" && c2== "i")
		return "-k";
	if (c1 == "k" && c2== "j")
		return "-i";
	if (c1 == "i" && c2== "k")
		return "-j";
}
string mult(string c1, string c2){
	if (c1[0]=='-' && c2[0] == '-'){
		return multpos(c1, c2);
	}
	else if (c1[0]=='-' || c2[0] == '-'){
		string temp;
		if(c1[0] == '-')
			temp = multpos(c1.substr(1,1), c2);
		else
			temp = multpos(c1, c2.substr(1,1));
		if(temp[0] == '-')
			temp = temp[1];
		else temp = "-" + temp;
		return temp;
	}
	else return multpos(c1, c2);
}
int main(){
	int ntest;
	cin>>ntest;
	for (int z = 1; z<=ntest; z++){
		//char arr[1000][1000];
		int l, x;
		cin>>l>>x;
		string rep;
		cin>>rep;
		
		string left = "1";
		bool done = false;
		
		string cum[l*x];
		cum[0] = rep[0];
		for (int  i = 1; i<l*x; i++){
			char cur = rep[i%l];
			string s(1, cur);
			cum[i] = mult(cum[i-1], s);
		}
		if (cum[l*x-1]!="-1"){
			cout<<"Case #"<<z<<": NO"<<endl;
			continue;
		}
		
		for(int i=0; i<l*x; i++){
			if(done)
				break;
			if(cum[i] == "k"){
				//cout<<i<<endl;
					bool same = true;
					for(int j = 0; j<min(i,l); j++){
						if(rep[j]!='k')
							same = false;
					}
					if (!same)
						done = true;
			}
		}
		cout<<"Case #"<<z<<": ";
		if(done)
			cout<<"YES"<<endl;
			else cout<<"NO"<<endl;		
	}
}
