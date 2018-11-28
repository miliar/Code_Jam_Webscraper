#include<bits/stdc++.h>
using namespace std;
int n;
list<double> np,kp;
int playFair()
{
	list<double>::iterator ni,ki;
	int win=n;
	for(ni=np.begin(),ki=kp.begin();ni!=np.end();ni++,ki++)
	{
		while(!(ki==kp.end() || *ki>*ni))ki++;
		if(ki!=kp.end())
			win--;
		else
			break; 
	} 
	return win;
}
bool check()
{
	list<double>::iterator ni,ki;
	for(ni=np.begin(),ki=kp.begin();ni!=np.end();ni++,ki++)
	{
		if(!(*ni>*ki))return false;
	}
	return true;
}
int playUnfair()
{
	while(!check())
	{
		np.pop_front();
		kp.pop_back();
	}
	return np.size();
}
int main()
{
	int T,no=1;
	cin>>T;
	while(T--)
	{
		cin>>n;
		np.clear();
		kp.clear();
		double temp;
		for(int i=0;i<n;i++){
			cin>>temp;
			np.push_back(temp);
		}
		for(int i=0;i<n;i++){
			cin>>temp;
			kp.push_back(temp);
		}
		np.sort();
		kp.sort();
		printf("Case #%d: %d %d\n",no++,playUnfair(),playFair());
	}
}

