#include<conio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

class className{
	int P, Q;
public:
	void getData()
	{
		string str = "";
		in >> str;
		
		unsigned pos = str.find("/" );
		string temp = str.substr(pos+1);
		Q = atoi(temp.c_str());
		temp = str.substr(0,pos);
		P = atoi(temp.c_str());
		
		/*cout << P<<endl;
		cout << Q;*/
	}
	void check(int &noc);// no of case

};

int main()
{
	const int T = 100;
	className caseArr[T];
	int noc;
	in >> noc;
	int i;
	for (i = 0; i < noc; i++)
	{
		caseArr[i].getData();
	}
	for (i = 0; i < noc; i++)
	{
		caseArr[i].check(i);
	}


		_getch();
	return 0;
}

void className::check(int & noc)
{

	/*cout << P<<" "<<Q<< " "<<P/Q<<endl;*/
	out << "Case #" << noc + 1 << ": ";
	if (Q % 2 != 0)
	{
		out << "impossible\n";
		return;
	}
	int temp = Q;
	for (int i = 1; temp>=2 ;i++)
	{
		
		if (temp % 2 == 0)
		{
			temp = temp / 2;
		}
		else{
			out << "impossible" << endl;
			return;
		}
		
	}
	double num = (double)P / Q;
	int count = 0;
	for (int i = 1; i<40; i++){
		num = num * 2;
		count++;
		
		if (num >= 1){
			out << count << endl;
			break;
		}

	}
}