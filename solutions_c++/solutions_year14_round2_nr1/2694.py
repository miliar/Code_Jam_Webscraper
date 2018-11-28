#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cmath>
using namespace std;
int main()
{
	int T;
	cin>>T;
	int counter=0;
	int n;
	while(T--)
	{    
		cin>>n;
		bool pos=true;
		vector <string> v;
		string temp;
		cin>>temp;
		string comp;
		comp=temp;
		v.push_back(temp);
		string::iterator it;
		it=unique(comp.begin(),comp.end());
		comp.resize(distance(comp.begin(),it));
		vector <int> counts(comp.size());
		for (int i=1;i<n;i++){
			string temp,temp2;
			cin>>temp;
			temp2=temp;
			//cout<<temp2<<endl;
			string::iterator it;
			it=unique(temp2.begin(),temp2.end());
			temp2.resize(distance(temp2.begin(),it));
			//cout<<temp2<<endl;
			if(temp2!=comp)pos=false;
			v.push_back(temp);
		}
		//cout<<comp<<endl;
		//for(int i=0;i<n;i++){
		//	cout<<v[i]<<endl;
		//}
		vector <vector <int> > all(n,vector <int> (comp.size(),0));
		for(int i=0;i<n;i++)
		{
			int k=0;
			int count=0;
			for(int j=0;j<comp.size();j++){
				while(v[i][k]==comp[j] && k < v[i].size()){
					k++;count++;
				}
				counts[j]+=count;
				all[i][j]=count;
				count=0;
			}
		}
		for(int i=0;i<counts.size();i++){
			counts[i]=floor((counts[i])/n+0.5);
		}
		int answer=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<comp.size();j++)
			{
				answer=answer + abs(all[i][j] - counts[j]);
			}
		}
		counter++;
		cout<<"Case #"<<counter<<": ";
		if(!pos)printf("Fegla Won \n");
        else printf("%i \n",answer);
	}
}