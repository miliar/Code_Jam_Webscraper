#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>


using namespace std;

int n;
set<pair<int,int> > Q;


int main()
{
	int t,T;
	//ifstream fin("input.txt");
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	
	fin>>T;

	for(t=0;t<T;t++){
		fin>>n;
		Q.clear();
		int a;
		for(int i=0;i<n;i++){
			fin>>a;
			Q.insert(make_pair(a,i));
		}
		fout<<"Case #"<<t+1<<":";
		set<pair<int,int> >::iterator pos,tmp,er;
		while(!Q.empty()){
			pos = Q.end();
			pos--;
			er = pos;
			int num,ch;
			num = pos->first;
			ch = pos->second;
			tmp = pos;
			if(pos != Q.begin())
				tmp--;			
			if(pos != Q.begin() && num == tmp->first){
				pos--;
				int num2 = pos->first;
				int ch2 = pos->second;
				tmp = pos;
				if(pos != Q.begin())
					tmp--;
				if(pos != Q.begin() && num == tmp->first){
					if(num>1){
						num-=2;
						string s;
						char temp = 'A'+ch;
						s = temp;
						s+= temp;
						fout<<" "<<s;
						if(num != 0)
							Q.insert(make_pair(num,ch));
					}
					else{
						string s;
						char temp = 'A'+ch;
						s = temp;
						fout<<" "<<s;
					}
				}
				else{
					Q.erase(pos);
					string s;
					char temp = 'A'+ch;
					s = temp;
					temp = 'A'+ch2;
					s+=temp;
					fout<<" "<<s;
					if(num > 1)
						Q.insert(make_pair(num-1,ch));
					if(num2 > 1)
						Q.insert(make_pair(num2-1,ch2));					

				}
			}
			else{
				if(num>1){
					num-=2;
					string s;
					char temp = 'A'+ch;
					s = temp;
					s+= temp;
					fout<<" "<<s;
					if(num != 0)
						Q.insert(make_pair(num,ch));
				}
				else{
					string s;
					char temp = 'A'+ch;
					s = temp;
					fout<<" "<<s;
				}
			}
			Q.erase(er);
		}
		fout<<endl;
		
	}

	return 0;
}


//fout.setf(ios::fixed);
//fout.precision(6);