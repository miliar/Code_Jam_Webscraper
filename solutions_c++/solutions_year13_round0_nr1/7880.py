#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int main()
{

	ofstream fout("trial.out");
	ifstream fin("A-large.in");
	int T;
	vector <string> results;
	vector <int> re;
	
	fin>>T;
	for(int n=0;n<T;n++)
	{
		string space,one,two,three,four,a,b,c,d,e,f,g,h,i,j,k,l,m,s,o,p;
		fin>>one>>two>>three>>four;
		a=one.substr(0,1);b=one.substr(1,1);c=one.substr(2,1);d=one.substr(3,1);e=two.substr(0,1);f=two.substr(1,1);g=two.substr(2,1);h=two.substr(3,1);
		i=three.substr(0,1);j=three.substr(1,1);k=three.substr(2,1);l=three.substr(3,1);m=four.substr(0,1);s=four.substr(1,1);o=four.substr(2,1);p=four.substr(3,1);
		
		if( (a=="X" && b=="X" && c=="X" && d=="X") ||(e=="X" && f=="X" && g=="X" && h=="X") ||(i=="X" && j=="X" && k=="X" && l=="X") || 
			(m=="X" && s=="X" && o=="X" && p=="X") ||(a=="X" && e=="X" && i=="X" && m=="X") ||(b=="X" && f=="X" && j=="X" && s=="X") ||
			(c=="X" && g=="X" && k=="X" && o=="X") ||(d=="X" && h=="X" && l=="X" && p=="X") ||(a=="X" && f=="X" && k=="X" && p=="X") ||
			(d=="X" && g=="X" && j=="X" && m=="X") ||(a=="X" && b=="X" && c=="X" && d=="T") ||(a=="X" && b=="X" && c=="T" && d=="X") ||
			(a=="X" && b=="T" && c=="X" && d=="X") ||(a=="T" && b=="X" && c=="X" && d=="X") ||(e=="T" && f=="X" && g=="X" && h=="X") ||
			(e=="X" && f=="T" && g=="X" && h=="X") ||(e=="X" && f=="X" && g=="T" && h=="X") ||(e=="X" && f=="X" && g=="X" && h=="T") ||
			(i=="T" && j=="X" && k=="X" && l=="X") ||(i=="X" && j=="T" && k=="X" && l=="X") ||(i=="X" && j=="X" && k=="T" && l=="X") ||
			(i=="X" && j=="X" && k=="X" && l=="T") ||(m=="T" && s=="X" && o=="X" && p=="X") ||(m=="X" && s=="T" && o=="X" && p=="X") ||
			(m=="X" && s=="X" && o=="T" && p=="X") ||(m=="X" && s=="X" && o=="X" && p=="T") ||(a=="T" && e=="X" && i=="X" && m=="X") ||
			(a=="X" && e=="T" && i=="X" && m=="X") ||(a=="X" && e=="X" && i=="T" && m=="X") ||(a=="X" && e=="X" && i=="X" && m=="T") ||
			(b=="T" && f=="X" && j=="X" && s=="X") ||(b=="X" && f=="T" && j=="X" && s=="X") ||(b=="X" && f=="X" && j=="T" && s=="X") ||
			(b=="X" && f=="X" && j=="X" && s=="T") ||(c=="T" && g=="X" && k=="X" && o=="X") ||(c=="X" && g=="T" && k=="X" && o=="X") ||
			(c=="X" && g=="X" && k=="T" && o=="X") ||(c=="X" && g=="X" && k=="X" && o=="T") ||(d=="T" && h=="X" && l=="X" && p=="X") ||
			(d=="X" && h=="T" && l=="X" && p=="X") ||(d=="X" && h=="X" && l=="T" && p=="X") ||(d=="X" && h=="X" && l=="X" && p=="T") ||
			(a=="T" && f=="X" && k=="X" && p=="X") ||(a=="X" && f=="T" && k=="X" && p=="X") ||(a=="X" && f=="X" && k=="T" && p=="X") ||
			(a=="X" && f=="X" && k=="X" && p=="T") ||(d=="T" && g=="X" && j=="X" && m=="X") ||(d=="X" && g=="T" && j=="X" && m=="X") ||
			(d=="X" && g=="X" && j=="T" && m=="X") ||(d=="X" && g=="X" && j=="X" && m=="T") )
			
		{
			string q=": X won";
			results.push_back(q);
			re.push_back(n+1);

			
		}
		else
		{
		 if( (a=="O" && b=="O" && c=="O" && d=="O") ||(e=="O" && f=="O" && g=="O" && h=="O") ||(i=="O" && j=="O" && k=="O" && l=="O") || 
			(m=="O" && s=="O" && o=="O" && p=="O") ||(a=="O" && e=="O" && i=="O" && m=="O") ||(b=="O" && f=="O" && j=="O" && s=="O") ||
			(c=="O" && g=="O" && k=="O" && o=="O") ||(d=="O" && h=="O" && l=="O" && p=="O") ||(a=="O" && f=="O" && k=="O" && p=="O") ||
			(d=="O" && g=="O" && j=="O" && m=="O") ||(a=="O" && b=="O" && c=="O" && d=="T") ||(a=="O" && b=="O" && c=="T" && d=="O") ||
			(a=="O" && b=="T" && c=="O" && d=="O") ||(a=="T" && b=="O" && c=="O" && d=="O") ||(e=="T" && f=="O" && g=="O" && h=="O") ||
			(e=="O" && f=="T" && g=="O" && h=="O") ||(e=="O" && f=="O" && g=="T" && h=="O") ||(e=="O" && f=="O" && g=="O" && h=="T") ||
			(i=="T" && j=="O" && k=="O" && l=="O") ||(i=="O" && j=="T" && k=="O" && l=="O") ||(i=="O" && j=="O" && k=="T" && l=="O") ||
			(i=="O" && j=="O" && k=="O" && l=="T") ||(m=="T" && s=="O" && o=="O" && p=="O") ||(m=="O" && s=="T" && o=="O" && p=="O") ||
			(m=="O" && s=="O" && o=="T" && p=="O") ||(m=="O" && s=="O" && o=="O" && p=="T") ||(a=="T" && e=="O" && i=="O" && m=="O") ||
			(a=="O" && e=="T" && i=="O" && m=="O") ||(a=="O" && e=="O" && i=="T" && m=="O") ||(a=="O" && e=="O" && i=="O" && m=="T") ||
			(b=="T" && f=="O" && j=="O" && s=="O") ||(b=="O" && f=="T" && j=="O" && s=="O") ||(b=="O" && f=="O" && j=="T" && s=="O") ||
			(b=="O" && f=="O" && j=="O" && s=="T") ||(c=="T" && g=="O" && k=="O" && o=="O") ||(c=="O" && g=="T" && k=="O" && o=="O") ||
			(c=="O" && g=="O" && k=="T" && o=="O") ||(c=="O" && g=="O" && k=="O" && o=="T") ||(d=="T" && h=="O" && l=="O" && p=="O") ||
			(d=="O" && h=="T" && l=="O" && p=="O") ||(d=="O" && h=="O" && l=="T" && p=="O") ||(d=="O" && h=="O" && l=="O" && p=="T") ||
			(a=="T" && f=="O" && k=="O" && p=="O") ||(a=="O" && f=="T" && k=="O" && p=="O") ||(a=="O" && f=="O" && k=="T" && p=="O") ||
			(a=="O" && f=="O" && k=="O" && p=="T") ||(d=="T" && g=="O" && j=="O" && m=="O") ||(d=="O" && g=="T" && j=="O" && m=="O") ||
			(d=="O" && g=="O" && j=="T" && m=="O") ||(d=="O" && g=="O" && j=="O" && m=="T") )
			
		{
			string u=": O won";
			results.push_back(u);
			re.push_back(n+1);
			
		}
		 else
		{
			if(a=="." || b=="." ||c=="." ||d=="." ||e=="." ||f=="." ||g=="." ||h=="." ||i=="." ||j=="." ||k=="." ||l=="." ||m=="." ||s=="." ||
			o=="." || p=="." )
			{
			string v=": Game has not completed";
			results.push_back(v);
			re.push_back(n+1);
			}
			else
		{
			string l=": Draw";
			results.push_back(l);
			re.push_back(n+1);
			
		}
			
		}
		
		
	}
	}
	for(int i=0;i<results.size();i++)
	{
		fout<<"Case #"<<re[i]<<results[i]<<endl;
	}
	
	

return 0;
}