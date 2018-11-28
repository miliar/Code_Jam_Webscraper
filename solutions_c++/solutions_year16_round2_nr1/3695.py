#include <bits/stdc++.h>
typedef long long int ll;
#define fio ios_base::sync_with_stdio(false)
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int z=1; z<=t; z++)
	{
		vector<int> v;
		map<char,int> m;
		string s;
		cin>>s;
		for(int i=0; i<s.size(); i++) m[s[i]]++;
		if(m['Z']!=0)
		{
			int k=m['Z'];
			for(int i=0; i<k; i++)	
				{v.push_back(0); m['Z']--,m['E']--,m['R']--,m['O']--;}
		}
		if(m['W']!=0) 
		{
			int k=m['W'];
			for(int i=0; i<k; i++)	
			{v.push_back(2); m['T']--;m['W']--;m['O']--;}
		}
		if(m['X']!=0) 
		{
			int k=m['X'];
			for(int i=0; i<k; i++)	
			{v.push_back(6); m['S']--;m['I']--;m['X']--;}
		}
		if(m['G']!=0) 
		{
			int k=m['G'];
			for(int i=0; i<k; i++)	
			{v.push_back(8); m['E']--;m['I']--;m['G']--;m['H']--;m['T']--;}
		}
		if(m['S']!=0) 
		{
			int k=m['S'];
			for(int i=0; i<k; i++)	
			{v.push_back(7); m['S']--;m['E']--;m['V']--;m['E']--;m['N']--;}
		}
		if(m['V']!=0) 
		{
			int k=m['V'];
			for(int i=0; i<k; i++)	
			{v.push_back(5); m['F']--;m['I']--;m['V']--;m['E']--;}
		}
		if(m['F']!=0) 
		{
			int k=m['F'];
			for(int i=0; i<k; i++)	
			{v.push_back(4); m['F']--;m['O']--;m['U']--;m['R']--;}
		}
		if(m['T']!=0) 
		{
			int k=m['T'];
			for(int i=0; i<k; i++)	
			{v.push_back(3); m['T']--;m['E']--;m['H']--;m['E']--;m['R']--;}
		}
		if(m['O']!=0) 
		{
			int k=m['O'];
			for(int i=0; i<k; i++)	
			{v.push_back(1); m['N']--;m['E']--;m['O']--;}
		}
		if(m['E']!=0) 
		{
			int k=m['E'];
			for(int i=0; i<k; i++)	
			{v.push_back(9); m['N']-=2;m['I']--;m['E']--;}
		}
		sort(v.begin(),v.end());
		cout<<"Case #"<<z<<": ";
		for(vector<int>::iterator it=v.begin(); it!=v.end(); it++) cout<<*it;
		cout<<"\n";
	}
	return 0;
}