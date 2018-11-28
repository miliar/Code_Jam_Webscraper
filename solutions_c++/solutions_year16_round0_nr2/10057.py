#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <algorithm>
using namespace std;
int main(int i,char *args[]) {
	char ch[200],ch_rev[200];
	string str;
	int cnt_case=1,count_case,len;
	long int n;
	ifstream fin;
	ofstream fout;
	fin.open(args[1],ios::in);
	if(!fin) {
		cout<<"Can't open the file "<<args[1]<<" !!\n";
		return 1;
	}
	fout.open(args[2],ios::out);
	fin.getline(ch,200,'\n');
	count_case =atol(ch);
	while(1) {
		int flag=0,indx=0,count_rpt=-99,g_count=0,gi;
		char gc;
		fin.getline(ch,100,'\n');
		str=ch;
		len=str.length();
		indx=len-1;
		gc=ch[indx];
		
		count_rpt=std::count(str.begin(), str.end(), '-');
		if(count_rpt==0) {
			fout<<"Case #"<<cnt_case<<": "<<0<<'\n';
			cnt_case++;
			continue;
		} else if(count_rpt==len) {
			fout<<"Case #"<<cnt_case<<": "<<1<<'\n';
			cnt_case++;
			continue;
		} else if(count_rpt==1 && len==2) {
			if(ch[1]=='+') {
				fout<<"Case #"<<cnt_case<<": "<<1<<'\n';
			} else {
				fout<<"Case #"<<cnt_case<<": "<<2<<'\n';
			}
			cnt_case++;
			continue;
		} else {
			for(int i=len-2; i>=0; i--) {
				gi=i;
				if(ch[i]!=gc) {
					break;
				}
			}
			for(int i=0; i<=gi; i++) {
				if(ch[i]==ch[i+1]) {
				
					continue;
				} else {
					
					for(int j=i,k=0; j>=0; j--,k++) {
						if(ch[j]=='+') {
							ch_rev[k]='-';
							continue;
						} else {
							ch_rev[k]='+';

						}
					}
					for(int l=0;l<=i;l++) {
						ch[l]=ch_rev[l];
					}
					
					g_count++;

				}
			}
			if(ch[0]==gc &&gc=='+')
			{
				fout<<"Case #"<<cnt_case<<": "<<g_count<<'\n';
			}
			else if(ch[0]==gc &&gc=='-')
			{
				fout<<"Case #"<<cnt_case<<": "<<g_count+1<<'\n';
			}
			else
			{
				fout<<"Case #"<<cnt_case<<": "<<'\n';
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

