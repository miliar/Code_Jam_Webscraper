#include <iostream>
#include <list>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int a=0;a<t;a++)
	{
		cout<<"Case #"<<(a+1)<<": ";
	
		int n;
		cin>>n;
		
		list<double> naomi;
		double tmp;
		
		for(int i=0;i<n;i++){
			cin>>tmp;
			naomi.push_front(tmp);
		}
		
		list<double> ken;
		for(int i=0;i<n;i++){
			cin>>tmp;
			ken.push_front(tmp);
		}
		
		naomi.sort(); naomi.reverse();
		ken.sort(); ken.reverse();
		
		list<double> N(naomi.begin(),naomi.end()),K(ken.begin(),ken.end());
		
		int score=0;
		
		//cout<<naomi.front()<<" -------- "<<ken.back()<<endl;
		
		for(int i=0;i<n;i++)
		{
			if(naomi.back()>ken.back()){
				score++;
				ken.pop_back();
			}
			else{
				ken.pop_front();
			}
			naomi.pop_back();
		}
		
		cout<<score<<" ";
		
		score=0;
		
		for(int i=0;i<n;i++)
		{
			if(N.front()>K.front()){
				score++;
				K.pop_back();
			}
			else{
				K.pop_front();
			}
			N.pop_front();
		}
		
		cout<<score<<endl;
		
		naomi.clear();
		ken.clear();
		N.clear();
		K.clear();
	}
	
}
