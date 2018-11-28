#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <stdlib.h>
using namespace std;

map<string,string> m;



string & reduceStr(string & str){
	
	if(str[0] == '-' ){
		if(str.size() < 3){
			return str;
		}
		str = m[str.substr(0,3)] + str.substr(3);
	} else {
		if(str.size() < 2){
			return str;
		}
		str = m[str.substr(0,2)] + str.substr(2);
	}
	//cout << "str=" << str<<endl;
	return str;
}

int main()
{
  freopen("C-small-attempt3.in","r",stdin);
  freopen("C-small-attempt3.out","w",stdout);
  m["ii"] = "-";
m["ij"] = "k";
m["ik"] = "-j";
m["ji"] = "-k";
m["jj"] = "-";
m["jk"] = "i";
m["ki"] = "j";
m["kj"] = "-i";
m["kk"] = "-";
m["-ii"] = "";
m["-ij"] = "-k";
m["-ik"] = "j";
m["-ji"] = "k";
m["-jj"] = "";
m["-jk"] = "-i";
m["-ki"] = "-j";
m["-kj"] = "i";
m["-kk"] = "";
  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
  		bool b_i = false;
		bool b_j = false;
		bool b_k = false;
      int L,X;
      cin>>L >> X ;
      string str ;
      cin >> str ;
   
      string temp = "";
      for (int i = 0; i < X; ++i)
      {
      	temp = temp + str;
      }
      while(!b_i && temp.size()>1){
      	if(temp[0] == 'i' ){
      		b_i =true;
      		temp = temp.substr(1);
      		break;
      	} else if(temp[0]=='-' && temp[1]=='i'){
      		b_i =true;
      		temp = "-" + temp.substr(2);
      		break;
      	} 
      	if( (temp[0]=='-' && temp.size() < 3 ) || temp.size() < 2){
      		break;
      	} else {
      		temp = reduceStr(temp);
      	}
      	
      }

      while(!b_j && temp.size()>1){
      	if(temp[0] == 'j' ){
      		b_j =true;
      		temp = temp.substr(1);
      		break;
      	} else if(temp[0]=='-' && temp[1]=='j'){
      		b_j =true;
      		temp = "-" + temp.substr(2);
      		break;
      	}
      	if( (temp[0]=='-' && temp.size() < 3 ) || temp.size() < 2){
      		break;
      	} else {
      		temp = reduceStr(temp);
      	}
      }
      
      while( !((temp[0]=='-' && temp.size() < 3 ) || temp.size() < 2)){
      	
      	temp = reduceStr(temp);
      }
      //cout<<"Case #"<<"b_i"<<": "<< b_i<<endl; 
     //cout<<"Case #"<<"b_j"<<": "<< b_j<<endl; 
      //cout<<"Case #"<<"temp"<<": "<< temp<<endl; 
      if(b_i == true && b_j == true && temp == "k"){
		cout<<"Case #"<<t<<": "<< "YES"<<endl;
      } else {
      	cout<<"Case #"<<t<<": "<< "NO"<<endl;
      }
      
      
   }
}