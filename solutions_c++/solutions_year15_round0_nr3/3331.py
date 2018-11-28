#include<iostream>
#include<string>
using namespace std;

string mul(string a,string b)
{
	
	if(a=="") return(b);
	if(b=="") return(a);
	string sa="";
	string sb="";
	int m=a.length();
	int n=b.length();
	if(m==2){
		a=a[1];
		sa="-";
	}
	if(n==2){
		b=b[1];
		sb="-";
	}
	string sr="";
	if(sa!=sb) sr="-";
	if(a=="1" && b=="1"){
		if(sr=="") return("1");
		return("-1");
	}
	if(a=="1" && b=="i"){
		if(sr=="")return("i");
		return("-i");
	}
	if(a=="1" && b=="j"){
		if(sr=="")return("j");
		return("-j");
	}
	if(a=="1" && b=="k"){
		if(sr=="")return("k");
		return("-k");
	}
	if(a=="i" && b=="1"){
		if(sr=="") return("i");
		else return("-i");
	}
	if(a=="i" && b=="i"){
		if(sr=="") return("-1");
		else return("1");
	}
	if(a=="i" && b=="j"){
		if(sr=="") return("k");
		else return("-k");
	}
	if(a=="i" && b=="k"){
		if(sr=="") return("-j");
		else return("j");
	}
	if(a=="j" && b=="1"){
		if(sr=="") return("j");
		else return("-j");
	}
	if(a=="j" && b=="i"){
		if(sr=="") return("-k");
		else return("k");
	}
	if(a=="j" && b=="j"){
		if(sr=="") return("-1");
		else return("1");
	}
	if(a=="j" && b=="k"){
		if(sr=="") return("i");
		else return("-i");
	}
	if(a=="k" && b=="1"){
		if(sr=="") return("k");
		else return("-k");
	}
	if(a=="k" && b=="i"){
		if(sr=="") return("j");
		else return("-j");
	}
	if(a=="k" && b=="j"){
		if(sr=="") return("-i");
		else return("i");
	}
	if(a=="k" && b=="k"){
		if(sr=="") return("-1");
		else return("1");
	}
	
	
	
}

int main()
{
	
	int t=0;
	int T;
	cin>>T;
	while(T--){
		int L,X;
		cin>>L;
		cin>>X;
		string str;
		cin>>str;
		string in;
		for(int i=0;i<X;i++){
			in=in+str;
		}
		string curr="";
		string ab="";
		int l=in.length();
		int i=0;
		while(curr!="i" && i<l){
			ab=in[i];
			curr=mul(curr,ab);
			i++;
		}
		//cout<<curr<<endl;
		if(i>=l){
			cout<<"Case #"<<(++t)<<": NO"<<endl;
			continue;
		}
		int j=l-1;
		curr="";
		while(curr!="k" && j>=i){
			ab=in[j];
			curr=mul(ab,curr);
			j--;
		}
		//cout<<curr<<endl;
		//cout<<i<<" "<<j<<endl;
		if(j<i){
			cout<<"Case #"<<(++t)<<": NO"<<endl;
			continue;
		}
		if(i==j){
			if(in[i]=='j') {
				cout<<"Case #"<<(++t)<<": YES"<<endl;
				continue;
			}
			else{
				cout<<"Case #"<<(++t)<<": NO"<<endl;
				continue;
			}
		}
		curr="";
		for(int x=i;x<=j;x++){
			ab=in[x];
			//cout<<curr<<" ";
			curr=mul(curr,ab);
			//cout<<ab<<" "<<curr<<endl;
			
		}
		if(curr=="j"){
			cout<<"Case #"<<(++t)<<": YES"<<endl;
			continue;
		}
		else{
			cout<<"Case #"<<(++t)<<": NO"<<endl;
			//cout<<curr<<endl;
			//cout<<"vb"<<endl;
			continue;
		}
		
		
	}
	
}
