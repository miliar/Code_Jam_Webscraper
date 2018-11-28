#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;


int main()
{
    freopen("D:\\A-large.in", "r", stdin);
    freopen("D:\\output.txt", "w", stdout);

    int t;
    cin>>t;
    for(int z=1; z<=t; ++z){
	string s; cin>>s;
	vector<int> V = vector<int>(100, 0);
	for(int i=0; i<s.size(); ++i)
		V[s[i]]++;
	vector<int> N = vector<int>(10, 0);
	//ZERO
	N[0] = V['Z'];
	V['Z']=0;
	V['E']-=N[0];
	V['R']-=N[0];
	V['O']-=N[0];
	//SIX
	N[6] = V['X'];
	V['S']-=N[6];
	V['I']-=N[6];
	V['X']=0;
	//SEVEN
	N[7] = V['S'];
	V['S']=0;
	V['E']-=2*N[7];
	V['V']-=N[7];
	V['N']-=N[7];
	//FIVE
	N[5] = V['V'];
	V['F']-=N[5];
	V['I']-=N[5];
	V['V']=0;
	V['E']-=N[5];
	//FOUR
	N[4] = V['F'];
	V['F']=0;
	V['O']-=N[4];
	V['U']-=N[4];
	V['R']-=N[4];
	//THREE
	N[3] = V['R'];
	V['T']-=N[3];
	V['H']-=N[3];
	V['R']=0;
	V['E']-=2*N[3];
	//TWO
	N[2] = V['W'];
	V['T']-=N[2];
	V['W']=0;
	V['O']-=N[2];
	//ONE
	N[1] = V['O'];
	V['O']=0;
	V['N']-=N[1];
	V['E']-=N[1];
	//EIGHT
	N[8] = V['G'];
	//NINE
	N[9] = V['N']/2;
	cout<<"Case #"<<z<<": ";
	for(int i=0; i<10; i++)
		for(int j=0; j<N[i]; j++)
			cout<<i;
	cout<<endl;
    }
}
