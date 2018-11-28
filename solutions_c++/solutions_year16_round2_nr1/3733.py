#include<iostream>
#include<stdafx.h>
#include <iostream>
#include <fstream>
#include<string>
#include <vector>
#include<algorithm>
#include <stdio.h>
#include<list>
#include<set>
#include <math.h> 
#include<map>
#define  LL long long
using namespace std;



//string num;
//LL finalcnt =0;
//vector<string>V;
//
//vector<LL>VLL;
//vector<string>total;
//int divisor[10] ={0};
//vector<vector<LL>>VVI;
//bool done = false;
//LL s =0;


//LL power(LL a, LL b) {
//	if(b == 0) return 1;
//	LL x = power(a,b/2);
//	x *= x;
//	if(b&1) x *= a;
//	return x;
//}
//
//bool checkPrime(LL num)
//{
//	bool flag = false;
//	for(LL i=2;i<=sqrt((long double)num);++i)
//  {
//      if(num%i==0)
//      {
//          flag=1;
//          break;
//      }
//  }
//  if (flag==0)
//  {
//      //cout << "This is a prime number";
//	  return true;
//  }
//  else
//     // cout << "This is not a prime number";
//	 return false;
//}
//
//set<string>Geneartenumber(LL n, LL k)
// {
//	 set<string>s;
//	 
//	 if(n ==1)
//	 {
//		for(LL i =0; i<k ; i++)
//		{
//			string temp ="";
//			temp+= i+'0';
//			s.insert(temp);
//			
//		}
//		return s;	
//
//	 }
//	 set<string>list1 = Geneartenumber(n-1,k);
//	 set<string>::iterator it = list1.begin();
//	 for(;it != list1.end();++it )
//	 {
//		 LL size =k;
//		 for(LL k =0; k<size;k++)
//		 {
//			 string temp =*it;
//			 temp+= k+'0';
//			 s.insert(temp);
//		 }
//	 }
//	
//	 /*for(int j =0; j<list1.size(); j++)
//	 {
//		 int size =k;
//		 for(int k =0; k<size;k++)
//		 {
//			 string temp =list1[j];
//			 temp+= k+'0';
//			 s.push_back(temp);
//		 }
//	 }*/
//	 return s;
//
//
// }
// 
//
//int main(){
//	
//	ifstream fin("input.in");
//    ofstream fout("output.out");
//
//	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
//    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
//
//	LL t;
//	fin >> t;
//	LL N;
//	fin >> N;
//	LL J ;
//	fin >> J;
//
//	for(LL i =0; i<J; i++)
//	{
//		vector<LL>temp;
//		VVI.push_back(temp);
//	}
//
//	for (LL f =0; f<t; f++){
//	set<string> temp = Geneartenumber(N,2);
//	set<string>::iterator it;
//	for (it = temp.begin(); it != temp.end();it++ ) {
//		string str = *it;
//		if(str[N-1]-'0'==1 && str[0]-'0'==1)
//		{
//			V.push_back(str);
//		}
//		
//    }
//	LL sum =0;
//	for(LL l = 0; l<J; l++ ){
//	for(LL i =0; i<V.size(); i++)
//	{
//		
//		string str = V[i];
//		for(LL j =2; j<=10; j++)
//		{
//			
//			LL k =0;
//			LL po = N-1;
//			while(k<=str.length()-1)
//			{
//				//sum += (str[k]-'0')*pow(j,po);
//				sum += (str[k]-'0')*power(j,po);
//				po--;
//				k++;
//			}
//			//check for not prime
//			/*if(sum == 470184985873)
//			{
//				VLL.push_back(sum);
//				sum =0;
//			}*/
//			 if(checkPrime(sum)== true)
//			{
//				VLL.clear();
//				sum =0;
//				break;
//			}
//			else{
//				VLL.push_back(sum);
//				sum =0;
//			}
//
//		 }
//		if(VLL.size()==9)
//		{
//			total.push_back(str);
//			/*cout<< str << endl;
//			for(int i =0 ; i<VLL.size()-1; i++)
//				cout<<VLL[i]<<endl;*/
//
//			LL divisor_cnt =0;
//			for(LL m =2; m<999999; m++)
//			{
//				for(LL i =0 ; i<VLL.size(); i++)
//				{
//					if(VLL[i]%m ==0 && divisor[i]==0)
//					{
//						divisor[i]= m;
//						divisor_cnt++;
//					}
//
//				}
//				if(divisor_cnt ==9)
//				{
//					for(LL p =0; p<9; p++){
//						LL a = divisor[p];
//					VVI[s].push_back(a);
//					}
//					s++;
//					VLL.clear();
//					for(LL b = 0; b<9; b++)
//						divisor[b]=0;
//					break;
//				}
//			}
//
//
//		}
//		if(total.size()==J){
//			done = true;
//			break;
//		}
//		
//		}
//		if(done ==true)
//			break;
//
//
//	}
//	s=0;
//	fout << "Case #" << (f+1) << ":"<<endl;
//	for(LL i =0; i<J ; i++){
//		fout<<total[i]<<" ";
//		LL sz = VVI[i].size();
//		for (LL k = 0; k<sz; k++)
//		{
//			fout <<VVI[i][k] <<" ";
//		}
//		fout<<endl;
//	}
//
//	}
//    
//    
//		//fout << "Case #" << (i+1) << ": " << need << endl;		
//	//}
//	return 0;
//}

