#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
	int T, len, cur, num;
	string str;
	ifstream fi;
	ofstream fo;
	fi.open("C://Bhavana//MyPrograms//CodeJam//Jam15//A-large.in");
	fo.open("output.txt");
	fi>>T;
	//cout<<T<<endl;
	
	for(int i=0;i<T;i++){
		fi>>len;
		fi>>str;
		//cout<<len<<" "<<str<<endl;
		cur = 0;
		num = 0;
		int p = 0;
		
		for(int j=0;j<len+1;j++){
			p = (int)(str[j]-48);
			if(cur < j){
				num += j - cur;
				cur = j + p;
			}
			else
			    cur += p;
		}
		fo<<"Case #"<<i+1<<": "<<num<<endl;
	}
	
	fi.close();
	fo.close();
}
