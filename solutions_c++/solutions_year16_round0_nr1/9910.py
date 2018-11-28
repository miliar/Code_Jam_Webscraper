#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main(int i,char *args[]) {
	int digits[10]= {0,1,2,3,4,5,6,7,8,9};
	char ch[100];
	int cnt_case=1,mul_indx=0;
	long int count_case,n,org_n;
	char ch_num;
	ifstream	fin;
	ofstream fout;
	fin.open(args[1],ios::in);
	if(!fin) {
		cout<<"Can't open the file "<<args[1]<<" !!\n";
		return 1;
	}
	fout.open(args[2],ios::out);
	fin.getline(ch,100,'\n');
	count_case=atol(ch);
	while(1) {
		int dig_fnd[10]= {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		fin.getline(ch,100,'\n');
		n=atol(ch);
		org_n=n;
		mul_indx=0;
		int r=0;
		long int t;
		if(n==0) {
			fout<<"Case #"<<cnt_case<<": "<<"INSOMNIA"<<'\n';
			cnt_case ++;
			continue;
		}
		while(1) {
			int g_flag=0;
			mul_indx++;			
			n=org_n*mul_indx;
			t=n;
			while(t>0) {
				int flag=0;
				r=t%10;
				for(int i=0; i<10; i++) {
					if(r==digits[i]) {
						if(dig_fnd[i]==-1) {
							dig_fnd[i]=r;
							break;
						}
					}
				}
				for(int i=0; i<10; i++) {
				if(dig_fnd[i]==-1) {
					flag=1;
					break;
				}
			}
			if(flag==0) {
				fout<<"Case #"<<cnt_case<<": "<<n<<'\n';
				g_flag=1;
				break;
			}

				t=t/10;
			}

			if(g_flag==1) {
				break;
			}

		}
		if (fin.eof()||cnt_case==count_case) {
			break;
		}
		cnt_case++;
	}

	fin.close();
	fout.close();
	return 0;
}

