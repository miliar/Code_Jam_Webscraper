#include <fstream>
using namespace std;
ifstream cin("in.txt");
ofstream cout("out.txt");
int check(int a[], int b[]){
	int temp=17;
	for(int i=0; i<4; ++i)
		for(int j=0; j<4; ++j){
			if(a[i]==b[j])
				if(temp==17)
					temp=a[i];
				else
					return -1;
		}
	return temp;

}
void main(){

	int T,t0=0,a,b,mas1[4][4],mas2[4][4];
	cin >> T;
	while(t0++<T){
	cin >> a;
	 for(int i=0;i<4; ++i)
		 for(int j=0; j<4; ++j)
			 cin >> mas1[i][j];
	 cin >> b;
	 for(int i=0;i<4; ++i)
		 for(int j=0; j<4; ++j)
			 cin >> mas2[i][j];
	 int temp=check(mas1[a-1],mas2[b-1]);
	 cout << "Case #" << t0 << ": ";
	 if(temp==17)
		 cout << "Volunteer cheated!";
	 else if(temp==-1)
		 cout << "Bad magician!";
	 else
		 cout << temp;
	 cout << endl;
	}
}