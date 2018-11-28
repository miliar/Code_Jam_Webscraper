#include <fstream>
//#include <iostream>
using namespace std;

int m, n, t, a[16], ans, line, tmp, k;
ifstream cin("input.in");
ofstream cout("output.out");
int main(){
	cin>>t;
	while(t--){
		memset(a,0,sizeof(a));
		for(int j=0; j<2; ++j){
			cin>>line;
			line--;
			for(int i=0; i<4*line; ++i)
				cin>>tmp;
			for(int i=0; i<4; ++i){
				cin>>tmp;
				a[tmp-1]++;
			}
			for(int i=0; i<4*(3-line); ++i)
				cin>>tmp;
		}
		ans=-1;
		cout<<"Case #"<<++k<<": ";
		for(int i=0; i<16; ++i){
			if (ans!=-1 && a[i]==2){
				ans=-2;
				break;
			}
			if (a[i]==2){
				ans=i+1;
			}
		}
		if (ans==-2)
			cout<<"Bad magician!\n";
		else if (ans==-1)
			cout<<"Volunteer cheated!\n";
		else
			cout<<ans<<endl;
	}
	return 0;
}
/*
4
3
4 5 2 13
16 12 3 15
1 7 14 10
11 8 6 9
2
12 5 11 10
16 15 8 4
7 1 3 2
13 6 14 9
2
7 16 9 6
3 10 13 14
11 4 15 1
12 5 2 8
4
12 16 6 11
5 9 8 7
1 4 2 15
10 3 13 14
3
11 2 6 5
7 13 16 4
8 9 14 15
10 1 3 12
2
15 2 6 8
7 11 4 3
5 10 1 12
9 13 14 16
3
16 2 14 1
4 3 15 5
8 10 7 9
13 11 12 6
1
3 9 5 12
6 14 11 16
2 4 7 13
10 1 8 15
*/