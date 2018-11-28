#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

bool debug=false;

void solveCase(int c)
{
	int first, second;
	int rows1[4][4];
	int rows2[4][4];
	cin>>first;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>rows1[i][j];
	cin>>second;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>rows2[i][j];
	int count = 0;
	int answer = 0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++){
			if(rows1[first-1][i]==rows2[second-1][j]){
				answer = rows1[first-1][i];
				count++;
			}
		}
	if(count==1)
		cout<<"Case #"<<c<<": "<<answer<<endl;
	else if ( count == 0 )
		cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
	else
		cout<<"Case #"<<c<<": Bad magician!"<<endl;
		
}

void solve()
{
	int T;
	cin>>T;
	int c=0;
	while((++c)<=T){
		solveCase(c);
	}
}

int main(int argc, char** args)
{
	if(argc>1&&args[1][0]=='d'){
		debug=true;
		freopen("sample.in","r",stdin);
	}
    solve();
}

