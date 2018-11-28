#include<vector>
#include<stack>
#include<set>
#include<queue>
#include<map>
#include<list>
#include<deque>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<bitset>
#include<complex>
#include<functional>
#include<limits>
#include<locale>
#include<numeric>
#include<string>
#include<utility>
#include<climits>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<ctime>
#include<unordered_set>
#include<unordered_map>

using namespace std;

string find_number(string s){
	string nums[]={"1.ZERO+", "O+NE", "2.TW+O", "T+HREE", "4.FOU+R", "5.F+IVE", "7.SIX+", "SEVEN", "8EIG+HT", "NINE"};
	unordered_map<char,int> dic;
	for(int i=0;i<s.size();++i)dic[s[i]]++;
	string res="";
	while(dic['Z']>0) {res+="0";--dic['E'];--dic['R'];--dic['O'];dic['Z']--;}
	while(dic['W']>0){res+="2";dic['T']--;dic['W']--;dic['O']--;}
	while(dic['F']>0&&dic['O']>0&&dic['U']>0&&dic['R']>0){res+="4";dic['F']--;dic['O']--;dic['U']--;dic['R']--;}
	while(dic['F']>0&&dic['I']>0&&dic['V']>0&&dic['E']>0){res+="5";dic['F']--;dic['I']--;dic['V']--;dic['E']--;}
	while(dic['S']>0&&dic['I']>0&&dic['X']>0){res+="6";dic['S']--;dic['I']--;dic['X']--;}
	while(dic['E']>0&&dic['I']>0&&dic['G']>0&&dic['H']>0&&dic['T']>0){res+="8";dic['E']--;dic['I']--;dic['G']--;dic['H']--;dic['T']--;}
	while(dic['O']>0&&dic['N']>0&&dic['E']>0){ res+="1"; dic['O']--;dic['N']--;dic['E']--;}
	while(dic['T']>0&&dic['H']>0&&dic['R']>0&&dic['E']>1){res+="3";dic['T']--;dic['H']--;dic['R']--;dic['E']-=2;}
	while(dic['S']>0&&dic['E']>1&&dic['V']>0&&dic['N']>0){res+="7";dic['S']--;dic['E']-=2;dic['V']--;dic['N']--;}
	while(dic['N']>1&&dic['I']>0&&dic['E']>0){res+="9";dic['N']-=2;dic['I']--;dic['E']--;}
	sort(res.begin(),res.end());
	return res;}

	
int main(){
    ifstream infile("A-large.txt");
    ofstream ofile("A-large-output.txt");
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
            
          string s;
          infile>>s;
          string res=find_number(s);
        
          ofile<<"Case #"<<curcase<<": "<<res<<endl;
          
          ++curcase;
                         }
          
		  
		  
		   }
       infile.close();
       ofile.close();
       return 0;}


