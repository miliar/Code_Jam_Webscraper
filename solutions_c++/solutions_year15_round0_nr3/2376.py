#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
string multi(string a,string d)
{
	string ret="";
	char c,b;
	if (a.length()>1)
	{
		ret="-";
		c=a[1];
	}
	else c=a[0];
	if (d.length()>1)
	{
		b=d[1];
		if (ret=="-") ret="";
		else ret="-";
	}
	else b=d[0];
	//cout << "@@@" << a << " " << d << " "<< c <<" "<< b <<  "###" << endl;
	switch (c)
	{
		case '1':
			ret+=b;
			return ret;
		case 'i':
			if (b=='1')
				if (ret=="-") return "-i";
				else return "i";
			if (b=='i')
				if (ret=="-") return "1";
				else return "-1";
			if (b=='j')
				if (ret=="-") return "-k";
				else return "k";
			if (b=='k')
				if (ret=="-") return "j";
				else return "-j";
		case 'j':
			switch (b)
			{
				case '1':
					if (ret=="-") return "-j";
					else return "j";	
				case 'i':
					if (ret=="-") return "k";
					else return "-k";
				case 'j':
					if (ret=="-") return "1";
					else return "-1";
				case 'k':
					if (ret=="-") return "-i";
					else return "i";
			}
		case 'k':
			switch (b)
			{
				case '1':
					if (ret=="-") return "-k";
					else return "k";
				case 'i':
					if (ret=="-") return "-j";
					else return "j";
				case 'j':
					if (ret=="-") return "i";
					else return "-i";
				case 'k':
					if (ret=="-") return "1";
					else return "-1";
			}
	}
}
int main()
{
	int t,i,l,y,j,k,o;
	ifstream fin("6.txt");
	ofstream fout("7.txt");
	string x,s,tmp;
	
	string now;
	fin >> t;
	for (i=0;i<t;i++)
	{
		fin >> l >> x;
		if (x.length()>2)
			x=x.substr(x.length()-2);
		y=stoi(x);
		if (y>12) y=y % 4+12;
		fin >> s;
		tmp="";
		l*=y;
		for (j=1;j<=y;j++) tmp=tmp+s;
		s=tmp;
	//cout << "doing : "<< s << " length:" << l << " Y:" << y<< " X:"<<x << endl;
		now="1";
		vector<int> oki,okk;
		for (j=0;j<l;j++)
		{
			now=multi(now,string(1,s[j]));
			if (now=="i")
			{
			//	cout <<"oki"<< j << ' ';
				oki.push_back(j);
			}
		}
		now="1";
		for (j=l-1;j>=0;j--)
		{
			now=multi(string(1,s[j]),now);
			if (now=="k") 
			{
				//cout << "okk " <<j << ' ';
				okk.push_back(j);
			}
		}
		//cout << oki.size() << ' '<< okk.size() << endl;
		for (j=0;j<oki.size();j++)
		{
			for (k=0;k<okk.size();k++)
			{
				if (oki[j]>=okk[k]-1) break;
			}
			k--;
			now="1";
			if (k<0) break;
			//cout << "j" << "!!!!" << k<< "@@@@";
			for (o=oki[j]+1;o<s.size();o++)
			{
				now=multi(now,string(1,s[o]));
				cout << now << ' ';
				if (okk[k]-1==o)
				{
					if (now=="j") break;
					k--;
					if (k<0) break;
				}
			}
			if (now=="j") break;
		}
		if (now=="j")
		{
			fout << "Case #"<<i+1<<": YES" << endl;
			cout << "Case #"<<i+1<<": YES" << endl;
		}
		else
		{
			fout << "Case #"<<i+1<<": NO" << endl;
			cout << "Case #"<<i+1<<": NO" << endl;
		}


	}
	return 0;
}