#include "stdafx.h"
#include<stdio.h>
#include<string>
#include<math.h>
#include<errno.h>
#include<ctype.h>
#include<limits>
#include<stdlib.h>
#include<valarray>
#include<conio.h>
#include<iterator>
#include<numeric>
#include<iomanip>
#include<set>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
int t,c=1,n,i,DEP,WAR;
double temp,minnao,maxnao,minken,maxken,chnao,chken;
vector<double> nao,naot;
vector<double> ken,kent;

double max_ken()
{
	return (*std::max_element(ken.begin(),ken.end()));
}
double min_ken()
{
	return (*std::min_element(ken.begin(),ken.end()));
}
double max_nao()
{
	return (*std::max_element(nao.begin(),nao.end()));
}
double min_nao()
{
	return (*std::min_element(nao.begin(),nao.end()));
}
double max_kent()
{
	return (*std::max_element(kent.begin(),kent.end()));
}
double min_kent()
{
	return (*std::min_element(kent.begin(),kent.end()));
}
double max_naot()
{
	return (*std::max_element(naot.begin(),naot.end()));
}
double min_naot()
{
	return (*std::min_element(naot.begin(),naot.end()));
}
void destroy(double _chken,double _chnao)
{
	ken.erase(std::find(ken.begin(),ken.end(),_chken));
	nao.erase(std::find(nao.begin(),nao.end(),_chnao));
}
void destroyt(double _chken,double _chnao)
{
	kent.erase(std::find(kent.begin(),kent.end(),_chken));
	naot.erase(std::find(naot.begin(),naot.end(),_chnao));
}

int main(int argc,char* argv[])
{
	cin>>t;
	while(t--)
	{
		cin>>n;
		DEP=WAR=0;
		for(i=0;i<n;i++)
		{
			cin>>temp;
			nao.push_back(temp);
			naot.push_back(temp);
		}
		for(i=0;i<n;i++)
		{
			cin>>temp;
			ken.push_back(temp);
			kent.push_back(temp);
		}
		while(n!=0)
		{
			n--;
			if(min_nao()<=min_ken())
			{
				chken = max_ken();
				chnao = min_nao();
				destroy(chken,chnao);
			}
			else if(min_nao()>min_ken())
			{
				chken = min_ken();
				chnao = min_nao();
				destroy(chken,chnao);
				DEP++;
			}
			if(max_naot()>=max_kent())
			{
				chnao=max_naot();
				chken=min_kent();
				destroyt(chken,chnao);
				WAR++;
			}
			else if(max_naot()<max_kent())
			{
				chnao=max_naot();
				chken=max_kent();
				destroyt(chken,chnao);
			}
		}
		cout<<"Case #"<<c<<": "<<DEP<<" "<<WAR<<endl;
		c++;
	}
	//getch();
	return 0;
}