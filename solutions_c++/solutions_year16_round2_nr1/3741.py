#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string input;
	scanf("%d",&t);
	map<char,int> mp;
	for( int test=1;test<=t;++test)
	{
		mp['Z']=mp['E']=mp['R']=mp['O']=mp['N']=mp['T']=mp['W']=mp['H']=mp['F']=mp['U']=mp['I']=mp['V']=mp['S']=mp['X']=mp['G']=0;
	
		vector<int> ans;
		cin>>input;
	
		for(unsigned int i=0;i<input.length();++i)
		{
			mp[input[i]]++;
		}
	
		while(mp['Z']||mp['E']||mp['R']||mp['O']||mp['N']||mp['T']||mp['W']||mp['H']||mp['F']||mp['U']||mp['I']||mp['V']||mp['S']||mp['X']||mp['G'])
		{
		if(mp['Z'])
		{
			while(mp['Z']!=0)
			{ans.push_back(0);
			mp['Z']--;
			mp['E']--;
			mp['R']--;
			mp['O']--;}
			
		}
		if(mp['W'])
		{
			while(mp['W']!=0)
			{
			ans.push_back(2);
			mp['T']--;
			mp['W']--;
			mp['O']--;}
		}
		if(mp['U'])
		{
			while(mp['U']!=0)
			{
			ans.push_back(4);
			mp['F']--;
			mp['O']--;
			mp['U']--;
			mp['R']--;}
		}
		
		if(mp['G'])
		{
			while(mp['G']!=0)
			{
			ans.push_back(8);
			mp['E']--;
			mp['I']--;
			mp['G']--;
			mp['H']--;
			mp['T']--;}
		}
		
		if(mp['X'])
		{
			while(mp['X']!=0)
			{
			ans.push_back(6);
			mp['S']--;
			mp['I']--;
			mp['X']--;}
		}
		
		if(mp['O'] && mp['N'] && mp['E'])
		{
			ans.push_back(1);
			mp['O']--;
			mp['N']--;
			mp['E']--;
			
		}
		
		if(mp['T'] && mp['H'] && mp['R'] && mp['E']>=2)
		{
			ans.push_back(3);
			mp['T']--;
			mp['H']--;
			mp['R']--;
			mp['E']--;
			mp['E']--;
		}
		
		if(mp['F'] && mp['I'] && mp['V'] && mp['E'])
		{
			ans.push_back(5);
			mp['F']--;
			mp['I']--;
			mp['V']--;
			mp['E']--;
		}
		
		
		
		if(mp['S'] && mp['E']>=2 && mp['V'] && mp['N'])
		{
			ans.push_back(7);
			mp['E']-=2;
			mp['S']--;
			mp['V']--;
			mp['N']--;
		}
		
		
		
		if(mp['N']>=2 && mp['I'] && mp['E'])
		{
			ans.push_back(9);
			mp['N']-=2;
			mp['I']--;
			mp['E']--;
		}
		}
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<test<<": ";
		for(unsigned int j=0;j<ans.size();++j)
		{
			cout<<ans[j];
		}
		cout<<"\n";
		mp.clear();
		
	}
	return 0;
}

