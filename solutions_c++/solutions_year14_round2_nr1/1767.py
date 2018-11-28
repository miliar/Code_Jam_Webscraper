#include <iostream>
#include <vector>
#include <algorithm> 
#include <set>
#include <fstream>
#include <string>
#include <utility>

using namespace std;
typedef vector<string> VS;
typedef vector<int> VI;
typedef pair< string , VI> PSVI;
typedef vector <PSVI> VSPVI;

PSVI signature(string s)
{
	string result; result+= s[0];	
	VI occ;
	int count = 1;
	char tmp = s[0];
	if(s.size()==1) occ.push_back(count);
	for(int i =1; i<s.size(); i++)
	{ 
	
	if(s[i]!=tmp) 
		{
		occ.push_back(count); 
		result+=s[i]; 
		tmp=s[i]; count=1;
		} 
	  	else{count++;}
	 
	 if(i==s.size()-1) 
	 		occ.push_back(count);
	}
	return make_pair(result,occ);
}

ifstream in("A-large.in"); ofstream out("a.out");
int T, tmpi, l=1;


int main()
{
	in>>T;
	while(T--)
	{
		int N, result = 0; in>>N;
		bool flag=true;
		string tmp,ref;
		VS st;
		VSPVI info;
		
		//preprocessing
		for(int i=0;i<N;i++)
		{
		  	in>>tmp;
			st.push_back(tmp);
			info.push_back(signature(tmp));
		}
		
		//check signatures are all the same
		ref = info[0].first;
		for(int i =1;i<N; i++) {if (info[i].first!=ref) {flag = false; break;}}
		if(flag)
		{
			VI values; int median;

			for(int j = 0;j < ref.size() ; j++)
			{
				for(int k = 0 ; k < N ; k++)
				{
					values.push_back(info[k].second[j]);
				}
				
				sort(values.begin(),values.end());
				if (N%2==0) {
				median = (values[N/2-1]+values[N/2])/2;} else median =values[(N-1)/2];
				
					for(int k = 0 ; k < N ; k++)
				{
					result+=abs(median-values[k]);
				}
				values.clear();
				
			}
			
		}
		out<<"Case #"<<l<<": ";
		if(flag) out<<result<<endl; else out<<"Fegla Won"<<endl;
		l++;	
		
	}
}
