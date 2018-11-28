#include<iostream>
#include<fstream>
#include<vector>
#include<iterator>
#include<algorithm>

using namespace std;



int main()
{

	ifstream fin;
	fin.open("D-large.in");
	
	ofstream fout;
	fout.open("output.txt");
	
	short int t,n;
	double temp,temp1;
	short int score, xscore;
	
	ostream_iterator<double> screen(cout," ");
	
	vector <double> naomi, ken, xnaomi, xken;
	vector <double> ::iterator np;
	vector <double> :: iterator kp;
	
	
	fin>>t;
	
	for(int i=0;i<t;i++)
	{
		fin>>n;
		score = 0;
		xscore=0;
		naomi.clear();
		ken.clear();
		xnaomi.clear();
		xken.clear();
		
		
		
		score= 0;
		for(int j=0;j<n;j++)
		{
			fin>>temp;
			naomi.push_back(temp);
		}
		
		for(int j=0;j<n;j++)
		{
			fin>>temp;
			ken.push_back(temp);
		}
		
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		
		xken.resize(n);
		xnaomi.resize(n);
		
		copy(naomi.begin(),naomi.end(),xnaomi.begin());
		copy(ken.begin(),ken.end(),xken.begin());
	/*	
		cout<<endl;
		copy(xnaomi.begin(),xnaomi.end(),screen); 
		cout<<endl;
		copy(xken.begin(),xken.end(),screen);
		cout<<endl;
	*/	
		// Lets play war first /////////////////
		
		while(naomi.size()!=0)
		{
		
		np = max_element(naomi.begin(),naomi.end());
		temp = *np;
		naomi.erase(np);
		
		
		kp = max_element(ken.begin(), ken.end());
		temp1 = *kp;
		
		if(temp1>temp)
		{
			for(kp=ken.begin();kp<ken.end();kp++)
			{
				if(*kp>temp)
				{
					
					ken.erase(kp);
					break;
				}
			}
		}
		
		else
		{
			score++;
			kp = min_element(ken.begin(),ken.end());
			ken.erase(kp);
			
		}
		
		
		}
	////////////////// war ends
	// Dhoka war start
		
		while(xnaomi.size()!=0)
		{
			
			
			
			np = max_element(xnaomi.begin(),xnaomi.end());
			temp = *np;
			//xnaomi.erase(np);
			
			kp = max_element(xken.begin(),xken.end());
			temp1 = *kp;
			
			if(temp>temp1)
			{
				xken.erase(kp);
				xscore++;
				
			}
			
			else
			{
				np = min_element(xnaomi.begin(),xnaomi.end());
				//kp = min_element(xken.begin(),xken.end());
				xken.erase(kp);
			}
			
			
			xnaomi.erase(np);
			
			
		}
	
		
		
		fout<<"Case #"<<i+1<<": "<<xscore<<" "<<score<<endl;
	
		
		
		
		
		
		
		
	
		
		
		
		
		
	}
	
	
}



