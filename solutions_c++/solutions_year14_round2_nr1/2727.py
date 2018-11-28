
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>


using namespace std; 

int T,N;
char ary[101][200];
	char temp[1000];

void insertc(int i,int n,char ch){
	int len;

	strcpy(temp,ary[i]);
	ary[i][n]=ch;
	strcpy(ary[i]+n+1,temp+n);
}

void deletec(int i,int n,char ch){
	int len;
	
	len=strlen(ary[i]);
	strncpy(ary[i]+n,ary[i]+n+1,len-n-1);
	ary[i][len-1]=0;
}

void addch(int n, char ch){
	int i;
	for(i=0;i<N;i++){
		if(ary[i][n]!=ch){
			insertc(i,n,ch);
		}
	}
}

void delch(int n, char ch){
	int i;
	for(i=0;i<N;i++){
		if(ary[i][n]==ch){
			deletec(i,n,ch);
		}
	}
}

long transfer(){
	int i,j;
	long res;
	char ch1,ch2;
	int flag=0;
	int count;
	
	int m,n;
	
	res=0;
	
	ch1=ary[0][0];

	for(i=1;i<N;i++){
		if(ary[i][0]!=ch1){
			res=-1;
			return res;
		}
	}
	
	for(j=1;;){
		count=0;
		ch2='0';
		flag=0;
		for(i=0;i<N;i++){
			if(ary[i][j]!=ch1){
				if(ary[i][j]!=ch2){
					if(flag==0){
						ch2=ary[i][j];
						flag=1;
						count++;
					}
					else{
						res=-1;
						return res;
					}
				}
				else{
					count++;
				}
			}
		}
		if(count>N/2){
			delch(j,ch1);
			res+=(N-count);
			ch1=ch2;
		}
		else{
			addch(j,ch1);
			res+=count;
			j++;
		}
		
		if(ch1==0)
			break;
	}


	return res;
}

int main() {
	int T;
	long res;
	char str[1024];
	char ch;

	fstream fin("A-small-attempt1.in", ios::in);
	fstream fout("result.txt", ios::out);

	fin >> T;
	fin.getline(str,1024);
	

	for (int i=0;i<T;i++){
		fin >> N;
		fin.getline(str,1024);

		for(int j=0;j<N;j++){
			fin.getline(ary[j],1024);
		}

		res=transfer();
//		fin >> str;
		if(res>=0)
			fout << "Case #" << i+1 << ": " << res << endl;
		else if(res<0)
			fout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
		else{}

	}



	return 0;
}
