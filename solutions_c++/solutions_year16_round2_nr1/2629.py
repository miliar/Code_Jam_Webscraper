#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
int main()
{
	ifstream input;
	input.open("A-large.in", ios::in);
	ofstream output;
	output.open("Answer-A-large.txt", ios::out);
	int T, Q;
	vector<int> v;
	input>>T;
	Q=T;
	while(Q--)
	{
		int i, S[26], count=0;
		char c[2001];
		for(i=0;i<26;i++)
			S[i]=0;
		input>>c;
		for(i=0; i<strlen(c); i++)
		{
			if(c[i]=='A')
				S[0]++;
			else if(c[i]=='B')
				S[1]++;
			else if(c[i]=='C')
				S[2]++;
			else if(c[i]=='D')
				S[3]++;	
			else if(c[i]=='E')
				S[4]++;
			else if(c[i]=='F')
				S[5]++;
			else if(c[i]=='G')
				S[6]++;
			else if(c[i]=='H')
				S[7]++;
			else if(c[i]=='I')
				S[8]++;
			else if(c[i]=='J')
				S[9]++;
			else if(c[i]=='K')
				S[10]++;
			else if(c[i]=='L')
				S[11]++;
			else if(c[i]=='M')
				S[12]++;
			else if(c[i]=='N')
				S[13]++;
			else if(c[i]=='O')
				S[14]++;
			else if(c[i]=='P')
				S[15]++;
			else if(c[i]=='Q')
				S[16]++;
			else if(c[i]=='R')
				S[17]++;
			else if(c[i]=='S')
				S[18]++;
			else if(c[i]=='T')
				S[19]++;
			else if(c[i]=='U')
				S[20]++;
			else if(c[i]=='V')
				S[21]++;
			else if(c[i]=='W')
				S[22]++;
			else if(c[i]=='X')
				S[23]++;
			else if(c[i]=='Y')
				S[24]++;
			else if(c[i]=='Z')
				S[25]++;
		}
		
		count+=S[25];			//zero-z
		for(i=0;i<S[25];i++)
			v.push_back(0);
		S[4]-=S[25];			//E
		S[17]-=S[25];			//R
		S[14]-=S[25];			//O
		S[25]=0;				//z
		
		count+=S[23];			//six-x
		for(i=0;i<S[23];i++)
			v.push_back(6);
		S[18]-=S[23];			//s
		S[8]-=S[23];			//i
		S[23]=0;				//x
		
		count+=S[6];			//eight-g
		for(i=0;i<S[6];i++)
			v.push_back(8);
		S[4]-=S[6];				//E
		S[8]-=S[6];				//i
		S[7]-=S[6];				//h
		S[19]-=S[6];			//t
		S[6]=0;					//g
		
		count+=S[22];			//two-w
		for(i=0;i<S[22];i++)
			v.push_back(2);
		S[19]-=S[22];			//t
		S[14]-=S[22];			//o
		S[22]=0;				//w
		
		count+=S[20];			//four-u
		for(i=0;i<S[20];i++)
			v.push_back(4);
		S[5]-=S[20];			//f
		S[14]-=S[20];			//o
		S[17]-=S[20];			//r
		S[20]=0;				//u
		
		count+=S[7];			//three-h
		for(i=0;i<S[7];i++)
			v.push_back(3);
		S[19]-=S[7];			//t
		S[17]-=S[7];			//r
		S[4]-=(2*S[7]);			//e e
		S[7]=0;					//h
		
		count+=S[5];			//five-f
		for(i=0;i<S[5];i++)
			v.push_back(5);
		S[8]-=S[5];				//i
		S[21]-=S[5];			//v
		S[4]-=S[5];				//e
		S[5]=0;					//f
		
		count+=S[21];			//seven-v
		for(i=0;i<S[21];i++)
			v.push_back(7);
		S[18]-=S[21];			//s
		S[4]-=(2*S[21]);		//e e
		S[13]-=S[21];			//n
		S[21]=0;				//v
		
		count+=S[8];			//nine-i
		for(i=0;i<S[8];i++)
			v.push_back(9);
		S[13]-=(2*S[11]);		//n n
		S[4]-=S[11];			//e
		S[8]=0;
		
		count+=S[14];			//one-o
		for(i=0;i<S[14];i++)
			v.push_back(1);
		S[13]-=S[14];			//n
		S[4]-=S[14];			//e
		S[14]=0;
		
		output<<"Case #"<<(T-Q)<<": ";
		sort(v.begin(), v.end());
		for(i=0; i<v.size();i++)
			output<<v[i];
		output<<"\n";
		v.clear();
	}
	input.close();
	output.close();
	return 0;
}
