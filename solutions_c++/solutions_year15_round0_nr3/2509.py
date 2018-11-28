// Dijkstra.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <string>

using namespace std;

map<char, map<char,char> > q;
map<string, char>cache;

char qmul(char _x, char _y )
{
	bool SignPos(true);
	char x, y;
	if(_x < 0) { SignPos = !SignPos; x=-_x;}else x=_x;
	if(_y < 0) { SignPos = !SignPos; y=-_y;}else y=_y;

	if(   ( x=='i' && (y=='i'||y=='k') )
		||( x=='j' && (y=='i'||y=='j') )
		||( x=='k' && (y=='k'||y=='j') )
		) SignPos = !SignPos;
	return SignPos ? q[x][y]:-q[x][y]; 
}

char eval(string in)
{
	if(in.size()>1) {
		map<string, char>::const_iterator it(cache.find(in));
		if(it == cache.end()) 
			return cache[in] = qmul(eval(in.substr(0,in.size()-1)),*in.rbegin());
		else return it->second;
	}
	else return in[0];
}

int _tmain(int argc, _TCHAR* argv[])
{
	map<char,char> q1,qi,qj,qk;
	q1['1']='1';q1['i']='i';q1['j']='j';q1['k']='k';
	qi['1']='i';qi['i']='1';qi['j']='k';qi['k']='j';
	qj['1']='j';qj['i']='k';qj['j']='1';qj['k']='i';
	qk['1']='k';qk['i']='j';qk['j']='i';qk['k']='1';
	q['1']=q1;
	q['i']=qi;
	q['j']=qj;
	q['k']=qk;

	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cache.clear();
		int L,X;
		set<unsigned int> IndexI,IndexK;
		bool Res(false);
		cin >> L >> X;
		string ins,inl;
		cin >> ins;
		for(int i=0;i<X;i++) inl=inl+ins;
		for(unsigned int i=1; i < inl.size()-1 ;i++) {
			if(eval( IndexI.empty() ? inl.substr(0,i) : (string("i")+inl.substr(*IndexI.rbegin(),i-*IndexI.rbegin()))) == 'i') 
				IndexI.insert(i);
		}
		if(! IndexI.empty()) {
			for(unsigned int j=inl.size()-1; j>1 ; j--) 
				if(eval( IndexK.empty() ?  inl.substr(j) : (inl.substr(j,*IndexK.begin()-j)+'k'    )) == 'k' )
					IndexK.insert(j);
			if(! IndexK.empty()) {

				int FirstI = *IndexI.begin();
				int FirstK = *IndexK.rbegin();

				bool HasJ = string::npos!=inl.substr(FirstI,FirstK-FirstI).find_first_of('j');
				bool HasI = string::npos!=inl.substr(FirstI,FirstK-FirstI).find_first_of('i');
				bool HasK = string::npos!=inl.substr(FirstI,FirstK-FirstI).find_first_of('k');
				if(HasJ || (HasI && HasK)) {
					cerr << "Is/Ks at " << IndexI.size() <<"\t"<<IndexK.size()<<" positions; Comb: " << IndexI.size()*IndexK.size() << endl; 
					for(set<unsigned int>::const_iterator IInt=IndexI.begin(); !Res && IInt != IndexI.end(); IInt++)
					{
						// find next K
						set<unsigned int>::const_iterator KInt=IndexK.begin();
						for(;  KInt != IndexK.end() && *KInt<*IInt; KInt++) continue;

							if(KInt != IndexK.end() &&eval(inl.substr(*IInt,*KInt-*IInt)) == 'j') Res = true;

					}
				}
			}
		}
		cout << "Case #" << NumCase << ": " << (Res?"YES":"NO");
		cout << endl;
		cerr << "Cache Size :" << cache.size() << endl;
	}
	return 0;
}
