#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<string>
using namespace std;

struct No
{
	char val;
	int sign;
	No()
	{}
	No(char c, int s = 1)
	{
		val = c;
		if (!s)
			sign = -1;
		else
		sign = s;
	}
};

No multi[4][4];

No multiply(No a, No b)
{
	int r, c;
	if (a.val == '1')
		r = 0;
	else
		r = a.val - 'i' + 1;

	if (b.val == '1')
		c = 0;
	else
		c = b.val - 'i' + 1;

	No ret = multi[r][c];

	ret.sign = (a.sign*b.sign*ret.sign);

	return ret;
}

bool Search(string str, No key, No res, int start = 1, int code = 0)
{
	

	for (int i = start; i <= str.length(); i++)
	{
		if (res.sign == key.sign && res.val == key.val)
		{
			if (code == 0)
			{
				return (Search(str, *(new No('j')), *(new No(str[i])), i + 1, 1));
					 
			}
			else if (code == 1)
			{

				return (Search(str, *(new No('k')), *(new No(str[i])), i + 1, 2));
					
			}
			else if (str.length()==i)
				return true;
		}
		No temp(str[i]);
		res = multiply(res, temp);
		
	}
	return false;
}

int main()
{
	multi[0][0] = *(new No('1'));
	multi[0][1] = *(new No('i'));
	multi[0][2] = *(new No('j'));
	multi[0][3] = *(new No('k'));

	multi[1][0] = *(new No('i'));
	multi[1][1] = *(new No('1', false));
	multi[1][2] = *(new No('k'));
	multi[1][3] = *(new No('j', false));

	multi[2][0] = *(new No('j'));
	multi[2][1] = *(new No('k', false));
	multi[2][2] = *(new No('1',false));
	multi[2][3] = *(new No('i'));

	multi[3][0] = *(new No('k'));
	multi[3][1] = *(new No('j'));
	multi[3][2] = *(new No('i',false));
	multi[3][3] = *(new No('1', false));


	ifstream ifile;
	ifile.open("C-small-attempt1.in");
	
	int total;
	ifile >>total;
	ofstream ofile;
	ofile.open("output.txt");
	int len;
	string dummy, str;
	int  i = 1;
	for (size_t j = 0; j < total; j++)
	{
		ifile >> len >> len;
		ifile >> dummy;
		str = "";
		for (int k = 0; k < len; k++)
		{
			str += dummy;
		}
		No res(str[0]);
		
		i = 1;
		bool iFound=false, jFound = false , kFound = false;
		iFound = Search(str, *(new No('i')), res);



		ofile << "Case #" << j + 1 << ": ";
		//if (iFound&& jFound && kFound)
		if (iFound)
			ofile << "YES";
		else 
			ofile << "NO";
		ofile << endl;
		
	}



	ifile.close();
	ofile.close();

	


	return 0;
}