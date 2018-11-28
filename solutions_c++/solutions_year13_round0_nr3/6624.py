#include<iostream>
#include<cmath>
#include<string>
#include<sstream>
#include<fstream>

using namespace std;

ifstream ifs("C-small-attempt0.in");
ofstream ofs("ans.txt");

string IntToString(int number)
{
  stringstream ss;
  ss << number;
  return ss.str();
}

int main(){
	int n;//s”
	int a,b;
	int i,j,k;
	int sa2=0;
	int count;
	float sa,sb;
	int temp;
	int flag=0;
	string str;

	//“ü—Í
	ifs >> n;

	for(i=0;i<n;i++){
		ifs >> a >> b;
		sa = sqrt((float)a);
		sb = sqrt((float)b);

		count = 0;
		
		if((int)sa*(int)sa!=a) 
			sa2 = (int)sa +1;
		else
			sa2 = (int)sa;

		/*temp = 10;

		str = IntToString(temp);
		
		cout <<str<< str[0] <<  str[str.size()-1] << endl;

		return 0;
		*/

		for(j=sa2;j<=(int)sb;j++){
			flag = 0;
			temp = j;
			str = IntToString(temp);
			k=0;
			while(1){
				if(str.size()==1){
					flag = 2;
					break;
				}

			//	cout <<str<< str[k] << str[str.size()-1-k] << endl;
				if(str[k]==str[str.size()-1-k]){}
				else{
					flag = 1;
					break;
				}
				
				if(((int)(str.size()/2))<=k){
					flag = 2;
					break;
				}
				
				k++;
			}


			temp = j*j;
			str = IntToString(temp);
			
			k=0;
			
			if(flag ==2){ 
			while(1){
				if(str.size()==1){
					flag = 2;
					break;
				}

			//	cout <<str<< str[k] << str[str.size()-1-k] << endl;
				if(str[k]==str[str.size()-1-k]){}
				else{
					flag = 1;
					break;
				}
				
				if(((int)(str.size()/2))<=k){
					flag = 2;
					break;
				}
				
				k++;
			}
			if(flag==2)
				count++;
		}
		}
		ofs << "Case #"<< (i+1) <<": "<< count << endl;

	}

	return 0;
}