#include<bits/stdc++.h>
using namespace std;

map<char,int>m;

vector< char>v;


int main(){

	int t,counter=1;
	string s;
	freopen("a.txt","w+",stdout);
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		for(int j=0;j<s.size();j++)
		{
			m[s[j]]++;
			//cout<<s[j]<<" ";
			//cout<<m[s[j]]<<endl;
		}
		if(m['Z']>=1)
		{

			while(m['Z']--)
			{
						v.push_back('0');

				m['E']--;
				m['R']--;
				m['O']--;
			}

		}

		 if(m['W']>=1)
		{

			while(m['W']--)
			{
				v.push_back('2');
				m['T']--;
				m['O']--;
		//		cout<<"run\n";
			}
		}

		 if(m['U']>=1)
		{

			while(m['U']--)
			{
						v.push_back('4');
					m['F']--;
					m['O']--;
					m['R']--;

			}

		}
		if(m['X']>=1)
		{

			while(m['X']--)
			{
			v.push_back('6');
				m['S']--;
				m['I']--;
			}
		}

		 if(m['G']>=1)
		{

			while(m['G']--)
			{

			v.push_back('8');
			m['E']--;
			m['I']--;
			m['H']--;
			m['T']--;

			}
		}



		if(m['O']>=1)

		{

			while(m['O']--)
				{
					v.push_back('1');
					m['E']--;
					m['N']--;
				}
		}

		if(m['F']>=1)
		{

			while(m['F']--)
			{
				v.push_back('5');
				m['I']--;
				m['E']--;
				m['V']--;
			}
		}


		 if(m['T']>=1)
		{

//			cout<<m['R']<<" ";
			while(m['T']--)
			{
						 v.push_back('3');
						 m['R']--;
						m['H']--;
						m['E']--;
						m['E']--;
			}

		}
		if(m['S']>=1)
		{

			while(m['S']--)
			{v.push_back('7');
				m['V']--;
				m['E']--;
				m['E']--;
				m['N']--;
			}
		}


		if(m['N']>=1&&m['I']>=1)
		{

			while(m['N']--&&m['I']--)
			{
				v.push_back('9');
				m['N']--;
				m['E']--;
			}
		}
		sort(v.begin(),v.end());

		cout<<"Case #"<<counter++<<": ";
		for(int k=0;k<v.size();k++)
		{
			cout<<v[k];
		}
		cout<<endl;
		v.clear();
		m.clear();
		s.clear();

	}
	return 0;
}
