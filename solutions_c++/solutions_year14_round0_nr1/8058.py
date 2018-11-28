#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<set>
using namespace std;

int N,M;


int main(){
ofstream out("prvi.txt");

cin>>N;
int cookie = 1;

while( N--){
	
int a,b;
int polje1[4][4];
int polje2[4][4];

cin>>a;
for ( int i = 0; i<4; i++) 
	for( int j = 0; j<4; j++) 
		cin>>polje1[i][j];	



cin>>b;
for ( int i = 0; i<4; i++) 
	for( int j = 0; j<4; j++) 
		cin>>polje2[i][j];	

a--;b--;

int ima[20];
memset(ima, 0, sizeof (ima));

for( int i = 0; i<4; i++) ima[polje1[a][i]]++;	
for( int i = 0; i<4; i++) ima[polje2[b][i]]++;
	
set<int> rj;
int x;
	
for( int i = 0; i<20; i++) 
if( ima[i] >1) rj.insert(i);

for( auto i: rj) x = i;

if( rj.size() == 1) out<<"Case #"<<cookie<<": "<<x<<endl;
else if( rj.size() > 1) out<<"Case #"<<cookie<<": "<<"Bad magician!"<<endl;
else out<<"Case #"<<cookie<<": "<<"Volunteer cheated!"<<endl;

cookie++;
}
return 0;
}

