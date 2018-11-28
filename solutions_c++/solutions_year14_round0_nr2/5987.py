#include <iostream>
#include<iomanip>
#include <fstream>
using namespace std;

int main()
{
	ofstream out("B-large.out");
	ifstream in("B-large.in");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
	int n;
	cin>>n;
	for(int t=1;t<=n;t++){
		double c,f,x;
		cin>>c>>f>>x;
		double total_sec=0;
		double per_sec=2.0;
		while( x/per_sec > ( c/per_sec + x/(f+per_sec)) ){ //�����building���ѵ�ʱ����٣���ôӦ�ý�building
			total_sec+=c/per_sec;
			per_sec+=f;
		}
		//���ļ���
		total_sec +=x/per_sec;
		cout<<"Case #"<<t<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<total_sec<<endl;
	}
	return 0;
}

