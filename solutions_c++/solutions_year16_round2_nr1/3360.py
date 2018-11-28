#include<iostream>
#include<string.h>
#include <algorithm>

using namespace std;
string check0(string s){
	int e;
 	if(s.find("Z") != -1)
	{
 			e = s.find("Z");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("R");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("O");
			s = s.substr(0,e) + s.substr(e+1);
	}
	return s;	
}

string check1(string s){
	int e;
 	if(s.find("O") != -1 && s.find("N") != -1 && s.find("E") != -1 )
	{
		    e = s.find("O");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("N");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);

	}
	return s;	
}

string check2(string s){
	int e;
 	if(s.find("T") != -1 && s.find("W") != -1 && s.find("O") != -1 )
	{
		    e = s.find("T");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("W");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("O");
			s = s.substr(0,e) + s.substr(e+1);

	}
	return s;	
}

string check3(string s){
	int e;
	int p = s.find("E");
 	if(s.find("T") != -1 && s.find("H") != -1 && s.find("R") != -1 &&  p!= -1 && s.find("E",p+1) != -1 )
	{
		    e = s.find("T");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("H");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("R");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
	}
	return s;	
}


string check4(string s){
	int e;
 	if(s.find("F") != -1 && s.find("O") != -1 && s.find("U") != -1 && s.find("R") != -1 )
	{
		    e = s.find("F");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("O");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("U");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("R");
			s = s.substr(0,e) + s.substr(e+1);
	   	}
	return s;	
}

string check5(string s){
	int e;
 	if(s.find("F") != -1 && s.find("I") != -1 && s.find("V") != -1 && s.find("E") != -1 )
	{
		    e = s.find("F");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("I");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("V");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
	   	}
	return s;	
}

string check6(string s){
	int e;
 	if(s.find("S") != -1 && s.find("I") != -1 && s.find("X") != -1   )
	{
		    e = s.find("S");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("I");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("X");
			s = s.substr(0,e) + s.substr(e+1);
	   	}
	return s;	
}

string check7(string s){
	int e;
	int p = s.find("E");
 	if(s.find("S") != -1 && s.find("V") != -1 && s.find("N") != -1 &&  p!= -1 && s.find("E",p+1) != -1 )
	{
		    e = s.find("S");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("V");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("N");
			s = s.substr(0,e) + s.substr(e+1);
	}
	return s;	
}

string check8(string s){
	int e;
 	if(s.find("E") != -1 && s.find("I") != -1 && s.find("G") != -1 && s.find("H") != -1 && s.find("T") != -1 )
	{
		    e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("I");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("G");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("H");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("T");
			s = s.substr(0,e) + s.substr(e+1);
			
	   	}
	return s;	
}

string check9(string s){
	int e;
	int p = s.find("N");
 	if(s.find("I") != -1 && s.find("E") != -1 &&  p!= -1 && s.find("N",p+1) != -1 )
	{
		    e = s.find("N");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("I");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("N");
			s = s.substr(0,e) + s.substr(e+1);
			e = s.find("E");
			s = s.substr(0,e) + s.substr(e+1);

	}
	return s;	
}
int main(int argc, char *argv[])
{
	int T;
	cin>>T;
	string s = "";
	string w = "";
	string ans = "";
	string open = "";
	int i,j = 0;
  	for (i = 1; i <= T; i++) {
		s = "";
		w = "";
		ans = "";
		open = "";
		cin>>s;
		open = s;
 		//for 0
		for(j = 0;;j++) {
			w = check0(s);
			if(w == s)
				break;
			else{
					ans = ans + "0";
					s = w;
			}
		}

		//for 2
		for(j = 0;;j++) {
			w = check2(s);
			if(w == s)
				break;
			else{
					ans = ans + "2";
					s = w;
			}
		}

		//for 6
		for(j = 0;;j++) {
			w = check6(s);
			if(w == s)
				break;
			else{
					ans = ans + "6";
					s = w;
			}
		}
		//for 8
		for(j = 0;;j++) {
			w = check8(s);
			if(w == s)
				break;
			else{
					ans = ans + "8";
					s = w;
			}
		}

		//for 3
		for(j = 0;;j++) {
			w = check3(s);
			if(w == s)
				break;
			else{
					ans = ans + "3";
					s = w;
			}
		}

		//for 7
		for(j = 0;;j++) {
			w = check7(s);
			if(w == s)
				break;
			else{
					ans = ans + "7";
					s = w;
			}
		}

		//for 4
		for(j = 0;;j++) {
			w = check4(s);
			if(w == s)
				break;
			else{
					ans = ans + "4";
					s = w;
			}
		}

		//for 5
		for(j = 0;;j++) {
			w = check5(s);
			if(w == s)
				break;
			else{
					ans = ans + "5";
					s = w;
			}
		}
		
		//for 1
		for(j = 0;;j++) {
			w = check1(s);
			if(w == s)
				break;
			else{
					ans = ans + "1";
					s = w;
			}
		}
		
		
		//for 9
		for(j = 0;;j++) {
			w = check9(s);
			if(w == s)
				break;
			else{
					ans = "9" + ans ;
					s = w;
			}
		}
		

			if(s != ""){
			cout<<"+++++++++++"<<s<<"************ "<<open<<" : "<<i<<endl;}
		
			
			if(s==""){
				sort(ans.begin(), ans.end());
				cout<<"Case #"<<i<<": "<<ans<<endl;
			}
		/*	
		else{
			ans = "";
			s = open;

			//for 0
		for(j = 0;;j++) {
			w = check0(s);
			if(w == s)
				break;
			else{
					ans = "0" + ans ;
					s = w;
			}
		}
			//for 6
		for(j = 0;;j++) {
			w = check6(s);
			if(w == s)
				break;
			else{
					ans = "6" + ans ;
					s = w;
			}
		}

		//for 2
		for(j = 0;;j++) {
			w = check2(s);
			if(w == s)
				break;
			else{
					ans = "2" + ans ;
					s = w;
			}
		}
			//for 8
		for(j = 0;;j++) {
			w = check8(s);
			if(w == s)
				break;
			else{
					ans = "8" + ans ;
					s = w;
			}
		}
		//for 5
		for(j = 0;;j++) {
			w = check5(s);
			if(w == s)
				break;
			else{
					ans = "5" + ans ;
					s = w;
			}
		}
		//for 4
		for(j = 0;;j++) {
			w = check4(s);
			if(w == s)
				break;
			else{
					ans = "4" + ans ;
					s = w;
			}
		}
		
		//for 1
		for(j = 0;;j++) {
			w = check1(s);
			if(w == s)
				break;
			else{
					ans = "1" + ans ;
					s = w;
			}
		}

		//for 9
		for(j = 0;;j++) {
			w = check9(s);
			if(w == s)
				break;
			else{
					ans = "9" + ans ;
					s = w;
			}
		}
		//for 7
		for(j = 0;;j++) {
			w = check7(s);
			if(w == s)
				break;
			else{
					ans = "7" + ans ;
					s = w;
			}
		}

		

		//for 3
		for(j = 0;;j++) {
			w = check3(s);
			if(w == s)
				break;
			else{
					ans = "3" + ans ;
					s = w;
			}
		}

		
		if(s != "")
			cout<<"+++++++++++"<<s<<"************ "<<open<<" : "<<i;
			cout<<"Case #"<<i<<": "<<ans<<endl;
			}*/
	}
}