//int main(){
//
//	ifstream fin("input.in");
//    ofstream fout("output.out");
//
//	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
//    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
//	LL T;
//	fin>> T;
//	
//	for(int i =0; i< T; i++)
//	{
//		LL K;
//	fin>> K;
//	LL C;
//	fin>> C;
//	LL S;
//	fin>> S;
//		fout << "Case #" << (i+1) << ": ";
//		for(int j=1; j<=S; j++)
//		{
//			fout <<j <<" ";
//		}
//		fout<< endl;
//
//	}
//
//	return 0;
//}
//int main(){
//
//	ifstream fin("input.in");
//    ofstream fout("output.out");
//
//	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
//    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
//	LL T;
//	fin>> T;
//	for(LL i =0; i<T; i++){
//		string s;
//		
//		fin>>s;
//		string out =s;
//
//		
//		for(LL j =0; j<s.length()-1;j++)
//		{
//			if(s[0]-'0'>s[j+1]-'0')
//			{
//			}
//			else{
//				/*char temp;
//				temp =s[0];
//				s[0]= s[j+1];
//				s[1] = temp;
//				for(LL k =2; k<=j+1;k++){
//					s[k] = s[k-1];
//					
//				}*/
//
//				out[0]= s[j+1];
//				for(LL k =1 ; k<=j+1; k++)
//				{
//					out[k] = s[k-1];
//				}
//				for(LL n =0; n<s.length(); n++)
//				{
//					s[n] = out[n];
//				}
//				//s[0] = out[0];
//				
//
//			}
//		}
//		fout << "Case #" << (i+1) << ": " << out << endl;
//	}
//	
//	
//	return 0;
//}

string arr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
//string greater1(string a, string b)
//{
//	return a>b;
//}
int main(){

	ifstream fin("input.in");
    ofstream fout("output.out");

	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	LL T;
	fin>> T;
	for(LL i =0; i<T ; i++)
	{
		string s;
		fin>>s;
		string temp = s;
		int k =0;
		//vector<int>V;
		string res;
		bool find = false;

		//for(int j =0; j<s.length(); j++)
		sort(temp.begin(), temp.end());
		string emr = temp;
		string temp1 = temp;
		int p =0;
		int q =0;
		while(temp.length()>0)
		{

			if(p == 9999)
			{
				temp = emr;
				p =0;
				if(q<10)
				{
					k=q++;
					res.erase();
				}
				else
				q=0;
			}
			string ph_str = arr[k];
			sort(ph_str.begin(), ph_str.end());
			int r =0;

			for (LL m = 0; m < temp.length();  m++)
			{
				if(temp[m]==ph_str[r])
				{
					temp.erase(temp.begin()+m);
					r++;
					m--;
				}
				if(r == ph_str.length())
				{
					res += k+'0';
					find = true;
					temp1 = temp;
					break;
				}

			}
			if(find == false)
			{
				temp = temp1;
			}
			find = false;
			k++;
			if(k==10)
				k=0;
			p++;
			

			
		}
		sort(res.begin(),res.end());
		fout << "Case #" << (i+1) << ": " << res << endl;

	}
	
	
	
	
	
	return 0;
}