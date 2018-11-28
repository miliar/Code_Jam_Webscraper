#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>
using namespace std;

int main()
{
	ifstream ifp("k:\\A-large.in");
	ofstream ofp("k:\\output_large.out",ofstream::ate);

 /*   if((!ifp) || (!ofp))
	{
		cout<<"open fail"<<endl;
		return -1;
	}
	else
	   cout<<"open ok"<<endl;
*/

	int num;
	ifp>>num;
	string temp;
	getline(ifp, temp);
////cout<<num<<endl;
	int smax = 0;
	string str, str_line;
	int i = 0;
	while(i < num)
	{
		//获取原始输入
		getline(ifp, str_line);

////////cout<<str_line<<endl;

        istringstream iss(str_line);
		iss>>smax;
		iss>>str;
////////cout<<smax<<endl;
////////cout<<str<<endl;

        //处理原始输入成一致格式
		int len = smax + 1 - str.size() ; 
		if(str.empty())
			str.insert(str.size(), smax+1, '1');

		else if( len >0)
			str.insert(str.size(), len, '1');

////////cout<<str<<endl;
		//开始处理
        int ask = 0;
		int already_stand = str[0] - '0';
//		cout<<already_stand<<endl;
		int j;
		int add;
		for(j = 1; j < str.size(); j++)
		{
			if(   (already_stand < j)  &&   ((str[j] - '0') != 0)   )
			{
				add = j - already_stand;
				ask += add;
				already_stand += add + str[j] - '0';
			}
			else
                already_stand += str[j] - '0';
		}


        i++;
		ofp<<"Case #"<<i<<": "<<ask<<endl;

		

////////cout<<i<<endl;
	}
	return 0;
}
